import instructor
import openai
from atomic_agents.lib.components.system_prompt_generator import SystemPromptGenerator
from atomic_agents.agents.base_agent import BaseAgent, BaseAgentConfig
from atomic_agents.lib.components.agent_memory import AgentMemory
from atomic_agents.lib.base.base_io_schema import BaseIOSchema

from src.config import ChatConfig


class CodeRewriteInputSchema(BaseIOSchema):
    """Input schema for the code rewrite agent"""

    user_message: str


class CodeRewriteOutputSchema(BaseIOSchema):
    """Output schema for the code rewrite agent"""

    rewritten_code: str


code_rewrite_agent = BaseAgent(
    BaseAgentConfig(
        client=instructor.from_openai(openai.OpenAI(api_key=ChatConfig.api_key)),
        model=ChatConfig.model,
        system_prompt_generator=SystemPromptGenerator(
            background=[
                "You are a great programmer!",
            ],
            steps=[],
            output_instructions=[],
        ),
        input_schema=CodeRewriteInputSchema,
        output_schema=CodeRewriteOutputSchema,
        temperature=0,
        max_tokens=None,
    )
)
