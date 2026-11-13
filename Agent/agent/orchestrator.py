
import ollama

from config import MODEL_NAME, MAX_TOOL_CALLS, ISSUE_URL
from agent import tools
from agent.issue_analyzer import analyze_issue

TOOL_DEFINITIONS = [
    {
        "type": "function",
        "function": {
            "name": "list_files",
            "description": "List files in a directory of the target repository.",
            "parameters": {
                "type": "object",
                "properties": {
                    "directory": {"type": "string"}
                },
                "required": ["directory"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "read_file",
            "description": "Read a file from the target repository, especially CONTRIBUTING.md.",
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {"type": "string"}
                },
                "required": ["path"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "search_code",
            "description": "Search Python files for a piece of text.",
            "parameters": {
                "type": "object",
                "properties": {
                    "term": {"type": "string"}
                },
                "required": ["term"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "run_tests",
            "description": "Run approved checks: doctest or ruff.",
            "parameters": {
                "type": "object",
                "properties": {
                    "command": {
                        "type": "string",
                        "enum": ["doctest", "ruff"]
                    }
                },
                "required": ["command"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "propose_edit",
            "description": "Propose a code edit. The user must approve before it is applied.",
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {"type": "string"},
                    "old_text": {"type": "string"},
                    "new_text": {"type": "string"}
                },
                "required": ["path", "old_text", "new_text"]
            }
        }
    }
]


AVAILABLE_TOOLS = {
    "list_files": tools.list_files,
    "read_file": tools.read_file,
    "search_code": tools.search_code,
    "run_tests": tools.run_tests,
    "propose_edit": tools.propose_edit,
}


def run_agent(issue_description: str) -> None:
    """Run the AI agent's tool-selection and reasoning loop."""

    messages = [
        {
            "role": "system",
            
            "content": (
                "You are an autonomous Python repository contribution agent. "
                "You must investigate the issue using repository tools before "
                "recommending a solution. Follow these steps in order: "
                "1. Read CONTRIBUTING.md. "
                "2. Read the source file relevant to the issue. "
                "3. Search for the specific problematic code. "
                "4. Explain the exact cause of the bug using evidence from the code. "
                "5. Identify the smallest appropriate correction. "
                "6. Propose the correction using propose_edit. "
                "7. If the user approves, run doctest and ruff. "
                "8. Summarize the changes and test results. "
                "Do not skip investigation steps. "
                "Do not invent a replacement algorithm when a small correction "
                "to the existing implementation is sufficient. "
                "Preserve existing function signatures and behavior. "
                "Never claim tests passed unless you ran them. "
                "You must follow CONTRIBUTING.md. "
                "Do not commit, push, or create pull requests."
            )
        },
        {
            "role": "user",
            "content": (
                f"Repository issue: {ISSUE_URL}\n\n"
                f"{analyze_issue(issue_description)}"
            )
        }
    ]

    for step in range(MAX_TOOL_CALLS):
        print(f"\n--- Agent reasoning step {step + 1} ---")

        response = ollama.chat(
            model=MODEL_NAME,
            messages=messages,
            tools=TOOL_DEFINITIONS,
            think=True,
        )

        assistant_message = response.message
        messages.append(assistant_message)

        if not assistant_message.tool_calls:
            print("\n--- Agent final response ---")
            print(assistant_message.content)

            print("\nThe agent has finished its investigation.")
            print("Running required verification checks...")

            print("\n--- Doctests ---")
            print(tools.run_tests("doctest"))

            print("\n--- Ruff ---")
            print(tools.run_tests("ruff"))

            return

        for tool_call in assistant_message.tool_calls:
            name = tool_call.function.name
            arguments = tool_call.function.arguments

            print(f"\nAgent selected tool: {name}")
            print(f"Arguments: {arguments}")

            function = AVAILABLE_TOOLS.get(name)

            if function is None:
                result = f"Error: Unknown tool {name}."
            else:
                try:
                    result = function(**arguments)
                except Exception as error:
                    result = f"Tool error: {error}"

            print(f"\nTool result:\n{result}")

            messages.append({
                "role": "tool",
                "name": name,
                "content": str(result)
            })

    print("\nAgent stopped because it reached the tool-call limit.")
