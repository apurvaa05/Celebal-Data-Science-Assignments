from services.llm_service import LLMService
from services.rag_service import RAGService


class RecoveryAgent:

    def __init__(self):
        self.llm = LLMService()
        self.rag = RAGService()

    def recover(self, code: str, error: str, columns):

        query = f"""
Python Pandas error:

{error}

Previous code:

{code}

Find the relevant Python or Pandas documentation needed to fix this error.
"""

        documentation = self.rag.retrieve(query, k=3)

        prompt = f"""
You are an expert Python and Pandas data analyst.

The previous Python/Pandas code failed.

Dataset columns:
{list(columns)}

Previous code:
{code}

Error:
{error}

Relevant Python/Pandas documentation retrieved using RAG:
{documentation}

Use the retrieved documentation to understand and fix the error.

Return corrected executable Python code.

Rules:
- Return ONLY Python code.
- No markdown.
- No explanation.
- Use only existing dataframe columns.
- DataFrame variable is df.
- Do not invent columns.
- Preserve the original user intent.
"""

        return self.llm.generate(prompt)