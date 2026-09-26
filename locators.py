from selenium.webdriver.common.by import By


class TestLocators:
    """Локаторы для автотестов Stellar Burgers."""

    #Регистрация
    INPUT_NAME = (By.XPATH, "//fieldset[1]//input")
    #Поле Имя в форме регистрации

    INPUT_EMAIL_REG = (By.XPATH, "//fieldset[2]//input")
    #Поле Email в форме регистрации

    INPUT_PASSWORD_REG = (By.XPATH, "//fieldset[3]//input")
    #Поле Пароль в форме регистрации

    BUTTON_REGISTER_SUBMIT = (By.XPATH, "//button[text()='Зарегистрироваться']")
    #Кнопка Зарегистрироваться

    NOTIFICATION_INCORRECT_PASSWORD = (By.XPATH, "//p[text()='Некорректный пароль']")
    #Сообщение Некорректный пароль

    #Авторизация
    BUTTON_LOGIN_ACCOUNT = (By.XPATH, "//button[text()='Войти в аккаунт']")
    #Кнопка Войти в аккаунт на главной

    INPUT_EMAIL_AUTH = (By.XPATH, "//fieldset[1]//input")
    #Поле Email в форме авторизации

    INPUT_PASSWORD_AUTH = (By.XPATH, "//fieldset[2]//input")
    #Поле Пароль в форме авторизации

    BUTTON_LOGIN = (By.XPATH, "//button[text()='Войти']")
    #Кнопка Войти в форме авторизации

    LINK_LOGIN_IN_REG_FORM = (By.XPATH, "//a[text()='Войти']")
    #Ссылка Войти в форме регистрации

    LINK_FORGOT_PASSWORD = (By.XPATH, "//a[text()='Восстановить пароль']")
    #Ссылка Восстановить пароль на странице авторизации

    LINK_LOGIN_IN_RECOVERY_FORM = (By.XPATH, "//a[text()='Войти']")
    #Ссылка Войти в форме восстановления пароля

    #Шапка сайта
    BUTTON_PERSONAL_ACCOUNT = (By.XPATH, "//p[text()='Личный Кабинет']")
    #Кнопка Личный Кабинет в шапке

    BUTTON_CONSTRUCTOR = (By.XPATH, "//p[text()='Конструктор']")
    #Кнопка Конструктор в шапке

    LOGO = (By.XPATH, "//div[contains(@class, 'AppHeader_header__logo')]")
    #Логотип Stellar Burgers

    BUTTON_ORDER = (By.XPATH, "//button[text()='Оформить заказ']")
    #Кнопка Оформить заказ - маркер авторизации на главной

    #Личный кабинет
    BUTTON_LOGOUT = (By.XPATH, "//button[text()='Выход']")
    #Кнопка Выйти в личном кабинете

    #Конструктор
    TAB_BUNS = (By.XPATH, "//span[text()='Булки']")
    #Таб Булки

    TAB_SAUCES = (By.XPATH, "//span[text()='Соусы']")
    #Таб Соусы

    TAB_FILLINGS = (By.XPATH, "//span[text()='Начинки']")
    #Таб Начинки

    ACTIVE_BUNS = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]//span[text()='Булки']")
    #Активный таб Булки

    ACTIVE_SAUCES = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]//span[text()='Соусы']")
    #Активный таб Соусы

    ACTIVE_FILLINGS = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]//span[text()='Начинки']")
    #Активный таб Начинки