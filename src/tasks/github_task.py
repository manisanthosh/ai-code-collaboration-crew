from crewai import Task

def create_github_task(agent):
    return Task(
        description="""
        Take the final reviewed Python code from previous steps.

        Output ONLY the raw Python code.
        Do NOT explain anything.
        Do NOT call any tools.
        """,
        agent=agent,
        expected_output="Pure Python code",
    )