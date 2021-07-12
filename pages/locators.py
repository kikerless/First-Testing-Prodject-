from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_PAGE_LINK = (By.CSS_SELECTOR, "#registration_link")


class LoginPageLocators:
    CURRENT_URL = ".current_url"
    LOGIN_FORM = (By.ID, "login_form")
    REGISTRATION_FORM = (By.ID, "register_form")

