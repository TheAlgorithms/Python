
def analyze_issue(issue_description: str) -> str:
    """Create a concise investigation plan for the supplied issue."""
    return f"""
Analyze this software issue:

{issue_description}

Identify:
1. The suspected bug.
2. What source code needs investigation.
3. What evidence would confirm the bug.
4. What tests should verify a correction.

Do not invent source code or propose a complete replacement
before inspecting the existing implementation.
"""
