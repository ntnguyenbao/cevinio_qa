from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from robot.api.logger import librarylogger as logger
from robot.api.deco import keyword
from lib.browser_factory import *


class BaseActions(object):

    def __init__(self):
        self.driver = None

    def find_element(self, sLocator: str, timeout: int = 30):
        wait = WebDriverWait(self.driver, timeout)
        lSplitLocator = sLocator.split(':', 1)
        dLocatorType = {
            'id': By.ID,
            'name': By.NAME,
            'xpath': By.XPATH,
            'link_text': By.LINK_TEXT,
            'partial_link_text': By.PARTIAL_LINK_TEXT,
            'tag_name': By.TAG_NAME,
            'class': By.CLASS_NAME,
            'css_selector': By.CSS_SELECTOR
        }
        if len(lSplitLocator) <= 1:
            raise Exception("locator %s is in incorrect format. Expected format: <locator type>:<locator value> (e.g. xpath://div)" % sLocator)
        locatorType = dLocatorType.get(lSplitLocator[0].lower())
        return wait.until(EC.presence_of_element_located((locatorType, lSplitLocator[1])))

    def find_elements(self, sLocator: str, timeout: int = 30):
        wait = WebDriverWait(self.driver, timeout)
        lSplitLocator = sLocator.split(':', 1)
        dLocatorType = {
            'id': By.ID,
            'name': By.NAME,
            'xpath': By.XPATH,
            'link_text': By.LINK_TEXT,
            'partial_link_text': By.PARTIAL_LINK_TEXT,
            'tag_name': By.TAG_NAME,
            'class': By.CLASS_NAME,
            'css_selector': By.CSS_SELECTOR
        }
        if len(lSplitLocator) <= 1:
            raise Exception("locator %s is in incorrect format. Expected format: <locator type>:<locator value> (e.g. xpath://div)" % sLocator)
        locatorType = dLocatorType.get(lSplitLocator[0].lower())
        return wait.until(EC.presence_of_all_elements_located((locatorType, lSplitLocator[1])))


