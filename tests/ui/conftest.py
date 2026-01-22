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
    """Handles exception, used for screenshot. Pytest builtin function"""
    driver = node.funcargs.get("driver", None)
    logger = node.funcargs.get("logger", None)
    if not driver or not logger:
        return
    
    take_screenshot(driver, logger)

@pytest.fixture(scope="class")
def accept_cookies_banner_if_present(driver, logger):
    """
    Accepts the cookies banner if it is present on the page.
    """
    cookies_banner = wait_for(
        driver,logger, waitBy.xpath,Locators.cookies_banners["cookieConsentBanner"],conditions.presence
    )

    if cookies_banner:
        logger.info("Cookies banner is present. Accepting cookies.")
        click_element(
            driver, logger, waitBy.xpath, Locators.cookies_banners["acceptCookiesButton"], conditions.clickable
        )
    else:
        logger.info("Cookies banner is not present. No action needed.")

    