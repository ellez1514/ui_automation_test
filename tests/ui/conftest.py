import pytest

from data import Locators
from helpers.ui_utils import (
    click_element,
    conditions,
    wait_for,
    waitBy,
    take_screenshot,
)

def pytest_exception_interact(node, call, report):
    """Pytest builtin function. In case of exception, takes screenshot."""
    driver = node.funcargs.get("driver", None)
    logger = node.funcargs.get("logger", None)
    if not driver or not logger:
        return
    
    logger.error("Test failed. Taking screenshot")
    take_screenshot(driver, logger)

@pytest.fixture(scope="class")
def accept_cookies_banner_if_present(driver, logger):
    """
    Accepts the cookies banner if it is present on the page.
    """
    cookies_banner = wait_for(
        driver, logger, waitBy.xpath, Locators.cookies_banners["cookieConsentBanner"], conditions.clickable
    )

    if cookies_banner:
        logger.info("Cookies banner is present. Accepting cookies.")
        click_element(
            driver, logger, waitBy.xpath, Locators.cookies_banners["acceptCookiesButton"], conditions.clickable
        )
        
        # Verify that banner is invisible to avoid 'ElementClickInterceptedException'
        verify_invisibility = wait_for(
            driver, logger, waitBy.xpath, Locators.cookies_banners["cookieConsentBanner"], conditions.invisibility
        )
        assert verify_invisibility, "Expected cookies banner to be invisible"

    else:
        logger.info("Cookies banner is not present. No action needed.")

    