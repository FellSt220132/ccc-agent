
import subprocess
import sys
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
SOLUTION_DIR = BASE_DIR / "solutions"

TEST_CASES = [
    {
        "name": "Example case",
        "input": "5\n3 8 -2 10 4\n",
        "expected": "10",
    },
    {
        "name": "Single number",
        "input": "1\n42\n",
        "expected": "42",
    },
    {
        "name": "All negative numbers",
        "input": "4\n-8 -3 -15 -1\n",
        "expected": "-1",
    },
    {
        "name": "Duplicate maximum",
        "input": "5\n7 12 3 12 4\n",
        "expected": "12",
    },
]


def test_solution(solution_file: Path) -> dict:
    result_data = {
        "file": solution_file.name,
        "passed": 0,
        "total": len(TEST_CASES),
        "success": False,
    }

    if not solution_file.exists():
        print(f"\nMissing file: {solution_file.name}")
        return result_data

    print(f"\nTesting {solution_file.name}")

    for test in TEST_CASES:
        try:
            result = subprocess.run(
                [sys.executable, str(solution_file)],
                input=test["input"],
                capture_output=True,
                text=True,
                timeout=2,
                check=False,
            )

            if result.returncode == 0 and (
                result.stdout.strip() == test["expected"]
            ):
                print(f"  PASS: {test['name']}")
                result_data["passed"] += 1
            else:
                print(f"  FAIL: {test['name']}")

        except subprocess.TimeoutExpired:
            print(f"  FAIL: {test['name']} (timeout)")

    result_data["success"] = (
        result_data["passed"] == result_data["total"]
    )

    print(
        f"Result: {result_data['passed']}/"
        f"{result_data['total']} tests passed"
    )

    return result_data


def main():
    results = []

    for model in ("chatgpt", "claude"):
        solution = SOLUTION_DIR / f"{model}_solution.py"
        results.append(test_solution(solution))

    return results


if __name__ == "__main__":
    main()
