import random

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import TestLocators

URL = "https://stellarburgers.education-services.ru/"


def generate_email():
    return f"test_{random.randint(10000, 99999)}@ya.ru"


def generate_password():
    return f"pass{random.randint(1000, 9999)}"


def register_new_user(driver, email, password):
    driver.get(f"{URL}register")
    driver.find_element(*TestLocators.INPUT_NAME).send_keys("Иван")
    driver.find_element(*TestLocators.INPUT_EMAIL_REG).send_keys(email)
    driver.find_element(*TestLocators.INPUT_PASSWORD_REG).send_keys(password)
    driver.find_element(*TestLocators.BUTTON_REGISTER_SUBMIT).click()
    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located(TestLocators.BUTTON_LOGIN)
    )


def login(driver, email, password):
    driver.find_element(*TestLocators.INPUT_EMAIL_AUTH).send_keys(email)
    driver.find_element(*TestLocators.INPUT_PASSWORD_AUTH).send_keys(password)
    driver.find_element(*TestLocators.BUTTON_LOGIN).click()