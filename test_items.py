

def is_element_present(browser):
    try:
        browser.implicitly_wait(10)
        browser.find_element_by_css_selector("#add_to_basket_form")
        return True
    except:
        return False

def test_basket(browser):
    link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    assert is_element_present(browser)==True, "корзинка не найдена"
