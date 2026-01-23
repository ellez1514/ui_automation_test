import logging
import os
import pytest

from clients.ui_client import UIClient


logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)-15s - %(levelname)s - [%(filename)-.20s | L%(lineno)d] - %(message)s"
)
logging.getLogger("selenium").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)


@pytest.fixture(scope="session")
def logger():
    """Logging fixture to be used across the tests"""
    return logging.getLogger(__name__)

@pytest.fixture(scope="module")
def uiclient(logger):
    root_url = os.environ.get("URL", "https://www.twitch.tv/")
    uiclient = UIClient(root_url, logger)
    logger.debug("Will perform a driver get at %s", uiclient.url)

    uiclient.driver.get(uiclient.url)

    yield uiclient

    try:
        uiclient.driver.close()
        uiclient.driver.quit()
    except Exception as e:
        logger.error("Closing or quitting driver failed: %s:%s", type(e), e)


@pytest.fixture(scope="class")
def driver(uiclient):
    return uiclient.driver