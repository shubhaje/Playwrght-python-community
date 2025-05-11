from playwright.sync_api import Page, expect

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.inventory_items = page.locator('.inventory_item')
        self.cart_badge = page.locator('.shopping_cart_badge')
        self.add_to_cart_buttons = page.locator('[data-test^="add-to-cart"]')
        self.remove_buttons = page.locator('[data-test^="remove"]')
        self.cart_link = page.locator('.shopping_cart_link')
        self.product_sort = page.locator('.product_sort_container')
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
        # Wait for product container and list to be ready
        self.page.wait_for_selector('.inventory_list', state='visible')
        self.page.wait_for_selector('.product_sort_container', state='visible')
        
        # Map sort options to dropdown values
        sort_map = {
            "az": "az",  # Name (A to Z)
            "za": "za",  # Name (Z to A)
            "lohi": "lohi",  # Price (low to high)
            "hilo": "hilo"  # Price (high to low)
        }
        
        if sort_option not in sort_map:
            raise ValueError(f"Invalid sort option: {sort_option}. Valid options are: {', '.join(sort_map.keys())}")
            
        # Select the sort option and wait for products to re-sort
        self.product_sort.select_option(sort_map[sort_option])
        self.page.wait_for_timeout(500)  # Brief wait for sort animation

    def get_product_names(self) -> list:
        return [name.text_content() for name in self.inventory_item_names.all()]

    def get_product_prices(self) -> list:
        return [price.text_content() for price in self.inventory_item_prices.all()]

    def go_to_cart(self):
        self.cart_link.click()