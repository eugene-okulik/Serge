import pytest
from pages.base_page import BasePage
from pages.locators.product_locators import ProductPageLocators
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError
from time import sleep


class ProductPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.base_url = 'http://testshop.qa-practice.com/shop/'

    def is_product_available(self):
        return self.is_element_hidden(ProductPageLocators.PRODUCT_UNAVAILABLE)

    def skip_if_unavailable(self):
        if not self.is_product_available():
            message = "Product is not available for sale"
            try:
                unavailable_text = self.get_text(ProductPageLocators.PRODUCT_UNAVAILABLE_TEXT)
                message = f"Product unavailable: {unavailable_text}"
            except PlaywrightTimeoutError:
                pass
            pytest.skip(message)

    def open_product(self, product_slug):
        url = f"{self.base_url}{product_slug}"
        self.open(url)
        self.wait_for_page_ready()

    def open_office_design_software(self):
        self.open_product('furn-9999-office-design-software-7?category=9')

    def click_add_one(self, times=1):
        for _ in range(times):
            self.click(ProductPageLocators.ADD_ONE_BUTTON)

    def click_add_to_cart(self):
        self.click_first(ProductPageLocators.ADD_TO_CART_BUTTON)

    def wait_for_cart_badge_quantity(self, expected_quantity):
        wait = self.page.locator(ProductPageLocators.CART_QUANTITY_BADGE)
        wait.first.filter(has_text=str(expected_quantity)).wait_for(state="attached")

    def click_cart_button(self):
        self.click_first(ProductPageLocators.CART_BUTTON)

    def get_product_name_in_cart(self):
        return self.page.locator(ProductPageLocators.PRODUCT_NAME_IN_CART)

    def get_quantity_in_cart(self):
        return self.page.locator(ProductPageLocators.QUANTITY_IN_CART)

    def add_multiple_items_to_cart(self, quantity):
        self.click_add_one(times=quantity - 1)

        self.click_add_to_cart()

        self.wait_for_cart_badge_quantity(quantity)

    def click_terms_and_conditions(self):
        self.click(ProductPageLocators.TERMS_LINK)

    def click_pinterest_button(self):
        self.click(ProductPageLocators.PINTEREST_BUTTON)

    def click_pinterest_button_and_switch(self):
        with self.page.context.expect_page() as new_page_info:
            self.click_pinterest_button()
        new_page = new_page_info.value
        new_page.wait_for_load_state()
        return new_page
