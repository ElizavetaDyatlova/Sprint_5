# Проект автоматизации тестирования Stellar Burgers

Основа для написания автотестов - фреймворк pytest и библиотека Selenium WebDriver

## Установка

pip install selenium pytest

Установить браузер Google Chrome

## Запуск

pytest -v

## Структура проекта

- tests/ - тесты, сгруппированные по функциональности.
- conftest.py - фикстуры.
- locators.py - локаторы элементов.
- helpers.py - генераторы логина и пароля, вспомогательные функции.