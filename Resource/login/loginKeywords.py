import sys

from robot.libraries.BuiltIn import BuiltIn

sys.path.append("../..")

from Resource.login.loginPage import loginPage
from robot.api.deco import keyword
from Resource.BaseKeywords import BaseKeywords

class loginKeywords(BaseKeywords):
    def __init__(self):
        super().__init__()

    @keyword("login page is displayed")
    def login_page_is_displayed(self):
        self.driver = BuiltIn().get_library_instance('Selenium2Library').driver
        self.hdr_sigin = self.find_element(loginPage.hdr_signin)
        self.txt_username = self.find_element(loginPage.txt_username)
        self.txt_passwd = self.find_element(loginPage.txt_passwd)
        self.btn_signin = self.find_element(loginPage.btn_signin)

    @keyword("user inputs username ${username}")
    def user_input_username(self, username: str):
        self.txt_username.send_keys(username)

    @keyword("user inputs password ${passwd}")
    def user_input_password(self, passwd: str):
        self.txt_passwd.send_keys(passwd)

    @keyword("click Sign in button")
    def click_sign_in_button(self):
        self.btn_signin.click()

    @keyword("user login by ${username}/${password}")
    def login(self, username: str, password: str):
        self.user_input_username(username)
        self.user_input_password(password)
        self.click_sign_in_button()
