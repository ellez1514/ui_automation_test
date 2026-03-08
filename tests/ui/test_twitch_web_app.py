import pytest
from helpers.ui_utils import (
    check_all_images_loaded,
    take_screenshot, 
)

__author__ = "Eleni Kamara"
__email__ = "elenidespinakamara@gmail.com"


@pytest.mark.ui
@pytest.mark.usefixtures("select_keep_using_web_button", "accept_cookies_banner_if_present")
class TestTwitchWebApp:
    """Test suite for Twitch web application UI tests
    """

    def test_select_streamer(self, logger, driver, base_page, streamer_page, search_results_page):
        """
        Selects a streamer by searching for their name in the browse tab.
        """
        streamer_name = "StarCraft II"

        # Click on the browse tab and search for the streamer
        base_page.click_browse_tab()
        search_results_page.input_in_search_fields(streamer_name)
        # Click on the streamer from the search results
        search_results_page.click_streamer_on_search_results(streamer_name)
        
        # Wait for the page to load (checks for streamer name and that all images are loaded)
        assert streamer_page.is_streamer_title_displayed(streamer_name)
        assert streamer_page.is_love_button_displayed, "Love button is not found"
        
        # NOTE: In a real test, the expected count should be  based on expected test data to avoid flakiness
        check_all_images_loaded(driver, logger, expected_count=17)

        take_screenshot(driver, logger)


    