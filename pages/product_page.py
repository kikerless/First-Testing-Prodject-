from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def product_page(self):
        self.add_to_cart()
        self.should_be_added_to_cart()
        self.should_be_that_price()
        self.should_not_be_success_message()
        self.should_not_be_success_message_disappeared_method()

    def add_to_cart(self):
        add_to_cart_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART)
        add_to_cart_button.click()

    def should_be_added_to_cart(self):
        x = self.browser.find_element(*ProductPageLocators.PRODUCT_ADDED_TO_CART_MESSAGE).text
        y = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        print(f"Is {x} == {y} ?")
        assert y == x, "Wrong product name in cart"

    def should_be_that_price(self):
        x = self.browser.find_element(*ProductPageLocators.PRODUCT_ADDED_PRICE_MESSAGE).text
        y = self.browser.find_element(*ProductPageLocators.SELLING_PRICE).text
        print(f"Is {x} == {y} ?")
        assert y == x, "Wrong product price in cart"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_not_be_success_message_disappeared_method(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
