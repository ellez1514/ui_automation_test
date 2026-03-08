import inspect
import pathlib
from retry import retry

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

base_dir = pathlib.Path(__file__).resolve().parent.parent

class waitBy:
    """Maps selenium 'By' types to simple names
    NOTE: Only including those used in the project
    """
    xpath = By.XPATH

class conditions:
    """
    Maps selenium 'expected_conditions' to simple names
    NOTE: Only including those used in the project
    """
    clickable = EC.element_to_be_clickable
    presence = EC.presence_of_element_located
    visibility = EC.visibility_of_element_located
    visibility_all = EC.presence_of_all_elements_located
    invisibility = EC.invisibility_of_element_located

# NOTE: This function could be moved to general "utils" file
# Its only used in this file so opted to keep here
def get_caller_info():
    """Get caller function for logging purposes

    Returns:
        caller_info(str): Caller filename and function name
    """
    caller = inspect.stack()[1]
    caller_filename = pathlib.Path(caller.filename).name
    caller_info = f"[{caller_filename}:{caller.function}:{caller.lineno}]"
    return caller_info


def wait_for(driver, logger, by, locator, expected_condition, timeout=10, poll_frequency=0.5):
    """Wait for an element that satisfies the expected condition

    Args:
        driver: Selenium driver object
        logger: Logger
        by: Selenium By type
        locator(str): Locator being searched for
        expected_condition: Condition to satisfy, e.g. visibility or presence
        timeout(int): The maximum time to wait for the condition to be met
        poll_frequency(float): Poll frequency to check for the condition to be met
    
    Returns:
        element: The element if found, None otherwise

    Raises:
        exception: If there is an error while waiting for the element.
    """
    caller_info = get_caller_info()
    logger.debug(
        "Caller info: %s, by: %s, element: %s, expected condition: %s, timeout %s, poll_frequency: %s",
        caller_info,
        by,
        locator,
        expected_condition,
        timeout,
        poll_frequency,
    )
    try:
        element = WebDriverWait(driver, timeout, poll_frequency).until(expected_condition((by, locator)))
        return element
    except Exception as e:
        logger.debug("'Wait for element' error: %s:%s", type(e), e)
        return None
    

def click_element(driver, logger, by, locator, conditions=conditions.presence, timeout=10):
    """
    Waits for an element with expected condition to appear on the page and clicks it.

    Args:
        driver: Selenium driver object
        logger: Logger.
        by:  Selenium By type
        locator(str): Locator used to find the element to be clicked.
        conditions: Condition to satisfy, e.g. visibility or presence
        timeout(int): The maximum time to wait for the condition to be met

    Raises:
        AssertionError: If the element cannot be found on the page.
        exception: If there is an error while clicking the element.
    """
    caller_function = get_caller_info()
    logger.debug("Click element called by %s", caller_function)
   
    element = wait_for(driver, logger, by, locator, conditions, timeout=timeout)
    assert element, f"Cannot find element with this locator: {locator}"

    try:
        element.click()
    except Exception as e:
        logger.error("Click error %s:%s", type(e), e)
        raise

def input_text(driver, logger, by, element, value, timeout=10):
    """Finds a input element using the specified locator and
    fills it with the given value.

    Args:
        driver: Selenium driver object
        by: Selenium By type
        element(str): Locator used to find the element.
        value(str): The text to enter into the input field.
    """
    ele = wait_for(driver, logger, by, element, conditions.presence, timeout)
    assert ele, f"Cannot find element to input text: {element}"
    ele.send_keys(value)

@retry(AssertionError, tries=6, delay=0.5)
def check_all_images_loaded(driver, logger, expected_count):
    """Check if all images on the page have been loaded. Retries on failure.

    Args:
        driver: Selenium driver object
        Logger: Logger object
        expected_count(int): The expected number of images to be loaded.

    """
    # NOTE: Had to look this command up, as it was not straightforward
    loaded_images = driver.execute_script(
        """
        const imgs = Array.from(document.querySelectorAll("img"));
        return imgs.filter(img => img.complete && img.naturalWidth > 0).length;
        """
    )

    logger.info(f"Number of images loaded: {loaded_images}")
    assert loaded_images == expected_count, (
        f"Expected {expected_count} images to be loaded, but found {loaded_images}"
    )


def take_screenshot(driver, logger, name=""):
    """Creates a screenshot directory (if it doesn't exist) and takes screenshot from driver, with preset name.
    If name is not provided, it uses caller info to create a name.

    Args:
        driver: Selenium driver object
        logger: Logger object.
        name(str, optional): The name to use for the function.

    """
    # Create screenshots directory if it doesn't exist
    screenshots_dir = base_dir / "screenshots"
    screenshots_dir.mkdir(exist_ok=True)
    
    filename = f"{name}.png"

    if not name:
        caller = inspect.stack()[1]
        filename = f"{pathlib.Path(caller.filename).stem}_{caller.function}_{caller.lineno}.png"

    screenshot_path = screenshots_dir / filename

    logger.info(f"Taking screenshot and will save in: '{filename}")
    driver.save_screenshot(screenshot_path)