import pytest
from pages.home import HomePage

@pytest.mark.usefixtures('setup')
class TestHome():

    def test_home(self):
        driver = self.driver
        self.homepage = HomePage(driver)
        self.homepage.click_allow_location()
        self.homepage.click_transport_icon()
        assert self.homepage.get_alert_title() == "Alert"
        assert self.homepage.get_alert_message() == "Transport"
        self.homepage.click_alert_ok_button()