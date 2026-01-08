from pages.cart_page import CartPage
from playwright.sync_api import expect


def test_cart_is_empty_by_default(page):
    cart_page = CartPage(page)
    cart_page.open_cart()
    expect(cart_page.get_empty_cart_locator()).to_have_text('Your cart is empty!')


def test_search_in_cart(page):
    cart_page = CartPage(page)
    cart_page.open_cart()
    cart_page.search_product("Corner Desk Left Sit")
    cart_page.click_first_search_result()
    expected_url = 'http://testshop.qa-practice.com/shop/furn-1118-corner-desk-left-sit-18'

    expect(page).to_have_url(expected_url)


def test_check_items_in_categories_dropdown_in_cart(page):
    cart_page = CartPage(page)
    cart_page.open_cart()
    expect(cart_page.get_items()).to_have_count(2)
    expect(cart_page.get_items()).to_have_text(["Desks", "Furnitures"])
