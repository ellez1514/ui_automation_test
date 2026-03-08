from selenium.webdriver.common.by import By
from helpers.ui_utils import conditions, wait_for
from .base_page import BasePage

class StreamerPage(BasePage):

    STREAMER_NAME_TITLE = (By.XPATH, "//h1[text()='{title}']")
    LOVE_BUTTON = (By.XPATH, "//button[@data-a-target='game-directory-follow-button']")

    def __init__(self, driver, logger):
        super().__init__(driver, logger)

    def get_streamer_title_locator(self, title) :
        """
        Generates the dynamic locator for the streamer title.
        """
        return (By.XPATH, f"//h1[text()='{title}']")

    def is_streamer_title_displayed(self, title):
        """
        Check that streamer title is displayed and returns True/False.
        """
        streamer_title_locator = self.get_streamer_title_locator(title)
        streamer_name_title_exists = wait_for(
            self.driver,
            self.logger,
            streamer_title_locator,
            conditions.visibility
        )
        return streamer_name_title_exists
    
    def is_love_button_displayed(self, title):
        """
        Check that love button is displayed and returns True/False.
        """
        love_button_exists = wait_for(
            self.driver,
            self.logger,
            self.LOVE_BUTTON,
            conditions.visibility
        )
        return love_button_exists