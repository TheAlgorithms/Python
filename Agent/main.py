
from agent.orchestrator import run_agent


def main():
    print("=" * 60)
    print("THEALGORITHMS PYTHON CONTRIBUTION AGENT")
    print("=" * 60)

    print("\nTarget issue:")
    print("https://github.com/TheAlgorithms/Python/issues/15655")

    print("\nEnter the issue description.")
    print("Paste the description, then type END on a new line.")

    description_lines = []

    while True:
        line = input()

        if line.strip() == "END":
            break

        description_lines.append(line)

    issue_description = "\n".join(description_lines)

    if not issue_description.strip():
        print("No issue description provided.")
        return

    print("\nStarting agent...\n")
    run_agent(issue_description)


if __name__ == "__main__":
    main()
