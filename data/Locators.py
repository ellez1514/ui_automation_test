# Locators for web application elements
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
}

streamer_page = {
    "channels": "//h2[text()='Channels']",
    "video_images": "//img[@class='tw-image']"
}