from crewai import Task

def create_review_task(agent, code):
    return Task(
        description=f"""
        ### REVIEW ###
        Review and improve the following code:

        {code}

        Provide:
        - Bug fixes
        - Performance improvements
        - Cleaned version
        """,
        agent=agent,
        expected_output="Improved code with explanations",
    )