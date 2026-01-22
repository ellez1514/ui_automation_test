from time import sleep
import pytest
from data import Locators
from helpers.ui_utils import (
    click_element, 
    conditions, 
    input_text, 
    scroll_to, 
    take_screenshot, 
    wait_for, 
    waitBy
)

__author__ = "Eleni Kamara"
__email__ = "elenidespinakamara@gmail.com"


@pytest.mark.ui
@pytest.mark.usefixtures("accept_cookies_banner_if_present")
class TestTwitchWebApp:
    """@brief Test suite for Twitch web application UI tests
    """

    def test_select_streamer(self, logger, driver):
        """
        Selects a streamer by searching for their name in the browse tab.
        """
        streamer_name = "StarCraft II"

        # Click on the browse tab and search for the streamer
        # NOTE: Original request mentions "click search icon", but that doesn't exist on Twitch UI
        click_element(driver, logger, waitBy.xpath, Locators.navigation_tabs["browse"], conditions.clickable)
        input_text(driver, logger, waitBy.xpath, Locators.input_fields["searchInputField"], streamer_name)
        
        # Scroll down 2 times 
        # NOTE: No reason to scroll since page is not scrollable, but keeping as per original request
        scroll_to(driver, x="0", y="50")
        scroll_to(driver, x="0", y="50")

        # Click on the streamer from the search results
        click_element(
            driver,
            logger,
            waitBy.xpath,
            Locators.search_results["resultItem"].format(title=streamer_name),
            conditions.clickable
        )

        # Wait for the page to load (NOTE: waiting for channels text to appear)
        #  and take a screenshot
        wait_for(driver, logger, waitBy.xpath, Locators.streamer_page["channels"], conditions.presence)
        take_screenshot(driver, logger)


    