from pages.product_page import ProductPage
from playwright.sync_api import expect
import re


def test_add_to_cart_several_items_of_product(page):
    product_page = ProductPage(page)
    product_page.open_office_design_software()

    product_page.skip_if_unavailable()

    product_page.add_multiple_items_to_cart(quantity=6)
    product_page.click_cart_button()

    product_name = product_page.get_product_name_in_cart()
    quantity_in_cart = product_page.get_quantity_in_cart()

    expect(quantity_in_cart).to_have_value('6')
    expect(product_name).to_contain_text("Office Design Software")


def test_redirect_to_terms_and_conditions(page):
    product_page = ProductPage(page)
    product_page.open_office_design_software()

    product_page.skip_if_unavailable()

    product_page.click_terms_and_conditions()

    expected_url = 'http://testshop.qa-practice.com/terms'

    expect(page).to_have_url(expected_url)


def test_redirect_to_pinterest(page):
    product_page = ProductPage(page)
    product_page.open_office_design_software()

    product_page.skip_if_unavailable()
    new_url = product_page.click_pinterest_button_and_switch()

    expect(new_url).to_have_url(re.compile(r'pinterest.com/pin/create/button'))
