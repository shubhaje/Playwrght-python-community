# Playwright Python Test Automation Framework

This project is a test automation framework using Playwright with Python and pytest, implementing the Page Object Model design pattern.

## Project Structure

```
Playwrght-opython-community/
|--requirements.txt        # Project dependencies
|--pages/                 # Page Object Model implementations
|    |--__init__.py
|    |--login_page.py     # Login page elements and actions
|--tests/                 # Test files
|    |--test_login.py     # Login test scenarios
|    |--pytest.ini        # Pytest configuration
|    |--conftest.py       # Test fixtures and configuration
```

## Setup

1. Install Python 3.8 or higher
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Install Playwright browsers:
```bash
playwright install
```

## Running Tests

To run all tests:
```bash
pytest
```

To run specific test file:
```bash
pytest tests/test_login.py
```

To run tests with HTML report:
```bash
pytest --html=report.html
```

## Test Scenarios

The framework includes the following test scenarios:
- Valid login with standard user
- Locked out user login attempt
- Problem user login
- Performance glitch user login
- Error user login
- Visual user login
- Invalid credentials login attempt

## Page Object Model

The framework uses Page Object Model to:
- Separate test code from page specific code
- Create reusable page methods
- Maintain element locators in one place

## CI/CD

This project includes GitHub Actions workflow for continuous integration. Tests are automatically run on:
- Push to main branch
- Pull request to main branch

