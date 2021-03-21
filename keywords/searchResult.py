from Pages.searchResult import searchResultPage as searchPage
from robot.api.deco import keyword
from keywords.BaseKeywords import BaseKeywords


class searchResultKeywords(BaseKeywords):

    def __init__(self):
        super().__init__()
        self.searchButton = None

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
        list_actual_links = self.find_elements(searchPage.cityLink)
        is_pass = True
        for id in list_expected_ids:
            is_found = False
            for link in list_actual_links:
                if str(link.get_attribute('href')).find(id) != -1:
                    is_found = True
                    break
            if not is_found:
                is_pass = False
                break

        assert is_pass, "Expected id %s cannot be found" % id
