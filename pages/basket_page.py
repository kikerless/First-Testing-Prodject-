from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def product_page(self):
        self.should_not_be_products_in_cart()
        self.should_be_message_empty_cart()

    def should_not_be_products_in_cart(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_CART), \
            "Product in cart, but should not be"

    def should_be_message_empty_cart(self):
        assert self.is_disappeared(*BasketPageLocators.CART_IS_EMPTY), \
            "Success message is presented, but should not be"
