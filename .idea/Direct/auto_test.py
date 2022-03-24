# запускаем код в PyCharm
from selenium import webdriver
import time
import unittest

browser = webdriver.Chrome()
class TestAbs(unittest.TestCase):
    def test_abs1(self):
        browser.get("http://suninjuly.github.io/registration1.html")

        input1 = browser.find_element_by_xpath("//input[@placeholder=\"Input your first name\"]")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_xpath("//input[@placeholder=\"Input your last name\"]")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_xpath("//input[@placeholder=\"Input your email\"]")
        input3.send_keys("R@yandex.ru")

        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        time.sleep(2)

        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual ("Congratulations! You have successfully registered!" == welcome_text)
    def test_abs2(self):
        browser.get("http://suninjuly.github.io/registration2.html")

        input1 = browser.find_element_by_xpath("//input[@placeholder=\"Input your first name\"]")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_xpath("//input[@placeholder=\"Input your last name\"]")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_xpath("//input[@placeholder=\"Input your email\"]")
        input3.send_keys("R@yandex.ru")

        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(2)

        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual ("Congratulations! You have successfully registered!" == welcome_text)

if __name__ == "__main__":
    unittest.main()
