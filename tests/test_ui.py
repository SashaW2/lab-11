from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import os


def get_driver():

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, "..", "index.html")

    driver.get(f"file:///{file_path}")

    return driver


def test_title_exists():

    driver = get_driver()

    title = driver.find_element(By.ID, "title")

    assert title.text == "Форма обратной связи"

    driver.quit()


def test_button_text():

    driver = get_driver()

    button = driver.find_element(By.ID, "submitBtn")

    assert button.text == "Отправить форму"

    driver.quit()


def test_empty_form():

    driver = get_driver()

    button = driver.find_element(By.ID, "submitBtn")
    button.click()

    message = driver.find_element(By.ID, "message")

    assert message.text == "Заполните все поля"

    driver.quit()


def test_success_submit():

    driver = get_driver()

    driver.find_element(By.ID, "name").send_keys("Ivan")
    driver.find_element(By.ID, "email").send_keys("ivan@test.com")

    driver.find_element(By.ID, "submitBtn").click()

    message = driver.find_element(By.ID, "message")

    assert message.text == "Форма успешно отправлена"

    driver.quit()