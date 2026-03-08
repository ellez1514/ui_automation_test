from selenium.webdriver.common.by import By
from typing import Tuple
from helpers.ui_utils import click_element, conditions, input_text
from .base_page import BasePage

class SearchResultsPage(BasePage):
    """Page object for the search results page.
    Contains methods to interact with the search results page.
    """

    SEARCH_FIELD_INPUT =  (By.XPATH, "//input[@placeholder='Search']")
    SEARCH_RESULTS_ITEMS_WITH_IMAGES = (By.XPATH, "//img[@class='tw-image' and @alt='{title}']")

    def __init__(self, driver, logger):
        super().__init__(driver, logger)

    def get_search_result_locator(self, title: str) -> Tuple[By, str]:
        """
        Generates the dynamic locator for a search result item.
        """
        return (By.XPATH, f"//img[@class='tw-image' and @alt='{title}']")

    def input_in_search_fields(self, streamer_name: str) -> None:
        """ Input streamer name in search field"""
        input_text(
            self.driver,
            self.logger,
            self.SEARCH_FIELD_INPUT,
            streamer_name
        )

    def click_streamer_on_search_results(self, streamer_name: str) -> None:
        """
        Click on the streamer on search results
        """
        locator = self.get_search_result_locator(streamer_name)
        click_element(
            self.driver,
            self.logger,
            locator,
            conditions.clickable
        )
