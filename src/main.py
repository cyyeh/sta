from pathlib import Path

import orjson

from src.agents.code_rewrite import code_rewrite_agent, CodeRewriteInputSchema
from src.context_providers import SourceCodeContextProvider


def get_source_code(file_path: Path) -> str:
    with open(file_path, "r") as file:
        return file.read()


def main():
    file_path = Path("examples/example1/main.py")
    output_file_path = Path("examples/example1/rewritten/main.py")

    # Initialize context providers
    source_code_context_provider = SourceCodeContextProvider("python")

    # Register context providers
    code_rewrite_agent.register_context_provider("source_code", source_code_context_provider)

    source_code = get_source_code(file_path)
    source_code_context_provider.source_code = source_code

    # Run the agent
    response = code_rewrite_agent.run(
        CodeRewriteInputSchema(user_message="Please rewrite the code to use FastAPI instead of Flask.")
    )
    rewritten_code = response.rewritten_code

    output_file_path.parent.mkdir(parents=True, exist_ok=True)
    output_file_path.write_text(rewritten_code)
    print(f"Rewritten code saved to {output_file_path}")


if __name__ == "__main__":
    main()
