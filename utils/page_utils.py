from time import sleep
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

class PageUtils():

    def __init__(self, driver) -> None:
        self.driver = driver

    def get_element(self, locator):
        method = locator[0]
        values = locator[1]

        if type(values) is str:
            return self.get_element_by_type(method, values)
        elif type(values) is list:
            for value in values:
                try:
                    return self.get_element_by_type(method, value)
                except NoSuchElementException:
                    pass
            raise NoSuchElementException

    def get_element_by_type(self, method, value):
        if method == "accessibility_id":
            return self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, value)
        elif method == "android":
            return self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().%s' % value)
        elif method == "ios":
            return self.driver.find_element(AppiumBy.IOS_UIAUTOMATION, value)
        elif method == "class_name":
            return self.driver.find_element(AppiumBy.CLASS_NAME, value)
        elif method == "id":
            return self.driver.find_element(AppiumBy.ID, value)
        elif method == "xpath":
            return self.driver.find_element(AppiumBy.XPATH, value)
        elif method == "name":
            return self.driver.find_element(AppiumBy.NAME, value)
        else:
            raise Exception('Invalid locator method.')

    def is_visible(self, locator):
        try:
            self.get_element(locator).is_displayed()
            return True
        except NoSuchElementException:
            return False

    def wait_visible(self, locator, timeout=10):
        i = 0
        while i != timeout:
            try:
                self.is_visible(locator)
                return self.get_element(locator)
            except NoSuchElementException:
                sleep(1)
                i += 1
        raise Exception('Element never became visible: %s (%s)' % (locator[0], locator[1]))

    def click(self, locator):
        element = self.wait_visible(locator)
        element.click()

    def tap(self, locator):
        element = self.wait_visible(locator)
        element.tap()

    def wait(self, locator, seconds=25):
        WebDriverWait(self.driver, seconds).until(EC.presence_of_element_located(locator))

    def get_text(self, locator):
        element = self.wait_visible(locator)
        return element.text