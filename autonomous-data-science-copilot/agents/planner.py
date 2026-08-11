from services.llm_service import LLMService
from agents.prompts import SYSTEM_PROMPT


class PlannerAgent:

    def __init__(self):
        self.llm = LLMService()

    def plan(self, question, columns):

        prompt = f"""
{SYSTEM_PROMPT}

Dataset Columns:
{columns}

User Question:
{question}

Return ONLY executable Pandas code.
"""

        return self.llm.generate(prompt)