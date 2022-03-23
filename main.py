from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()
try:
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    # находим кнопку №1
    but = browser.find_element(By.ID, "book")
    # ждем заданные 12 сек до того как прайс опустится до $100
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    # кликаем
    but.click()

    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)
    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)
    # находим кнопку №2 и кликаем
    button = browser.find_element(By.ID, "solve")
    button.click()

finally:
    time.sleep(20)
    browser.quit()