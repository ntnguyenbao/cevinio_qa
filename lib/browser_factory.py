from selenium import webdriver
from pathlib import Path
from robot.api.deco import keyword

def __get_current_path():
    return str(Path(__file__).parent.absolute())


def __get_firefox(headless: str) -> webdriver:
    """This function establishes firefox browser."""
    firefox_options = webdriver.firefox.options.Options()
    if headless:
        firefox_options.add_argument('--headless')
        firefox_options.add_argument('--disable-gpu')
        firefox_options.add_argument('--debug')
    firefox_options.set_preference("dom.push.enabled", False)

    return webdriver.Firefox(firefox_options=firefox_options)


def __get_chrome(headless: str) -> webdriver:
    """This function establishes chrome browser."""
    chrome_options = webdriver.chrome.options.Options()
    if headless:
        chrome_options.add_argument('--headless')
        # open Browser in maximized mode
        chrome_options.add_argument('start-maximized')
        # disable info bars
        # chrome_options.add_argument('disable-infobars')
        # disable extensions
        chrome_options.add_argument('--disable-extensions')
        chrome_options.add_argument('--disable-gpu')  # For windows os only
        chrome_options.add_argument('--no-sandbox')  # bypass OS security model
        # overcome limited resource problems
        chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_experimental_option("prefs", {
        "profile.default_content_setting_values.notifications": 1
    })

    return webdriver.Chrome(chrome_options=chrome_options)

@keyword("Get Browser")
def get_browser(name: str, headless: bool=False):
    """This function is used for quick selection of browser."""
    switcher = {
        "firefox": __get_firefox,
        "chrome": __get_chrome
    }
    func = switcher.get(name.lower())
    return func(headless)