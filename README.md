# TEST SUITE FOR TWITCH WEB APP (USING MOBILE EMULATOR)
This repo contains automated test that tests the search of streamer in twitch

#### TEST CASE

| Test Case              | Scenario   | Expected Outcome                             |
|------------------------|------------|----------------------------------------------|
| `test_select_streamer` | Happy Path | Select the streamer and capture a screenshot |


#### REPO STRUCTURE DESCRIPTION

| Folder / Subfolder | File                        | Description                                       |
|------------------- |----------------------------|----------------------------------------------------|
| `clients/`         | `__init__.py`              | Marks the clients dir as a Python package          |
| `clients/`         | `ui_client.py`             | Client that contains Selenium WebDriver wrapper    |
| `helpers/`         | `ui_utils.py`              | Helper functions used for UI automation            |
| `pages/`           | `__init__.py`              | Marks the pages dir as a Python package            |
| `pages/`           | `base_page.py`             | Base page class for Page Object Model              |
| `pages/`           | `search_results_page.py`   | Page object for search results                     |
| `pages/`           | `streamer_page.py`         | Page object for streamer page                      |
| `screenshots/`*    | -                          | Stores screenshots taken during test run           |
| `tests/ui/`        | `conftest.py`              | Test configuration and fixtures for UI tests       |
| `tests/ui/`        | `test_twitch_web_app.py`   | UI test cases for the Twitch web app               |
| `/`                | `conftest.py`              | General config and fixtures for the whole project  |
| `/`                | `pytest.ini`               | Pytest configuration file                          |
| `/`                | `requirements.txt`         | Python package dependencies                        |
| `/`                | `README.md`                | Project documentation                              |
| `/`                | `ui_automation.gif`        | GIF of test execution                              |

* Screenshots folder is created at test execution.

#### HOW TO EXECUTE TEST:

1. Install requirements:
```sh
pip install -r requirements.txt
```

2. (Optional) Export following variables:
```sh
export USE_HEADLESS=1
export URL=https://www.twitch.tv
export MOBILE_DEVICE="Pixel 7"
```

If those parameters are not exported, then default values will be used 
which are the same values as seen above.

MOBILE DEVICE has only been tested with "Pixel 7"

2. Execute test:
```sh
pytest -rA -s -v tests/ui/test_twitch_web_app.py
or
cd tests/ui/
pytest -rA -s -v -m "ui"

```

#### TEST EXECUTION
![Test Execution](ui_test_execution.gif)