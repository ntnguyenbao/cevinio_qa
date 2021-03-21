from Pages.home import homePage as homePage
from robot.api.deco import keyword
from keywords.BaseKeywords import BaseKeywords


class homeKeywords(BaseKeywords):


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
