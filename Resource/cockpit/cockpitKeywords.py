import sys

from robot.libraries.BuiltIn import BuiltIn


from Resource.cockpit.cockpitPage import cockpitPage
from robot.api.deco import keyword
from Resource.BaseKeywords import BaseKeywords

class cockpitKeywords(BaseKeywords):

    def __init__(self):
        super().__init__()

    @keyword("Cockpit page is displayed")
    def cockpit_page_is_displayed(self):
        self.driver = BuiltIn().get_library_instance('Selenium2Library').driver
        self.client_logo = self.find_element(cockpitPage.client_logo)
        self.li_language = self.find_element(cockpitPage.li_language)
        self.li_my_account = self.find_element(cockpitPage.li_my_account)
        self.li_logout = self.find_element(cockpitPage.li_logout)

    @keyword("user selects module ${group}/${module} from Cockpit page")
    def user_select_module(self, group: str, module: str):
        xpath = cockpitPage.lnk_function.replace("?", group.lower(), 1)
        xpath = xpath.replace("?", module)
        lnk_function = self.find_element(xpath)
        lnk_function.click()

