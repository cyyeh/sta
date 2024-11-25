from atomic_agents.lib.components.system_prompt_generator import SystemPromptContextProviderBase


class CodeContextProvider(SystemPromptContextProviderBase):
    def __init__(self, language: str):
        super().__init__(language)
        self.language = language
        # as of now, we only support one source code and one test code
        self.source_code = ""
        self.test_code = ""

    def get_info(self) -> str:
        return f"```{self.language}\n{self.source_code}\n```\n\n```{self.language}\n{self.test_code}\n```"
