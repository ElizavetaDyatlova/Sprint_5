from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from helpers import generate_email, generate_password, login, register_new_user, URL
from locators import TestLocators


class TestLogin:

    def test_login_from_main_page(self, driver):
        email = generate_email()
        password = generate_password()
        register_new_user(driver, email, password)
        driver.get(URL)
        driver.find_element(*TestLocators.BUTTON_LOGIN_ACCOUNT).click()
        login(driver, email, password)
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.BUTTON_ORDER)
        )
        assert driver.current_url == URL

    def test_login_via_personal_account_button(self, driver):
        email = generate_email()
        password = generate_password()
        register_new_user(driver, email, password)
        driver.get(URL)
        driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()
        login(driver, email, password)
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.BUTTON_ORDER)
        )
        assert driver.current_url == URL

    def test_login_via_register_form_link(self, driver):
        email = generate_email()
        password = generate_password()
        register_new_user(driver, email, password)
        driver.get(f"{URL}register")
        driver.find_element(*TestLocators.LINK_LOGIN_IN_REG_FORM).click()
        login(driver, email, password)
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.BUTTON_ORDER)
        )
        assert driver.current_url == URL

    def test_login_via_recovery_form_link(self, driver):
        email = generate_email()
        password = generate_password()
        register_new_user(driver, email, password)
        driver.get(f"{URL}forgot-password")
        driver.find_element(*TestLocators.LINK_LOGIN_IN_RECOVERY_FORM).click()
        login(driver, email, password)
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.BUTTON_ORDER)
        )
        assert driver.current_url == URL