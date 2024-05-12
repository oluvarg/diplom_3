from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element_visibility(self, locator, timeout=20):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator),
                                                         message=f"Can't find element by locator {locator}")

    def find_element_clickable(self, locator, timeout=20):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator),
                                                         message=f"Can't find element by locator {locator}")

    def find_element_not_visibility(self, locator, timeout=60):
        return WebDriverWait(self.driver, timeout).until_not(EC.visibility_of_element_located(locator),
                                                             message=f"Can't find element by locator {locator}")

    def set_text(self, locator, text):
        element = self.find_element_visibility(locator)
        element.send_keys(text)

    def get_text(self, locator):
        element = self.find_element_visibility(locator)
        return element.text

    def click_element_if_visibility(self, locator):
        element = self.find_element_visibility(locator)
        element.click()

    def click_element_if_clickable(self, locator):
        element = self.find_element_clickable(locator)
        element.click()

    def open_url(self, url):
        self.driver.get(url)

    def get_url(self):
        return self.driver.current_url

    def check_exist_element(self, locator):
        try:
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            return False
        return True

    def drag_and_drop_on_element(self, locator_one, locator_two):
        draggable = self.driver.find_element(*locator_one)
        droppable = self.driver.find_element(*locator_two)
        action_chains = ActionChains(self.driver)
        action_chains.drag_and_drop(draggable, droppable).perform()

    def check_invisibility(self, locator) -> object:
        return WebDriverWait(self.driver, 10).until(EC.invisibility_of_element(locator))

    def check_presence(self, locator):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        return self.driver.find_element(*locator)

    def find_until_all_elements_located(self, locator):
        return WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located(locator))
