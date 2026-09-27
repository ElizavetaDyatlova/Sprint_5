from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from helpers import URL
from locators import TestLocators


class TestConstructor:

    def test_buns_section(self, driver):
        driver.get(URL)
        driver.find_element(*TestLocators.TAB_SAUCES).click()
        driver.find_element(*TestLocators.TAB_BUNS).click()
        active = WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.ACTIVE_BUNS)
        )
        assert active.text == "Булки"

    def test_sauces_section(self, driver):
        driver.get(URL)
        driver.find_element(*TestLocators.TAB_SAUCES).click()
        active = WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.ACTIVE_SAUCES)
        )
        assert active.text == "Соусы"

    def test_fillings_section(self, driver):
        driver.get(URL)
        driver.find_element(*TestLocators.TAB_FILLINGS).click()
        active = WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.ACTIVE_FILLINGS)
        )
        assert active.text == "Начинки"