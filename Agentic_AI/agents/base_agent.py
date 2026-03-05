from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

class BaseAgent:

    def __init__(self):
        self.llm = ChatOpenAI(
            model=os.getenv("MODEL_NAME", "gpt-4o-mini"),
            temperature=0
        )