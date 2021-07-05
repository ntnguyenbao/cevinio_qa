from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select

from Resource.BaseActions import BaseActions
from Resource.Managment.CompanySettings.Permissions.ManageUsers.EditUserRolesAndRightsPage import EditUserRolesAndRightsPage


class EditUserRolesAndRightsActions(BaseActions):
    def __init__(self):
        super().__init__()

    @keyword("Role Assignment page is displayed")
    def role_assignment_page_is_displayed(self):
        selenium = BuiltIn().get_library_instance('Selenium2Library')
        self.driver = BuiltIn().get_library_instance('Selenium2Library').driver
        locator = EditUserRolesAndRightsPage.tab_menu.replace("?", 'tab_')
        list_tab_menu = self.find_elements(locator)
        for tab in list_tab_menu:
            assert tab.get_attribute("id") in EditUserRolesAndRightsPage.expected_tabs
        selenium.capture_page_screenshot()