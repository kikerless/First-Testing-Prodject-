from .base_page import BasePage
from .locators import LoginPageLocators, BasePageLocators


email, password = "maiil@lol.com", "qwerty321"


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()
        self.register_new_user(email, password)

    def should_be_login_url(self):
        assert self.browser*LoginPageLocators.CURRENT_URL == "http://selenium1py.pythonanywhere.com/ru/accounts/login/"\
            , "Wrong login url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not presented"

    def register_new_user(self, email, password):
        input_email = self.browser.find_element(*BasePageLocators.USER_REGISTRATION_INPUT_EMAIL)
        input_email.send_keys(email)
        input_pass = self.browser.find_element(*BasePageLocators.USER_REGISTRATION_INPUT_PASS)
        input_pass.send_keys(password)
        input_pass2 = self.browser.find_element(*BasePageLocators.USER_REGISTRATION_INPUT_PASS_REPEAT)
        input_pass2.send_keys(password)
        submit_button = self.browser.find_element(*BasePageLocators.USER_REGISTRATION_SUBMIT_BUTTON)
        submit_button.click()
