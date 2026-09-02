from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    CART_ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")

    def get_item_names(self):
        elements = self.driver.find_elements(*self.CART_ITEM_NAMES)
        return [el.text for el in elements]