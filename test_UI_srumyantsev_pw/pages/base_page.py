from playwright.sync_api import Page, TimeoutError as PlaywrightTimeoutError


class BasePage:

    def __init__(self, page: Page):
        self.page = page

    def open(self, url):
        self.page.goto(url)

    def find_element(self, locator):
        return self.page.locator(locator)

    def find_elements(self, locator):
        return self.page.locator(locator).all()

    def click(self, locator):
        self.page.locator(locator).click()

    def click_first(self, locator):
        self.page.locator(locator).first.click()

    def get_text(self, locator):
        return self.page.locator(locator).text_content()

    def send_keys(self, locator, text):
        element = self.page.locator(locator)
        element.clear()
        element.fill(text)

    def is_visible(self, locator):
        try:
            self.page.locator(locator).wait_for(state="visible")
            return True
        except PlaywrightTimeoutError:
            return False

    def wait_for_page_ready(self):
        self.page.wait_for_load_state("networkidle")

    def get_current_url(self):
        return self.page.url

    def is_visible_fast(self, locator, timeout=2):
        try:
            self.page.locator(locator).wait_for(state="visible", timeout=timeout * 1000)
            return True
        except PlaywrightTimeoutError:
            return False

    def is_element_hidden(self, locator):
        try:
            element = self.page.locator(locator)
            classes = element.get_attribute("class") or ""
            return "d-none" in classes
        except PlaywrightTimeoutError:
            return False
