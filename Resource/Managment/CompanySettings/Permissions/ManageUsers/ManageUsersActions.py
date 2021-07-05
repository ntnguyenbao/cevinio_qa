from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn

from Resource.BaseActions import BaseActions
from Resource.Managment.CompanySettings.Permissions.ManageUsers.ManageUsersPage import ManageUsersPage


class ManageUsersActions(BaseActions):

    def __init__(self):
        super().__init__()

    @keyword("Manage Users page is displayed")
    def manage_users_is_displayed(self):
        self.driver = BuiltIn().get_library_instance('Selenium2Library').driver
        self.box_info = self.find_element(ManageUsersPage.box_info)
        assert ManageUsersPage.page_description in self.box_info.text
        self.tbl_user_browser = self.find_element(ManageUsersPage.tbl_user_browser)

    @keyword("user clicks Add User link")
    def click_add_user_link(self):
        self.lnk_add_user = self.find_element(ManageUsersPage.lnk_add_user)
        self.lnk_add_user.click()