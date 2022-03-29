import time


def test_items_find(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)
    button = browser.find_elements_by_css_selector('[class="btn btn-lg btn-primary btn-add-to-basket"]')
    assert button, "!!!КНОПКА НЕ НАЙДЕНА!!!"
