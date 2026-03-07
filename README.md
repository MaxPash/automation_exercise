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


## Development Roadmap

This framework is continuously evolving to demonstrate additional automation engineering practices commonly used in production QA environments.

The following improvements are planned as part of the framework development:

### 1. Test Data Factory
Introduce a centralized test data generation layer to provide reusable and maintainable test payloads. This helps keep test data consistent across API, UI, and integration tests.

---

### 2. API Test Suite
Add a dedicated API testing layer covering core backend functionality.

Example structure:

tests/
    api/
    ui/
    integration/

The API test suite will include:

- positive API scenarios
- negative validation tests
- authentication flows
- user lifecycle tests (create / login / delete)

This demonstrates backend testing capabilities in addition to UI automation.

---

### 3. API Schema Validation
Validate API responses using typed schema models to ensure response structure and data types match the expected contract.

Planned implementation:

- `pydantic` models for response validation
- validation of required fields and data types
- improved API contract verification

Example structure:

schemas/
    user_schema.py

This approach strengthens API tests by verifying not only response status but also response structure.

---

### 4. Allure Reporting
Integrate **Allure reporting** to provide detailed and readable test execution reports.

Planned report features:

- step-by-step test execution
- screenshots on failure
- API request / response attachments
- execution timeline

This improves test observability and debugging in both local and CI environments.

---

### 5. Test Markers
Introduce Pytest markers for better test organization and selective execution.

Planned markers:

- `api`
- `ui`
- `integration`
- `smoke`
- `regression`

Example usage:

pytest -m smoke  
pytest -m api  

This allows flexible test execution strategies depending on testing scope.