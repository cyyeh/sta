from pathlib import Path

import orjson

from src.agents.code_rewrite import code_rewrite_agent, CodeRewriteInputSchema, CodeRewriteOutputSchema
from src.context_providers import CodeContextProvider


def read_file(file_path: Path) -> str:
    with open(file_path, "r") as file:
        return file.read()


def main():
    source_file_base_path = Path("examples/example1")
    output_file_base_path = Path("examples/rewritten_example1")
    source_code_file_path = source_file_base_path / "main.py"
    test_code_file_path = source_file_base_path / "tests/test_main.py"
    dependencies_file_path = source_file_base_path / "requirements.txt"
    output_source_code_file_path = output_file_base_path / "main.py"
    output_test_code_file_path = output_file_base_path / "tests/test_main.py"
    output_dependencies_file_path = output_file_base_path / "requirements.txt"

    # Initialize context providers
    code_context_provider = CodeContextProvider("python")

    # Register context providers
    code_rewrite_agent.register_context_provider("code", code_context_provider)

    source_code = read_file(source_code_file_path)
    test_code = read_file(test_code_file_path)
    dependencies = read_file(dependencies_file_path)

    code_context_provider.source_code = source_code
    code_context_provider.test_code = test_code
    code_context_provider.dependencies = dependencies

    # Run the agent
    response: CodeRewriteOutputSchema = code_rewrite_agent.run(
        CodeRewriteInputSchema(user_message="Please rewrite the code to use FastAPI instead of Flask.")
    )
    rewritten_code = response.rewritten_code
    rewritten_test_code = response.rewritten_test_code
    rewritten_dependencies = response.rewritten_dependencies

    output_source_code_file_path.parent.mkdir(parents=True, exist_ok=True)
    output_source_code_file_path.write_text(rewritten_code)
    output_test_code_file_path.parent.mkdir(parents=True, exist_ok=True)
    output_test_code_file_path.write_text(rewritten_test_code)
    output_dependencies_file_path.parent.mkdir(parents=True, exist_ok=True)
    output_dependencies_file_path.write_text(rewritten_dependencies)
    print(f"Rewritten code saved to {output_source_code_file_path}")
    print(f"Rewritten test code saved to {output_test_code_file_path}")
    print(f"Rewritten dependencies saved to {output_dependencies_file_path}")


if __name__ == "__main__":
    main()
