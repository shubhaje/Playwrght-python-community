import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

@pytest.fixture
def setup_login(page):
    login_page = LoginPage(page)
    credentials = login_page.get_user_credentials("standard_user")
    login_page.navigate()
    login_page.login(credentials["username"], credentials["password"])
    # Wait for inventory page to load completely
    page.wait_for_load_state('networkidle')
    page.wait_for_selector('.inventory_list')
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
    # Get initial product names for comparison
    initial_names = inventory_page.get_product_names()
    inventory_page.sort_products("za")
    # Get sorted product names
    sorted_names = inventory_page.get_product_names()
    # Verify sort worked
    assert sorted_names == sorted(initial_names, reverse=True)
    # Verify at least one product is present
    assert len(sorted_names) > 0

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