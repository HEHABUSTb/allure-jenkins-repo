from .base_page import BasePage
from .locators import MainPageLocators
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    def add_book_in_basket(self):
        book_add_button = self.browser.find_element(*MainPageLocators.BOOK_ADD_BUTTON)
        book_add_button.click()

    def basket_is_not_empty(self):
        assert self.is_element_present(*MainPageLocators.ITEMS_IN_BASKET), 'Basket is empty'