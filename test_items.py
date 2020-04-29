

def test_basket(browser):
    link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    browser.implicitly_wait(10)
    check=browser.find_element_by_css_selector("#wrong locator")
    assert check, "корзинка не найдена"
