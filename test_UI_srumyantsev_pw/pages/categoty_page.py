from pages.base_page import BasePage
from pages.locators.category_locators import CategoryPageLocators
from time import sleep


class CategoryPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.base_url = 'http://testshop.qa-practice.com/shop/category/'

    def open_category(self, category_slug):
        url = f"{self.base_url}{category_slug}"
        self.open(url)
        self.wait_for_page_ready()

    def open_desks_category(self):
        self.open_category('desks-1')

    def click_steel_checkbox(self):
        self.click_first(CategoryPageLocators.STEEL_CHECKBOX)

    def is_product_visible(self):
        return self.page.locator(CategoryPageLocators.PRODUCT_LINK)

    def hover_over_product(self, locator):
        self.page.locator(locator).hover()

    def hover_over_customizable_desk(self):
        self.hover_over_product(CategoryPageLocators.CUSTOMIZABLE_DESK_IMAGE)

    def click_proceed_to_checkout(self):
        proceed_btn = self.page.locator(CategoryPageLocators.PROCEED_TO_CHECKOUT_BUTTON)
        proceed_btn.hover()
        self.page.wait_for_timeout(1000)
        proceed_btn.click()

    def get_added_product_name(self):
        return self.page.locator(CategoryPageLocators.ADDED_PRODUCT_NAME)

    def add_product_to_cart(self):
        self.page.locator(CategoryPageLocators.SHOPPING_CART_BUTTON).click()

    def open_sort_dropdown(self):
        self.click(CategoryPageLocators.SORT_DROPDOWN_BUTTON)

    def select_sort_by_name(self):
        self.click(CategoryPageLocators.SORT_BY_NAME_OPTION)

    def sort_products_by_name(self):
        self.open_sort_dropdown()
        self.select_sort_by_name()

    def get_first_product_name_locator(self):
        first_product = self.page.locator(CategoryPageLocators.FIRST_PRODUCT)
        name_element = first_product.locator(CategoryPageLocators.FIRST_PRODUCT_NAME)
        return name_element

    def get_first_product_name(self):
        first_product = self.page.locator(CategoryPageLocators.FIRST_PRODUCT)
        name_element = first_product.locator(CategoryPageLocators.FIRST_PRODUCT_NAME)
        return name_element.text_content()

    def hover_over_first_product(self):
        card = self.page.locator(CategoryPageLocators.FIRST_PRODUCT_NAME).nth(0)
        card.hover()
        btn = self.page.locator(CategoryPageLocators.SHOPPING_CART_BUTTON)
        btn.click()

    def add_first_product_to_cart(self):
        self._first_product_name = self.get_first_product_name()
        self.hover_over_first_product()
        self.click_proceed_to_checkout()
        self.wait_for_cart_page_loaded()

    def get_expected_product_name(self):
        return self._first_product_name

    def wait_for_cart_page_loaded(self):
        self.page.locator(CategoryPageLocators.ADDED_PRODUCT_NAME).wait_for(state="attached")

    def sort_by_name(self):
        self.page.locator(CategoryPageLocators.PRODUCTS).first.wait_for(state='visible')
        products = self.find_elements(CategoryPageLocators.PRODUCTS)
        products_list = [product.text_content() for product in products]
        products_list.sort()
        step = products_list[0]
        splitted = step.split('\n')
        result = splitted[0]
        return result
