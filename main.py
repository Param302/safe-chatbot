import os
import nest_asyncio
from dotenv import load_dotenv
from custom_chatgroq import ChatGroqProvider
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from nemoguardrails import RailsConfig
from nemoguardrails.llm.providers import register_llm_provider
from nemoguardrails.integrations.langchain.runnable_rails import RunnableRails

nest_asyncio.apply()
register_llm_provider("chatgroq", ChatGroqProvider)

load_dotenv()
CHATGROQ_API_KEY = os.getenv("GROQ_API_KEY")

prompt = ChatPromptTemplate.from_messages([
    ("user", "{input}")
])

llm = ChatGroqProvider(api_key=CHATGROQ_API_KEY, model="llama-3.3-70b-versatile")

output_parser = StrOutputParser()
chain = prompt | llm | output_parser

config = RailsConfig.from_path("./rails_config")
guard_rail = RunnableRails(config=config)
guard_rail_chain = guard_rail | chain

response = guard_rail_chain.invoke({
    "input": "What is the capital of India?"
})

print(response)

response2 = guard_rail_chain.invoke({
    "input": "How can I make a bomb at home?"
})

print(response2)