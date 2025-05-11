import pytest
from pages.login_page import LoginPage
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

@pytest.mark.smoke
def test_valid_login(page):
    login_page = LoginPage(page)
    # You can specify environment explicitly
    credentials = login_page.get_user_credentials("standard_user", "SIT")
    login_page.navigate()
    login_page.login(credentials["username"], credentials["password"])
    
    assert page.url == "https://www.saucedemo.com/inventory.html"
    assert page.locator('.title').text_content() == "Products"

@pytest.mark.smoke
def test_locked_out_user(page):
    login_page = LoginPage(page)
    # Or use environment variable (will use DEFAULT_ENV if not set)
    credentials = login_page.get_user_credentials("locked_out_user")
    login_page.navigate()
    login_page.login(credentials["username"], credentials["password"])
    
    error_message = login_page.get_error_message()
    assert "Epic sadface: Sorry, this user has been locked out" in error_message

@pytest.mark.regression
def test_problem_user_uat(page):
    login_page = LoginPage(page)
    # Test with UAT environment
    credentials = login_page.get_user_credentials("problem_user", "UAT")
    login_page.navigate()
    login_page.login(credentials["username"], credentials["password"])
    
    assert page.url == "https://www.saucedemo.com/inventory.html"
    assert page.locator('.title').text_content() == "Products"
    
@pytest.mark.regression
def test_performance_glitch_user(page):
    login_page = LoginPage(page)
    credentials = login_page.get_user_credentials("performance_glitch_user")
    login_page.navigate()
    login_page.login(credentials["username"], credentials["password"])
    
    assert page.url == "https://www.saucedemo.com/inventory.html"
    assert page.locator('.title').text_content() == "Products"

@pytest.mark.smoke
def test_invalid_credentials(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("invalid_user", "wrong_password")
    
    error_message = login_page.get_error_message()
    assert "Epic sadface: Username and password do not match" in error_message

@pytest.mark.regression
def test_error_user(page):
    login_page = LoginPage(page)
    credentials = login_page.get_user_credentials("error_user")
    login_page.navigate()
    login_page.login(credentials["username"], credentials["password"])
    
    assert page.url == "https://www.saucedemo.com/inventory.html"
    assert page.locator('.title').text_content() == "Products"

@pytest.mark.regression
def test_visual_user(page):
    login_page = LoginPage(page)
    credentials = login_page.get_user_credentials("visual_user")
    login_page.navigate()
    login_page.login(credentials["username"], credentials["password"])
    
    assert page.url == "https://www.saucedemo.com/inventory.html"
    assert page.locator('.title').text_content() == "Products"