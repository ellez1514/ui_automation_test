from selenium.webdriver.common.by import By
from helpers.ui_utils import click_element, conditions, wait_for


class BasePage:
    """Base page class that other page classes can inherit from. 
    Contains common methods and locators.
    """

    BROWSE_TAB = (By.XPATH, "//a[@href='/directory']")

    COOKIES_CONSENT_BANNER =  (By.XPATH, "//div[@data-a-target='consent-banner']")
    ACCEPT_COOKIES_BUTTON = (By.XPATH, "//button[@data-a-target='consent-banner-accept']")

    CLOSE_DIALOG_BUTTON = (By.XPATH, "//button[@aria-label='Activate to close dialog']")
    KEEP_USING_WEB_BUTTON = (By.XPATH, "//p[text()='Keep using web']")

    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger

    def click_browse_tab(self):
        """
        Click on browse tab
        """
        click_element(
            self.driver,
            self.logger,
            self.BROWSE_TAB,
            conditions.clickable
        )
    
    def accept_cookies_banner_if_present(self):
        """
        Accepts the cookies banner if it is present on the page.
        """
        cookies_banner = wait_for(
            self.driver,
            self.logger,
            self.COOKIES_CONSENT_BANNER,
            conditions.clickable
        )

        if cookies_banner:
            self.logger.info("Cookies banner is present. Accepting cookies.")
            click_element(
                self.driver, 
                self.logger,
                self.ACCEPT_COOKIES_BUTTON, 
                conditions.clickable
            )
            
            # Verify that banner is invisible to avoid 'ElementClickInterceptedException'
            verify_invisibility = wait_for(
                self.driver,
                self.logger,
                self.COOKIES_CONSENT_BANNER,
                conditions.invisibility
            )
            assert verify_invisibility, "Expected cookies banner to be invisible"

        else:
            self.logger.info("Cookies banner is not present. No action needed.")

    
    def select_keep_using_web_button(self):
        """
        Select the 'Keep using web' button if the dialog is present.
        """
        close_dialog_button = wait_for(
            self.driver, self.logger, self.CLOSE_DIALOG_BUTTON, conditions.clickable
        )

        if close_dialog_button:
            self.logger.info("Its required to select between using app or web browser. Select web browser")
            click_element(
                self.driver, self.logger, self.KEEP_USING_WEB_BUTTON, conditions.clickable
            )
        else:
            self.logger.info("Dialog does not exist. No action required.")