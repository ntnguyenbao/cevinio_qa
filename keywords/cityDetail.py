import sys

sys.path.append("..")

from Pages.cityDetail import cityDetailPage as detailPage
from robot.api.deco import keyword
from keywords.BaseKeywords import BaseKeywords


class cityDetail(BaseKeywords):

    def __init__(self):
        super().__init__()
        self.weather_widget = None
        self.city_name_header = None

    @keyword("City Detail page is loaded successfully")
    def wait_for_page_load(self, driver, timeout: int = 30):
        self.driver = driver
        self.weather_widget = self.find_element(detailPage.weather_widget, timeout)
        assert self.weather_widget is not None, 'City Detail page cannot be loaded'

    @keyword("Detail of ${city} is displayed")
    def validate_display_city(self, city: str):
        self.city_name_header = self.find_element(detailPage.city_name_header)
        displayed_city = self.city_name_header.text
        assert city.lower() in displayed_city.lower(), "Displayed detail is not %s city" % city
