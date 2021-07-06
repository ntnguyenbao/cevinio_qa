from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn

from Resource.BaseActions import BaseActions
from Resource.Managment.CompanySettings.CompanySettingsPage import CompanySettingsPage


class CompanySettingsActions(BaseActions):
    def __init__(self):
        super().__init__()

    @keyword("Company Settings page is displayed")
    def company_settings_page_is_displayed(self):
        self.driver = BuiltIn().get_library_instance('Selenium2Library').driver
        self.box_info = self.find_element(CompanySettingsPage.box_info)
        assert CompanySettingsPage.page_description in self.box_info.text

    @keyword("a notice message is displayed \"${message}\"")
    def notice_message_is_displayed(self, message: str):
        list_elements = self.find_elements(CompanySettingsPage.box_notice)
        is_displayed = False
        for element in list_elements:
            if message in element.text:
                is_displayed = True
                break
        assert is_displayed
