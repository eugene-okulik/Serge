class ProductPageLocators:

    PRODUCT_UNAVAILABLE = "#product_unavailable"
    PRODUCT_UNAVAILABLE_TEXT = "//div[@id='product_unavailable']//h3"

    ADD_ONE_BUTTON = "//a[@title='Add one' and contains(@class, 'js_add_cart_json')]"

    REMOVE_ONE_BUTTON = "//a[@title='Remove one' and contains(@class, 'js_add_cart_json')]"

    QUANTITY_INPUT = "input.quantity.text-center[name='add_qty']"

    ADD_TO_CART_BUTTON = "//a[@id='add_to_cart' and @role='button' and contains(@class, 'js_check_product')]"

    CART_QUANTITY_BADGE = "sup.my_cart_quantity.badge"

    CART_BUTTON = "//a[@aria-label='eCommerce cart' and contains(@class, 'o_navlink_background')]"

    PRODUCT_NAME_IN_CART = "//h6[@class='d-inline align-top h6 fw-bold' and normalize-space()='Office Design Software']"

    QUANTITY_IN_CART = "div[name='website_sale_cart_line_quantity'] input.js_quantity"

    TERMS_LINK = "text=Terms and Conditions"

    PINTEREST_BUTTON = ".s_share_pinterest"
