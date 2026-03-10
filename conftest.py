import pytest
from config import config as conf
from handlers.api_handler import APIHandler


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="qa",
        help="Environment: qa or dev or staging or prod"
    )

    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser: chrome, firefox, safari"
    )

def pytest_configure(config):
    env = config.getoption("--env")

    env_urls = {
        "qa": "https://jsonplaceholder.typicode.com",
        "dev": "https://dev-jsonplaceholder.typicode.com",
        "staging": "https://staging-jsonplaceholder.typicode.com",
        "prod": "https://prod-jsonplaceholder.typicode.com",
    }

    conf.BASE_URL = env_urls[env]

    print(f"\nRunning with env={env}, BASE_URL={conf.BASE_URL}")