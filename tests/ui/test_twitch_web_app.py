import pytest
from data import Locators
from helpers.ui_utils import (
    check_all_images_loaded,
    click_element, 
    conditions, 
    input_text, 
    take_screenshot, 
    wait_for,
    waitBy
)

__author__ = "Eleni Kamara"
__email__ = "elenidespinakamara@gmail.com"


@pytest.mark.ui
@pytest.mark.usefixtures("select_keep_using_web_button", "accept_cookies_banner_if_present")
class TestTwitchWebApp:
    """Test suite for Twitch web application UI tests
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

        # Click on the streamer from the search results
        click_element(
            driver,
            logger,
            waitBy.xpath,
            Locators.search_results["streamerImageItem"].format(title=streamer_name),
            conditions.clickable
        )

        # Wait for the page to load (checks for streamer name and that all images are loaded)
        streamer_name_title = wait_for(
            driver,
            logger,
            waitBy.xpath, 
            Locators.streamer_page["streamer_name_title"].format(title=streamer_name),
            conditions.visibility
        )
        assert streamer_name_title, "Streamer name title is not found"
        love_button = wait_for(driver, logger, waitBy.xpath, Locators.buttons["love_button"], conditions.visibility)
        assert love_button, "Love button is not found"
        
        # NOTE: In a real test, the expected count should be  based on expected test data to avoid flakiness
        check_all_images_loaded(driver, logger, expected_count=17)

        take_screenshot(driver, logger)


    