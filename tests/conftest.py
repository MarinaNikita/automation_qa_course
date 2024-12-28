# import pytest
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
#
#
# # Фикстура 'driver', которая инициализирует WebDriver
# @pytest.fixture(scope="function")  # Браузер будет открываться после каждого теста
# def driver():
#     # Настройка WebDriver с использованием webdriver_manager для автоматической загрузки правильной версии ChromeDriver
#     driver = webdriver.Chrome(ChromeDriverManager().install())
#
#     # Максимизация окна браузера перед каждым тестом
#     driver.maximize_window()
#
#     # Передаем драйвер в тестовую функцию
#     yield driver
#
#     # Очистка: закрываем браузер после выполнения теста
#     driver.quit()
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--start-maximized")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    yield driver

    driver.quit()

