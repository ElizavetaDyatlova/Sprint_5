from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from helpers import generate_email, generate_password, URL
from locators import TestLocators


class TestRegistration:

    def test_successful_registration(self, driver):
        email = generate_email()
        password = generate_password()
        driver.get(f"{URL}register")
        driver.find_element(*TestLocators.INPUT_NAME).send_keys("Иван")
        driver.find_element(*TestLocators.INPUT_EMAIL_REG).send_keys(email)
        driver.find_element(*TestLocators.INPUT_PASSWORD_REG).send_keys(password)
        driver.find_element(*TestLocators.BUTTON_REGISTER_SUBMIT).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.BUTTON_LOGIN)
        )
        assert driver.current_url == f"{URL}login"

    def test_registration_with_short_password(self, driver):
        driver.get(f"{URL}register")
        driver.find_element(*TestLocators.INPUT_NAME).send_keys("Иван")
        driver.find_element(*TestLocators.INPUT_EMAIL_REG).send_keys(generate_email())
        driver.find_element(*TestLocators.INPUT_PASSWORD_REG).send_keys("123")
        driver.find_element(*TestLocators.BUTTON_REGISTER_SUBMIT).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                TestLocators.NOTIFICATION_INCORRECT_PASSWORD
            )
        )
        assert driver.find_element(
            *TestLocators.NOTIFICATION_INCORRECT_PASSWORD
        ).text == "Некорректный пароль"