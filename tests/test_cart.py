from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


def test_add_item_to_cart(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)
    inventory_page.add_backpack_to_cart()
    assert inventory_page.get_cart_count() == "1"
    inventory_page.go_to_cart()
    cart_page = CartPage(driver)
    assert "Sauce Labs Backpack" in cart_page.get_item_names()
