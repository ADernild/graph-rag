from langchain_community.llms import VLLMOpenAI


class LLMConfig:
    def __init__(
        self,
        model_name: str,
        temperature: float,
        max_tokens: int,
        top_p: float,
        frequency_penalty: int,
        presence_penalty: int,
        api_key: str = "EMPTY",
        api_base: str = "http://host.docker.internal:1234/v1",
    ):
        self.llm = VLLMOpenAI(
            openai_api_key=api_key,
            openai_api_base=api_base,
            model_name=model_name,
            temperature=temperature,
            max_tokens=max_tokens,
            top_p=top_p,
            frequency_penalty=frequency_penalty,
            presence_penalty=presence_penalty,
        )
