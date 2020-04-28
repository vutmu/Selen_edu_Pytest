

def test_basket(browser):
    link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    browser.implicitly_wait(10)
    assert browser.find_element_by_css_selector("#add_to_basket_form")