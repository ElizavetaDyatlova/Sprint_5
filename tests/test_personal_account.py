from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from helpers import generate_email, generate_password, login, register_new_user, URL
from locators import TestLocators


class TestPersonalAccount:

    def test_go_to_personal_account(self, driver):
        email = generate_email()
        password = generate_password()
        register_new_user(driver, email, password)
        driver.get(URL)
        driver.find_element(*TestLocators.BUTTON_LOGIN_ACCOUNT).click()
        login(driver, email, password)
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.BUTTON_ORDER)
        )
        driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.BUTTON_LOGOUT)
        )
        assert driver.current_url == f"{URL}account/profile"

    def test_go_from_account_to_constructor(self, driver):
        email = generate_email()
        password = generate_password()
        register_new_user(driver, email, password)
        driver.get(URL)
        driver.find_element(*TestLocators.BUTTON_LOGIN_ACCOUNT).click()
        login(driver, email, password)
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.BUTTON_ORDER)
        )
        driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.BUTTON_LOGOUT)
        )
        driver.find_element(*TestLocators.BUTTON_CONSTRUCTOR).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.BUTTON_ORDER)
        )
        assert driver.current_url == URL

    def test_go_from_account_to_constructor_via_logo(self, driver):
        email = generate_email()
        password = generate_password()
        register_new_user(driver, email, password)
        driver.get(URL)
        driver.find_element(*TestLocators.BUTTON_LOGIN_ACCOUNT).click()
        login(driver, email, password)
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.BUTTON_ORDER)
        )
        driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.BUTTON_LOGOUT)
        )
        driver.find_element(*TestLocators.LOGO).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.BUTTON_ORDER)
        )
        assert driver.current_url == URL

    def test_logout(self, driver):
        email = generate_email()
        password = generate_password()
        register_new_user(driver, email, password)
        driver.get(URL)
        driver.find_element(*TestLocators.BUTTON_LOGIN_ACCOUNT).click()
        login(driver, email, password)
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.BUTTON_ORDER)
        )
        driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.BUTTON_LOGOUT)
        )
        driver.find_element(*TestLocators.BUTTON_LOGOUT).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.BUTTON_LOGIN)
        )
        assert driver.current_url == f"{URL}login"