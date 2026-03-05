# Playwright Test Automation Framework (Python)

Test automation framework built with Python, Playwright, and Pytest.

This project demonstrates a structured approach to UI test automation using the Page Object Model (POM) pattern, reusable fixtures, and environment configuration. The framework reflects practices commonly used in real-world QA automation projects.

The repository serves as a showcase of practical automation engineering concepts, including maintainable test architecture, separation of test logic and page interactions, and CI-ready test execution.

---

## Tech Stack

- Python
- Playwright
- Pytest
- Page Object Model (POM)
- python-dotenv
- GitHub Actions (CI workflow)

---

## Project Structure

Explore the project structure directly in the repository:

- [`tests`](https://github.com/MaxPash/automation_exercise/tree/main/tests) – UI test scenarios
- [`framework/pages`](https://github.com/MaxPash/automation_exercise/tree/main/framework/pages) – Page Object Model classes
- [`framework/config`](https://github.com/MaxPash/automation_exercise/tree/main/framework/config) – environment configuration
- [`framework/utils`](https://github.com/MaxPash/automation_exercise/tree/main/framework/utils) – helper utilities
- [`conftest.py`](https://github.com/MaxPash/automation_exercise/blob/main/conftest.py) – shared Pytest fixtures
- [`pytest.ini`](https://github.com/MaxPash/automation_exercise/blob/main/pytest.ini) – Pytest configuration
- [`.github/workflows`](https://github.com/MaxPash/automation_exercise/tree/main/.github/workflows) – CI pipeline configuration

This structure separates **test logic, page interactions, configuration, and utilities**, helping keep the framework maintainable and scalable.

---

## Key Features

- UI test automation using Playwright
- Page Object Model architecture
- Reusable Pytest fixtures
- Environment configuration support
- CI-ready project structure
- Clear separation between test logic and page objects

---

## Run Tests via GitHub Actions

The project includes a configured **GitHub Actions workflow** that automatically installs dependencies and executes the test suite.

You can view the workflow configuration here:

https://github.com/MaxPash/automation_exercise/tree/main/.github/workflows

To see real test executions:

1. Open the **Actions** tab in the repository.
2. Select the workflow run.
3. Review logs for dependency installation and test execution.

This demonstrates how the automation framework can be executed in a **CI environment**, ensuring that tests run automatically on each workflow trigger.