# Locators for Twitch web application UI elements
# NOTE: Opted to use one file for all locators as they are few and related to the same app. 
# For larger projects, this would be splitted by page.

buttons = {
    "closeButton": "//span[@title='Remove Widget']",
    "love_button": "//button[@data-a-target='game-directory-follow-button']"
}

navigation_tabs = {
    "browse": "//a[@href='/directory']",
}

cookies_banners = {
    "cookieConsentBanner": "//div[@data-a-target='consent-banner']",
    "acceptCookiesButton": "//button[@data-a-target='consent-banner-accept']",
}

input_fields = {
    "searchInputField": "//input[@placeholder='Search']",
}

search_results = {
    "resultItem": "//p[@title='{title}']",
    "streamerImageItem": "//img[@class='tw-image' and @alt='{title}']"
}

streamer_page = {
    "streamer_name_title": "//h1[text()='{title}']",
    "channels_header": "//h2[text()='Channels']",
    "categories_header": "//h2[text()='Categories']",
    "images": "//img[@class='tw-image']"
}