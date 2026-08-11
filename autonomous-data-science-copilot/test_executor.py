import pandas as pd

from agents.planner import PlannerAgent
from agents.executor import ExecutionEngine


df = pd.DataFrame({

    "Name": [
        "John",
        "Alice",
        "Bob",
        "Emma"
    ],

    "Department": [
        "HR",
        "IT",
        "IT",
        "Finance"
    ],

    "Salary": [
        50000,
        65000,
        55000,
        72000
    ]

})


planner = PlannerAgent()

executor = ExecutionEngine()


question = "Show average salary by department"

code = planner.plan(
    question,
    list(df.columns)
)

print("\nGenerated Code:\n")
print(code)

print("\nExecution Result:\n")

result = executor.execute(code, df)

print(result)