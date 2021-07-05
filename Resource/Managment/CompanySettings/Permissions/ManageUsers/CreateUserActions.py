from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select

from Resource.BaseActions import BaseActions
from Resource.Managment.CompanySettings.Permissions.ManageUsers.CreateUserPage import CreateUserPage


class CreateUserActions(BaseActions):
    def __init__(self):
        super().__init__()

    @keyword("Create User form is displayed")
    def create_user_form_is_displayed(self):
        self.driver = BuiltIn().get_library_instance('Selenium2Library').driver
        self.form_new_user = self.find_element(CreateUserPage.form_new_user)

    @keyword("Input field ${fieldName} with value ${value}")
    def input_field(self, fieldName: str, value: str):
        xpath = CreateUserPage.txt_fields.replace("?", fieldName)
        txt_filed = self.find_element(xpath)
        txt_filed.send_keys(value)

    @keyword("user selects Coscenter ${costcenter}")
    def select_costcenter(self, costcenter: str):
        self.li_costcenter = self.find_element(CreateUserPage.li_costcenter)
        self.li_costcenter = Select(self.li_costcenter)
        self.li_costcenter.select_by_visible_text(costcenter)

    @keyword("user update Account Locked checkbox")
    def update_is_locked_account(self, is_lock: bool):
        self.chk_is_locked = self.find_element(CreateUserPage.chk_is_locked)
        if self.chk_is_locked.is_selected() != is_lock:
            self.chk_is_locked.click()

    @keyword("user inputs ${userInfo} into form")
    def input_form(self, userInfo: dict):
        for key in userInfo.keys():
            if key not in ['Costcenter', 'Account locked']:
                self.input_field(key, userInfo.get(key))
                if key == 'Password':
                    self.input_field('Confirm Password', userInfo.get(key))
            elif key == 'Costcenter':
                self.select_costcenter(userInfo.get(key))
            elif key == 'Account locked':
                self.update_is_locked_account(bool(userInfo.get(key)))

    @keyword('click Submit button')
    def click_submit_btn(self):
        self.btn_submit = self.find_element(CreateUserPage.btn_submit)
        self.btn_submit.click()
