from playwright.sync_api import Page

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.inventory_items = page.locator('.inventory_item')
        self.cart_badge = page.locator('.shopping_cart_badge')
        self.add_to_cart_buttons = page.locator('[data-test^="add-to-cart"]')
        self.remove_buttons = page.locator('[data-test^="remove"]')
        self.cart_link = page.locator('.shopping_cart_link')
        self.product_sort = page.locator('[data-test="product_sort_container"]')
        self.inventory_item_names = page.locator('.inventory_item_name')
        self.inventory_item_prices = page.locator('.inventory_item_price')

    def add_item_to_cart(self, item_name: str):
        item = self.page.locator(f'.inventory_item:has-text("{item_name}")')
        item.locator('[data-test^="add-to-cart"]').click()

    def remove_item_from_cart(self, item_name: str):
        item = self.page.locator(f'.inventory_item:has-text("{item_name}")')
        item.locator('[data-test^="remove"]').click()

    def get_cart_count(self) -> str:
        return self.cart_badge.text_content() if self.cart_badge.is_visible() else "0"

    def sort_products(self, sort_option: str):
        self.product_sort.select_option(sort_option)

    def get_product_names(self) -> list:
        return [name.text_content() for name in self.inventory_item_names.all()]

    def get_product_prices(self) -> list:
        return [price.text_content() for price in self.inventory_item_prices.all()]

    def go_to_cart(self):
        self.cart_link.click()