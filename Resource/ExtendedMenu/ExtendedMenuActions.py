from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn

from Resource.BaseActions import BaseActions
from Resource.ExtendedMenu.ExtendedMenuPage import ExtendedMenuPage


class ExtendedMenuActions(BaseActions):
    def __init__(self):
        super().__init__()

    @keyword("Extended menu is displayed")
    def extended_menu_is_displayed(self):
        self.driver = BuiltIn().get_library_instance('Selenium2Library').driver
        self.menu = self.find_element(ExtendedMenuPage.menu)

    @keyword("user selects ${selected_item} from menu")
    def select_item_from_menu(self, selected_item: str):
        ls_items = selected_item.split('/')
        self.extended_menu_is_displayed()
        xpath = ExtendedMenuPage.menu
        for item in ls_items:
            xpath += "//following::a[text() = '%s']" % item
        self.lnk_menu = self.find_element(xpath)
        self.lnk_menu.click()
