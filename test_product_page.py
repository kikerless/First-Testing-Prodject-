from pages.main_page import MainPage
from pages.product_page import ProductPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = MainPage(browser, link)
    page.open()
    product_page = ProductPage(browser, browser.current_url)
    product_page.add_to_cart()
    page.solve_quiz_and_get_code()
    product_page.should_be_added_to_cart()
    product_page.should_be_that_price()
