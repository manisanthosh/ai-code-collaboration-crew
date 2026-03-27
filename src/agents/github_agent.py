from crewai import Agent
from src.config import get_llm


def get_github_agent():
    return Agent(
        role="GitHub Automation Engineer",
        goal="Create pull requests with generated code",
        backstory="Expert in CI/CD and Git workflows",
        llm=get_llm(),
        verbose=True,
    )