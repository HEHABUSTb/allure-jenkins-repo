import allure

from .pages.main_page import MainPage
from .selenium.webdriver.common.by import By
import pytest


link = 'http://selenium1py.pythonanywhere.com/' #main_page link

@pytest.mark.smoke
@allure.severity(allure.severity_level.NORMAL)
class TestSmokeMainPage():
    @allure.description('Guest can add book in basket')
    def test_guest_can_add_item_in_basket(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.add_book_in_basket()
        page.basket_is_not_empty()

    @allure.description('TEst')
    def test_guest_can_passed_registration(self, browser):
        pytest.skip('Just example skip test for allure')

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Guest should see login link')
    def test_guest_should_see_login_link(self, browser): #example failed test login link invalid
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


