from Pages.searchResult import searchResultPage as searchPage
from robot.api.deco import keyword
from keywords.BaseKeywords import BaseKeywords
from selenium.webdriver.common.action_chains import ActionChains
from robot.libraries.BuiltIn import BuiltIn
import random


class searchResultKeywords(BaseKeywords):

    def __init__(self):
        super().__init__()
        self.searchButton = None
        self.list_actual_links = None
        self.warn_msg = None

    @keyword("Search Result page is loaded successfully")
    def wait_for_search_page_load(self, driver, timeout: int):
        self.driver = driver
        self.searchButton = self.find_element(searchPage.searchButton, timeout)
        assert self.searchButton is not None, 'Search Result page cannot be loaded'

    @keyword("Actual result should be same ${expected_result}")
    def validate_search_result(self, expected_result: list):
        list_expected_ids = []
        for record in expected_result:
            list_expected_ids.extend(str(record['expected links']).replace(' ', '').split(','))
        self.list_actual_links = self.find_elements(searchPage.cityLink)
        is_pass = True
        for id in list_expected_ids:
            is_found = False
            for link in self.list_actual_links:
                if str(link.get_attribute('href')).find(id) != -1:
                    is_found = True
                    break
            if not is_found:
                is_pass = False
                break

        assert is_pass, "Expected id %s cannot be found" % id

    @keyword("Click a random result link")
    def click_random_link(self):
        random_link_idx = random.randint(0, len(self.list_actual_links) - 1)
        # actions = ActionChains(self.driver)
        # actions.move_to_element(random_link).perform()
        if random_link_idx > 0:
            self.list_actual_links[random_link_idx - 1].location_once_scrolled_into_view
        self.list_actual_links[random_link_idx].click()

    @keyword("Warning message \"${expected_msg}\" is displayed")
    def warning_message_is_displayed(self, expected_msg: str):
        self.warn_msg = self.find_element(searchPage.warning_msg)
        assert expected_msg.lower() in self.warn_msg.text.lower(), 'Warning message is not as expected'
