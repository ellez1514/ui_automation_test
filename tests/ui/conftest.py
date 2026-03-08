import pytest

from helpers.ui_utils import (
    take_screenshot,
)
from pages import StreamerPage, SearchResultsPage, BasePage

def pytest_exception_interact(node, call, report):
    """Pytest builtin function. In case of exception, takes screenshot."""
    driver = None
    logger = None

    if hasattr(node, "funcargs"):
        driver = node.funcargs.get("driver")
        logger = node.funcargs.get("logger", None)

    if driver and logger:
        logger.error("Test failed. Taking screenshot")
        take_screenshot(driver, logger)

@pytest.fixture(scope="class")
def streamer_page(driver, logger):
    """Returns a ready-to-use LoginPage object"""
    return StreamerPage(driver, logger)

@pytest.fixture(scope="class")
def search_results_page(driver, logger):
    """Returns a ready-to-use LoginPage object"""
    return SearchResultsPage(driver, logger)

@pytest.fixture(scope="class")
def base_page(driver, logger):
    """Returns a ready-to-use LoginPage object"""
    return BasePage(driver, logger)

@pytest.fixture(scope="class")
def select_keep_using_web_button(base_page):
    """
    Select "keep using web" button
    """
    base_page.select_keep_using_web_button()

@pytest.fixture(scope="class")
def accept_cookies_banner_if_present(base_page):
    """
    Accepts the cookies banner if it is present on the page.
    """
    base_page.accept_cookies_banner_if_present()