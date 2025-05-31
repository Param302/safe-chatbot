import os
from groq import Groq
from dotenv import load_dotenv
from langchain_groq import ChatGroq
# from nemoguardrails import RailsConfig
# from nemoguardrails.integrations.langchain.runnable_rails import RunnableRails

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

CHATGROQ_API_KEY = os.getenv("CHATGROQ_API_KEY")

# config = RailsConfig.from_path("./rails_config")

chatgroqllm = ChatGroq(
    api_key=CHATGROQ_API_KEY,
    model="llama-3.3-70b-versatile",
)

# guardrails = RunnableRails(config=config)

prompt = ChatPromptTemplate.from_messages([
    # ("system", "You are a helpful assistant."),
    ("user", "{input}")
])

output_parser = StrOutputParser()

chain = prompt | chatgroqllm | output_parser
# chain_with_guardrails = guardrails | chain

messages = [
    ("system", "You are a helpful assistant."),
    ("user", "?"),
]

input_ = {"input": "What is the capital of India?"}

print(chain.invoke(input_))
# print(chain_with_guardrails.invoke(input_))
