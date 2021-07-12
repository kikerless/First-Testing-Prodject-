from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_PAGE_LINK = (By.CSS_SELECTOR, "#registration_link")


class LoginPageLocators:
    CURRENT_URL = ".current_url"
    LOGIN_FORM = (By.ID, "login_form")
    REGISTRATION_FORM = (By.ID, "register_form")


class ProductPageLocators:
    ADD_TO_CART = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_ADDED_TO_CART_MESSAGE = (By.XPATH, "/html/body/div[2]/div/div[1]/div[1]/div/strong")
    PRODUCT_ADDED_PRICE_MESSAGE = (By.XPATH, "/html/body/div[2]/div/div[1]/div[3]/div/p[1]/strong")
    SELLING_PRICE = (By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/article/div[1]/div[2]/p[1]")
