import ast
import os
import pickle
import subprocess
import sys
import tempfile

import pandas as pd


class ExecutionEngine:
    """
    Executes AI-generated Pandas code inside an isolated Python subprocess.
    """

    def execute(self, code: str, df: pd.DataFrame):

        with tempfile.TemporaryDirectory() as temp_dir:

            input_path = os.path.join(temp_dir, "input.pkl")
            output_path = os.path.join(temp_dir, "output.pkl")
            runner_path = os.path.join(temp_dir, "runner.py")

            df.to_pickle(input_path)

            runner_code = '''
import ast
import pickle
import sys
import traceback
import pandas as pd


input_path = sys.argv[1]
output_path = sys.argv[2]

try:

    df = pd.read_pickle(input_path)

    scope = {
        "df": df,
        "pd": pd
    }

    code = """CODE_PLACEHOLDER"""

    tree = ast.parse(code)

    if len(tree.body) == 1 and isinstance(tree.body[0], ast.Expr):

        result = eval(
            compile(
                ast.Expression(tree.body[0].value),
                "<generated_code>",
                "eval"
            ),
            {},
            scope
        )

    else:

        exec(code, {}, scope)
        result = None

    with open(output_path, "wb") as f:
        pickle.dump(
            {
                "success": True,
                "result": result
            },
            f
        )

except Exception as e:

    with open(output_path, "wb") as f:
        pickle.dump(
            {
                "success": False,
                "error": str(e),
                "traceback": traceback.format_exc()
            },
            f
        )
'''

            runner_code = runner_code.replace(
                "CODE_PLACEHOLDER",
                code.replace("\\", "\\\\").replace('"""', '\\"\\"\\"')
            )

            with open(runner_path, "w", encoding="utf-8") as f:
                f.write(runner_code)

            try:

                process = subprocess.run(
                    [
                        sys.executable,
                        runner_path,
                        input_path,
                        output_path
                    ],
                    capture_output=True,
                    text=True,
                    timeout=30
                )

            except subprocess.TimeoutExpired:

                return {
                    "success": False,
                    "error": "Execution timed out after 30 seconds."
                }

            if not os.path.exists(output_path):

                return {
                    "success": False,
                    "error": process.stderr or "Subprocess execution failed."
                }

            try:

                with open(output_path, "rb") as f:
                    result = pickle.load(f)

                return result

            except Exception as e:

                return {
                    "success": False,
                    "error": str(e)
                }