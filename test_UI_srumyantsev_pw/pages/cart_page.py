from pages.base_page import BasePage
from pages.locators.cart_locators import CartPageLocators


class CartPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.url = 'http://testshop.qa-practice.com/shop/cart'

    def open_cart(self):
        self.open(self.url)
        self.wait_for_page_ready()

    def get_empty_cart_locator(self):
        return self.page.locator(CartPageLocators.EMPTY_CART_MESSAGE)

    def open_search(self):
        self.click(CartPageLocators.SEARCH_BUTTON)
        self.page.locator(CartPageLocators.SEARCH_INPUT).wait_for(state="visible")

    def search_product(self, product_name):
        self.open_search()
        self.send_keys(CartPageLocators.SEARCH_INPUT, product_name)
        self.page.locator(CartPageLocators.SEARCH_RESULT_ITEM).wait_for(state="visible")

    def click_first_search_result(self):
        self.click(CartPageLocators.SEARCH_RESULT_ITEM)

    def hover_categories_dropdown(self):
        self.page.locator(CartPageLocators.CATEGORIES_DROPDOWN).hover()

    def get_dropdown_menu_items(self):
        self.hover_categories_dropdown()
        self.page.locator(CartPageLocators.DROPDOWN_MENU_ITEMS).first.wait_for(state="visible")
        return self.page.locator(CartPageLocators.DROPDOWN_MENU_ITEMS).all()

    def get_items(self):
        self.hover_categories_dropdown()
        return self.page.locator(CartPageLocators.DROPDOWN_MENU_ITEMS)
