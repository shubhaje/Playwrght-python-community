import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

@pytest.fixture
def setup_login(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    return page

@pytest.mark.smoke
def test_add_item_to_cart(setup_login):
    inventory_page = InventoryPage(setup_login)
    initial_count = inventory_page.get_cart_count()
    inventory_page.add_item_to_cart("Sauce Labs Backpack")
    assert inventory_page.get_cart_count() == "1"

@pytest.mark.smoke
def test_remove_item_from_cart(setup_login):
    inventory_page = InventoryPage(setup_login)
    inventory_page.add_item_to_cart("Sauce Labs Backpack")
    inventory_page.remove_item_from_cart("Sauce Labs Backpack")
    assert inventory_page.get_cart_count() == "0"

@pytest.mark.regression
def test_sort_products(setup_login):
    inventory_page = InventoryPage(setup_login)
    inventory_page.sort_products("za")
    product_names = inventory_page.get_product_names()
    assert product_names == sorted(product_names, reverse=True)

@pytest.mark.smoke
def test_cart_workflow(setup_login):
    inventory_page = InventoryPage(setup_login)
    cart_page = CartPage(setup_login)
    
    # Add items to cart
    inventory_page.add_item_to_cart("Sauce Labs Backpack")
    inventory_page.add_item_to_cart("Sauce Labs Bike Light")
    assert inventory_page.get_cart_count() == "2"
    
    # Go to cart and verify items
    inventory_page.go_to_cart()
    cart_items = cart_page.get_cart_items()
    assert "Sauce Labs Backpack" in cart_items
    assert "Sauce Labs Bike Light" in cart_items
    
    # Remove item and verify
    cart_page.remove_item("Sauce Labs Backpack")
    assert cart_page.get_cart_count() == 1
    
    # Continue shopping
    cart_page.continue_shopping()
    assert "inventory.html" in setup_login.url