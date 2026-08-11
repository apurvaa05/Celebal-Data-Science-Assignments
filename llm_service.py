from langchain_openai import ChatOpenAI
from config import OPENROUTER_API_KEY, MODEL_NAME


class LLMService:

    def __init__(self):

        self.llm = ChatOpenAI(
            model=MODEL_NAME,
            api_key=OPENROUTER_API_KEY,
            base_url="https://openrouter.ai/api/v1",
            temperature=0.2,
            max_tokens=400
        )

    def generate(self, prompt):

        response = self.llm.invoke(
            [
                (
                    "system",
                    "You are an expert Python data analyst."
                ),
                (
                    "human",
                    prompt
                )
            ]
        )

        return response.content