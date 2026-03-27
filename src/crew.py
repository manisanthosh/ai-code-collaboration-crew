from crewai import Crew

from src.agents.backend_engineer import get_backend_engineer
from src.agents.reviewer import get_reviewer
from src.agents.tester import get_tester

from src.tasks.coding_task import create_coding_task
from src.tasks.review_task import create_review_task
from src.tasks.testing_task import create_testing_task

from src.agents.github_agent import get_github_agent
from src.tasks.github_task import create_github_task


def build_crew(feature_request: str):
    backend = get_backend_engineer()
    reviewer = get_reviewer()
    tester = get_tester()

    coding_task = create_coding_task(backend, feature_request)

    # review_task = create_review_task(reviewer, "{coding_task_output}")
    # testing_task = create_testing_task(tester, "{review_task_output}")

    github_agent = get_github_agent()

    github_task = create_github_task(
        github_agent,
    )

    return Crew(
        agents=[backend, github_agent],
        tasks=[coding_task, github_task],
        verbose=True,
        memory=False,
    )