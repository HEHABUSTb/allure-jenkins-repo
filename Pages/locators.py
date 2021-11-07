from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    VIEW_BASKET = (By.CSS_SELECTOR, ".btn-group .btn-default:nth-child(1)")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators():
    ITEMS_IN_BASKET = (By.XPATH, "//strong[contains(text(), 'The City and the Stars')]")
    BOOK_ADD_BUTTON = (By.CSS_SELECTOR, '.well-blank .row li:nth-child(4) button')