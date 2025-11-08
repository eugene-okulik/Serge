from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_customer_flow():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(5)

    driver.get('http://testshop.qa-practice.com/')
    cust_desk = driver.find_element(By.XPATH, "//a[text()='Customizable Desk']")
    ActionChains(driver).key_down(Keys.CONTROL).click(cust_desk).key_up(Keys.CONTROL).perform()
    tab = driver.window_handles
    driver.switch_to.window(tab[1])
    add_to_cart = driver.find_element(By.ID, "add_to_cart")
    wait = WebDriverWait(driver, 10)
    wait.until(lambda _: add_to_cart.is_displayed() and add_to_cart.is_enabled())
    ActionChains(driver).move_to_element(add_to_cart).click(add_to_cart).perform()
    wait = WebDriverWait(driver, 15)
    wait.until(
        lambda d: d.find_element(
            By.XPATH,
            "//div[@role='dialog' and contains(@class,'show') and @aria-modal='true']"
        )
    )
    cont_btn = wait.until(lambda d: d.find_element(
        By.XPATH,
        "//div[@role='dialog' and contains(@class,'show')]"
        "//button[.//span[normalize-space()='Continue Shopping']]"
    ))
    ActionChains(driver).move_to_element(cont_btn).pause(1).click(cont_btn).perform()

    driver.close()
    driver.switch_to.window(tab[0])
    wait = WebDriverWait(driver, 10)
    wait.until(lambda d: "Customizable Desk" in d.page_source or d.find_element(By.TAG_NAME, "body").is_displayed())
    cart_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/shop/cart']"))
    )
    cart_button.click()
    added_dest = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "h6.d-inline.align-top.h6.fw-bold"))
    )
    assert "Customizable Desk" in added_dest.text
    print("Тест пройден")


test_customer_flow()


def test_popup():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(5)

    driver.get('http://testshop.qa-practice.com/')
    product_name = driver.find_element(
        By.XPATH, "//a[contains(@class, 'text-decoration-none') and @content='Customizable Desk']"
    )
    product_cart = driver.find_element(
        By.XPATH,
        "//img[@itemprop='image' and contains(@class, 'img-fluid') and @alt='Customizable Desk']"
    )
    ActionChains(driver).move_to_element(product_cart).perform()
    driver.find_element(By.XPATH, "//a[@aria-label='Shopping cart']").click()
    wait = WebDriverWait(driver, 15)
    wait.until(
        lambda d: d.find_element(By.XPATH, "//div[contains(@class, 'modal-dialog')]"))
    product_full_name = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//strong[contains(@class, 'product_display_name')]"))
    )
    assert product_name.text in product_full_name.text
    print(f'"Тест пройден", Имя товара: {product_name.text}')


test_popup()
