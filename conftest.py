import logging
import os

import urllib
from clients.ui_client import UIClient
import pytest
import time


logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)
logging.getLogger("selenium").setLevel(logging.WARNING)
logging.getLogger("selenium").propagate = False
logging.getLogger("urllib3").setLevel(logging.WARNING)
logging.getLogger("urllib3").propagate = False


@pytest.fixture(scope="session")
def logger():
    """Logging fixture to allow across-the-board logging"""
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