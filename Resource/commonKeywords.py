from robot.api.deco import keyword

from Resource.BaseKeywords import BaseKeywords
from lib.browser_factory import get_browser


class commonKeywords(BaseKeywords):


    def __init__(self):
        super().__init__()

    @keyword("user accesses ${url} by ${browser}")
    def access_url_by_browser(self, url, browser):
        self.driver = get_browser(browser)
        self.driver.maximize_window()
        self.driver.get(url)
