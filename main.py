from solver import generate_solutions
from selector import select_best_solution


def main():
    print("=" * 40)
    print("CCC SOLUTION AGENT")
    print("=" * 40)

    print("\n[1/2] Generating solutions...")
    generate_solutions()

    print("\n[2/2] Testing and selecting the best solution...")
    select_best_solution()

    print("\nPipeline finished.")


if __name__ == "__main__":
    main()
