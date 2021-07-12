import time

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def product_page(self):
        self.add_to_cart()
        self.should_be_added_to_cart()
        self.should_be_that_price()

    def add_to_cart(self):
        add_to_cart_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART)
        add_to_cart_button.click()

    def should_be_added_to_cart(self):
        x = self.browser.find_element(*ProductPageLocators.PRODUCT_ADDED_TO_CART_MESSAGE).text
        print(x)
        assert x == "The shellcoder's handbook", "Product is not added to cart"

    def should_be_that_price(self):
        x = self.browser.find_element(*ProductPageLocators.PRODUCT_ADDED_PRICE_MESSAGE).text
        y = self.browser.find_element(*ProductPageLocators.SELLING_PRICE).text
        print(f"Is {x} == {y} ?")
        assert y == x, "Wrong price in cart"
