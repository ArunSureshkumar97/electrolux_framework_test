# SDET API Challenge Framework

Pytest-based API automation framework for testing:

`https://jsonplaceholder.typicode.com/posts`

## Features
- Clean project structure for maintainability
- Central API handler
- Reusable HTTP session / connection
- Request headers handled centrally
- Pydantic payload and response schema validation
- Test data stored separately
- Pytest fixtures via `conftest.py`
- Logging utility
- HTML reporting

## Project Structure

```text
sdet_api_challenge_framework/
├── config/
├── core/
├── handlers/
├── schemas/
├── testdata/
├── tests/
├── utils/
├── reports/
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run Tests

```bash
pytest
```

## HTML Report

After execution, open:

```text
reports/report.html
```

## Covered Scenarios
- Get all posts
- Get post by id
- Create a post
- Validate response schema
- Validate important response fields
- Negative test for invalid post id
- Delete a post
