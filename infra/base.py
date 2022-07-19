from utils.page_utils import PageUtils

class Base():

    def __init__(self, driver) -> None:
        self.driver = driver
        self.page_utils = PageUtils(self.driver)

    def get_element(self, locator):
        self.page_utils.get_element(locator)

    def get_element_by_type(self, method, value):
        self.page_utils.get_element_by_type(method, value)

    def is_visible(self, locator):
        self.page_utils.is_visible(locator)

    def click(self, locator):
        self.page_utils.click(locator)
    
    def tap(self, locator):
        self.page_utils.tap(locator)

    def get_text(self, locator):
        return self.page_utils.get_text(locator)