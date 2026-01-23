import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class UIClient:
    """
    Class implementing UI client functionality. It initializes the webdriver.

    Args:
        url (str): URL that tests will be executed against
        logger: Logger object
    """
    def __init__(self, url, logger):
        self.url = url
        self.logger = logger
        self._options = None
        self._driver = None
        mobile_device = os.getenv("MOBILE_DEVICE", "Pixel 7")
        self.mobile_emulation = {
            "deviceName": mobile_device
        }

    @property
    def driver(self):
        return self._get_webdriver()

    def _get_options(self):
        """Set chromedriver options

        Returns: 
            self._options: The Chromedriver options object
        """
        if self._options:
            return self._options

        _options = webdriver.ChromeOptions()

        if os.environ.get("USE_HEADLESS") == "0":
            self.logger.info("Chrome will not be in headless mode")
        else:
            self.logger.info("Chrome will be in headless mode")
            _options.add_argument("--headless")

        _options.add_argument("--start-maximized")
        _options.add_experimental_option("mobileEmulation", self.mobile_emulation)
        self._options = _options

        return self._options
    
    def _get_webdriver(self):
        """Get the webdriver based on options

        Returns: 
            self._driver: The driver object
        """
        if self._driver:
            return self._driver

        self._driver = webdriver.Chrome(options=self._get_options())
        return self._driver