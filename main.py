import argparse
from src.crew import build_crew
from src.tools.github_tool import GitHubPRTool
import re

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--feature",
        type=str,
        required=True,
        help="Feature request for code generation",
    )

    args = parser.parse_args()

    crew = build_crew(args.feature)

    result = crew.kickoff()

    output_text = result.raw

    print("\n=== FINAL OUTPUT ===\n")
    print(output_text)

    code = extract_code(output_text)

    if "def " in code:
        pr_tool = GitHubPRTool()
        pr_url = pr_tool._run(file_content=code)

        print("\n🚀 PR Created:", pr_url)
    else:
        print("❌ Invalid code, skipping PR")


def extract_code(text: str) -> str:
    """Extract code block from markdown"""
    match = re.search(r"```python(.*?)```", text, re.DOTALL)
    if match:
        return match.group(1).strip()
    return text.strip()

if __name__ == "__main__":
    main()