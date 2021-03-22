import string
import random
import sys

sys.path.append("..")

from Pages.home import homePage as homePage
from robot.api.deco import keyword
from keywords.BaseKeywords import BaseKeywords


class home(BaseKeywords):


    def __init__(self):
        self.driver = None
        self.searchFiled = None
        self.searchForm = None
        self.menuButton = None

    @keyword("Access Home Page")
    def access_home_page(self, driver):
        self.driver = driver
        self.driver.get(homePage.url)
        self.driver.maximize_window()
        self.searchFiled = self.find_element(homePage.searchField)
        self.searchForm = self.find_element(homePage.searchForm)
        self.menuButton = self.find_element(homePage.menuButton)
        assert self.searchFiled is not None and self.searchForm is not None and self.menuButton is not None, "Home page cannot be loaded"

    @keyword()
    def search_city(self, city: str, country: str = ''):
        search_keyword = city
        search_keyword = search_keyword + ",%s" % country if country != '' else search_keyword
        self.searchFiled.send_keys(search_keyword)
        self.searchForm.submit()

    @keyword()
    def search_random_string(self):
        letters = string.ascii_letters
        random_string = ''.join(random.choice(letters) for i in range(10))
        self.search_city(city=random_string)

    @keyword("Change browser window size height: ${height} width: ${width}")
    def change_browser_window_size(self, height: int, width: int):
        self.driver.set_window_size(height,width)

    @keyword()
    def extend_home_menu(self):
        self.menuButton = self.find_element(homePage.menuButton)
        self.menuButton.click()
        self.searchFiled = self.find_element(homePage.searchField)
        assert self.searchFiled is not None, "Cannot extend home menu"

