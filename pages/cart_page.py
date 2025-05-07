from playwright.sync_api import Page

class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.cart_items = page.locator('.cart_item')
        self.cart_item_names = page.locator('.inventory_item_name')
        self.cart_item_prices = page.locator('.inventory_item_price')
        self.remove_buttons = page.locator('[data-test^="remove"]')
        self.checkout_button = page.locator('[data-test="checkout"]')
        self.continue_shopping_button = page.locator('[data-test="continue-shopping"]')

    def get_cart_items(self) -> list:
        return [item.text_content() for item in self.cart_item_names.all()]

    def get_item_prices(self) -> list:
        return [price.text_content() for price in self.cart_item_prices.all()]

    def remove_item(self, item_name: str):
        item = self.page.locator(f'.cart_item:has-text("{item_name}")')
        item.locator('[data-test^="remove"]').click()

    def checkout(self):
        self.checkout_button.click()

    def continue_shopping(self):
        self.continue_shopping_button.click()

    def get_cart_count(self) -> int:
        return len(self.cart_items.all())