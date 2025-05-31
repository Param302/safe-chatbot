from typing import Optional, List
from langchain_groq.chat_models import ChatGroq

class ChatGroqProvider(ChatGroq):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def _call(self, prompt: str, stop: Optional[List[str]] = None, **kwargs) -> str:
        # return self.model.predict(prompt)
        return super()._call(prompt, stop=stop, **kwargs)

    async def _acall(self, prompt: str, stop: Optional[List[str]] = None, **kwargs) -> str:
        # return await self.model.apredict(prompt)
        return await super()._acall(prompt, stop=stop, **kwargs)

    @property
    def _llm_type(self) -> str:
        return "chatgroq"
