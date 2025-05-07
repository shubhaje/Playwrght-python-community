import pytest
from pages.login_page import LoginPage
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
@pytest.mark.smoke
def test_valid_login(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    
    # Assert successful login by checking the URL
    assert page.url == "https://www.saucedemo.com/inventory.html"
    # Additional assertion to verify we're on the products page
    assert page.locator('.title').text_content() == "Products"

@pytest.mark.smoke
def test_locked_out_user(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("locked_out_user", "secret_sauce")
    
    # Assert error message for locked out user
    error_message = login_page.get_error_message()
    assert "Epic sadface: Sorry, this user has been locked out" in error_message

@pytest.mark.regression
def test_problem_user(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("problem_user", "secret_sauce")
    
    # Assert successful login by checking the URL
    assert page.url == "https://www.saucedemo.com/inventory.html"
    # Verify we're on the products page
    assert page.locator('.title').text_content() == "Products"
    
@pytest.mark.regression
def test_performance_glitch_user(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("performance_glitch_user", "secret_sauce")
    
    # Assert successful login by checking the URL
    assert page.url == "https://www.saucedemo.com/inventory.html"
    # Verify we're on the products page
    assert page.locator('.title').text_content() == "Products"

@pytest.mark.smoke
def test_invalid_credentials(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("invalid_user", "wrong_password")
    
    # Assert error message for invalid credentials
    error_message = login_page.get_error_message()
    assert "Epic sadface: Username and password do not match" in error_message

@pytest.mark.regression
def test_error_user(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("error_user", "secret_sauce")
    
    # Assert successful login by checking the URL
    assert page.url == "https://www.saucedemo.com/inventory.html"
    # Verify we're on the products page
    assert page.locator('.title').text_content() == "Products"

@pytest.mark.regression
def test_visual_user(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("visual_user", "secret_sauce")
    
    # Assert successful login by checking the URL
    assert page.url == "https://www.saucedemo.com/inventory.html"
    # Verify we're on the products page
    assert page.locator('.title').text_content() == "Products"