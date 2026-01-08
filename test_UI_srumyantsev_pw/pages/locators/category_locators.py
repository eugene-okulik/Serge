class CategoryPageLocators:
    STEEL_CHECKBOX = "input[name='attrib'][value='1-1']"

    PRODUCT_LINK = "//a[contains(@class, 'text-decoration-none')]"

    FIRST_PRODUCT = "(//td[@class='oe_product']//div[contains(@class,'o_wsale_product_grid_wrapper')])[1]"

    PRODUCTS = "//td[@class='oe_product']//div[contains(@class,'o_wsale_product_grid_wrapper')]"

    FIRST_PRODUCT_NAME = "div.o_wsale_product_information_text h6 a"

    SHOPPING_CART_BUTTON = "//input[@type='hidden'][@value='12']/following-sibling::a[@role='button']"

    PROCEED_TO_CHECKOUT_BUTTON = "//div[@role='dialog' and contains(@class,'show')]//button[.//span[normalize-space()='Proceed to Checkout']]"

    ADDED_PRODUCT_NAME = "h6.d-inline.align-top.h6.fw-bold"

    SORT_DROPDOWN_BUTTON = "//a[@role='button' and contains(@class, 'dropdown-toggle')][.//span[contains(normalize-space(),'Featured')]]"

    SORT_BY_NAME_OPTION = "//a[@role='menuitem' and contains(@class, 'dropdown-item')][.//span[contains(normalize-space(),'Name (A-Z)')]]"
