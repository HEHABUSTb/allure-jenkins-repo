from pages.main_page import MainPage
from selenium.webdriver.common.by import By
import pytest
import allure_pytest
import allure

link = 'http://selenium1py.pythonanywhere.com/' #main_page link

@pytest.mark.smoke
def test_guest_can_add_item_in_basket(browser):
    page = MainPage(browser, link)
    page.open()
    page.add_book_in_basket()
    page.basket_is_not_empty()

