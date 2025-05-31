import requests
from typing import Any, List, Optional
from langchain_core.outputs import LLMResult
from langchain_core.language_models import BaseChatModel
from langchain_core.messages import BaseMessage
from pydantic import Field, PrivateAttr

class ChatGroqLLM(BaseChatModel):
    api_key: str = Field(..., description="API key for Groq")
    model: str = Field(..., description="Model name to use")
    _client: Any = PrivateAttr()

    def _generate(
        self,
        messages: List[BaseMessage],
        stop: Optional[List[str]] = None,
        run_manager: Optional[Any] = None,
        **kwargs: Any,
    ) -> LLMResult:
        formatted_messages = [
            {"role": message.type, "content": message.content}
            for message in messages
        ]

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "messages": formatted_messages,
            "model": self.model,
            "stream": False
        }
        response = requests.post("https://api.groq.com/v1/chat/completions", json=payload, headers=headers)
        response.raise_for_status()
        data = response.json()
        return LLMResult(generations=[[{"text": data['choices'][0]['message']['content']}]])

    @property
    def _llm_type(self) -> str:
        return "chatgroq"