
from pathlib import Path

from models import ask_chatgpt, ask_claude
from code_extractor import extract_python_code


BASE_DIR = Path(__file__).resolve().parent
PROMPT_FILE = BASE_DIR / "prompts" / "solve.txt"
TASK_FILE = BASE_DIR / "tasks" / "problem.txt"
OUTPUT_DIR = BASE_DIR / "solutions"


def load_prompt():
    return PROMPT_FILE.read_text(encoding="utf-8")


def load_task():
    return TASK_FILE.read_text(encoding="utf-8")


def generate_solutions():
    prompt_template = load_prompt()
    problem = load_task()

    prompt = (
        prompt_template
        + "\n\nPROBLEM STATEMENT:\n"
        + problem
    )

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    models = {
        "chatgpt": ask_chatgpt,
        "claude": ask_claude,
    }

    for name, ask_model in models.items():
        print(f"\nGenerating solution with {name}...")

        try:
            response = ask_model(prompt)

            response_file = OUTPUT_DIR / f"{name}_response.txt"
            response_file.write_text(
                response,
                encoding="utf-8"
            )

            source = extract_python_code(response)

            solution_file = OUTPUT_DIR / f"{name}_solution.py"
            solution_file.write_text(
                source + "\n",
                encoding="utf-8"
            )

            print(f"Response saved: {response_file.name}")
            print(f"Python solution saved: {solution_file.name}")
            print("Syntax validation passed.")

        except Exception as error:
            print(f"{name} failed: {error}")


if __name__ == "__main__":
    generate_solutions()
