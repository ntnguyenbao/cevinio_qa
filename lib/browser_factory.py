from selenium import webdriver
from pathlib import Path
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn


def __get_current_path():
    return str(Path(__file__).parent.absolute())


def __get_firefox() -> webdriver:
    """This function establishes firefox browser."""
    firefox_options = webdriver.firefox.options.Options()
    firefox_options.set_preference("dom.push.enabled", False)

    return webdriver.Firefox(firefox_options=firefox_options)


def __get_chrome() -> webdriver:
    """This function establishes chrome browser."""
    chrome_options = webdriver.chrome.options.Options()
    chrome_options.add_argument('ignore-certificate-errors')
    chrome_options.add_experimental_option("prefs", {
        "profile.default_content_setting_values.notifications": 1
    })

    return webdriver.Chrome(chrome_options=chrome_options)

@keyword("Get Browser")
def get_browser(name: str):
    """This function is used for quick selection of browser."""
    switcher = {
        "firefox": __get_firefox,
        "chrome": __get_chrome
    }
    func = switcher.get(name.lower())
    driver = func()
    BuiltIn().get_library_instance('Selenium2Library').register_driver(driver, name)
    return driver