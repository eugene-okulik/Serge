from pages.categoty_page import CategoryPage
from playwright.sync_api import expect


def test_choose_steel_checkbox(page):
    category_page = CategoryPage(page)
    category_page.open_desks_category()
    category_page.click_steel_checkbox()
    expect(category_page.is_product_visible()).to_be_visible()


def test_add_to_cart(page):
    category_page = CategoryPage(page)
    category_page.open_desks_category()
    category_page.add_first_product_to_cart()

    expected_name = category_page.get_expected_product_name()
    actual_name = category_page.get_added_product_name()

    expect(actual_name).to_contain_text(expected_name)


def test_sort_by_name(page):
    category_page = CategoryPage(page)
    category_page.open_desks_category()
    category_page.sort_products_by_name()

    first_product_name = category_page.get_first_product_name_locator()
    expected_name = category_page.sort_by_name()

    expect(first_product_name).to_contain_text(expected_name)
