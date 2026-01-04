from playwright.sync_api import Page, expect, BrowserContext


def test_alert(page: Page):
    page.on('dialog', lambda alert: alert.accept())

    page.goto('https://www.qa-practice.com/elements/alert/confirm')
    page.locator('a[onclick*="confirm"]').click()
    result = page.locator('#result')
    result_text = page.locator('#result-text')
    expect(result).to_contain_text('You selected')
    expect(result_text).to_contain_text('Ok')


def test_enabled(page: Page, context: BrowserContext):
    page.goto('https://www.qa-practice.com/elements/new_tab/button')
    click_btn = page.locator('#new-page-button')
    with context.expect_page() as new_page_event:
        click_btn.click()
    new_page = new_page_event.value
    result = new_page.locator('#result-text')
    expect(result).to_have_text('I am a new page in a new tab')
    expect(click_btn).to_be_enabled()


def test_color_change(page: Page):
    page.goto('https://demoqa.com/dynamic-properties')
    change_btn = page.locator('#colorChange')
    expect(change_btn).to_have_css('color', 'rgb(220, 53, 69)')
    change_btn.click()
