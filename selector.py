
from pathlib import Path

from tester import main as run_tests


BASE_DIR = Path(__file__).resolve().parent
SOLUTION_DIR = BASE_DIR / "solutions"


def select_best_solution():
    results = run_tests()

    # Prefer the highest test score.
    # ChatGPT wins ties because it appears first.
    best = max(
        results,
        key=lambda result: result["passed"],
        default=None,
    )

    if best is None or best["passed"] == 0:
        print("\nNo usable solution was found.")
        return

    source = SOLUTION_DIR / best["file"]
    destination = SOLUTION_DIR / "selected_solution.py"

    destination.write_text(
        source.read_text(encoding="utf-8"),
        encoding="utf-8",
    )

    print(f"\nSelected solution: {best['file']}")
    print(f"Saved as: {destination.name}")
    print(
        f"Tests passed: {best['passed']}/{best['total']}"
    )


if __name__ == "__main__":
    select_best_solution()
