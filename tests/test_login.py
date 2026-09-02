from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)
    assert inventory_page.is_loaded()

def test_invalid_login(driver):
        login_page = LoginPage(driver)
        login_page.load()
        login_page.login("locked_out_user", "secret_sauce")

        assert "locked out" in login_page.get_error_text().lower()
