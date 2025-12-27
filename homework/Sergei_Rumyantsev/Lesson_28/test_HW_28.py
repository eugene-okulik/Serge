from playwright.sync_api import Page


def test_auth(page: Page):
    page.goto('https://the-internet.herokuapp.com/')
    page.get_by_role("link", name="Form Authentication").click()
    page.get_by_role('textbox', name='username').fill("username")
    page.get_by_role("textbox", name='password').fill("password")
    page.get_by_role("button").click()


def test_reg_form(page: Page):
    page.goto('https://demoqa.com/automation-practice-form')
    page.get_by_placeholder('First Name').fill('TestName')
    page.get_by_placeholder('Last Name').fill('TestLastName')
    page.get_by_placeholder('name@example.com').fill('test@gmail.com')
    page.locator('#gender-radio-1').check(force=True)
    page.get_by_placeholder('Mobile Number').fill('0987654321')
    date_picker = page.locator("#dateOfBirthInput")
    date_picker.fill("01 Jan 2000")
    date_picker.press('Escape')
    subj = page.locator('#subjectsInput')
    subj.click()
    subj.press_sequentially('Arts', delay=50)
    subj.press('ArrowDown')
    subj.press('Enter')
    page.get_by_role("checkbox", name='Sports').check(force=True)
    page.get_by_placeholder('Current Address').fill('Moscow, ul.Pushkina, dom Kolotushkina, 132')
    select_state = page.locator('text=Select State')
    select_state.click()
    select_state.press('ArrowDown')
    select_state.press('Enter')
    select_city = page.locator('text=Select City')
    select_city.click()
    select_city.press('ArrowDown')
    select_city.press('Enter')
    page.locator('text=Submit').click()
