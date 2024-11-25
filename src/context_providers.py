from atomic_agents.lib.components.system_prompt_generator import SystemPromptContextProviderBase


class SourceCodeContextProvider(SystemPromptContextProviderBase):
    def __init__(self, language: str):
        super().__init__(language)
        self.language = language
        self.source_code = ""

    def get_info(self) -> str:
        return f"```{self.language}\n{self.source_code}\n```"
