from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Первое задание
def test_input_text():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(5)

    driver.get('https://www.qa-practice.com/elements/input/simple')
    text_string = driver.find_element(By.ID, 'id_text_string')
    text_string.send_keys('ForTest')
    text_string.send_keys(Keys.ENTER)

    result_text = driver.find_element(By.ID, 'result-text')
    assert result_text.text == 'ForTest'
    print('Тест пройден!')


test_input_text()


def test_few_inputs():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get('https://demoqa.com/automation-practice-form')
    name_field = driver.find_element(By.ID, 'firstName')
    name_field.send_keys('Test')
    last_name_field = driver.find_element(By.ID, 'lastName')
    last_name_field.send_keys('Testovikh')
    email_field = driver.find_element(By.ID, 'userEmail')
    email_field.send_keys('testovich@test.test')
    gender_radiobutton = driver.find_element(By.XPATH, "//label[text()='Male']")
    gender_radiobutton.click()
    phone_number_field = driver.find_element(By.ID, 'userNumber')
    phone_number_field.send_keys('9999999999')

    date_of_birth_field = driver.find_element(By.ID, 'dateOfBirthInput')
    date_of_birth_field.click()
    driver.find_element(
        By.CSS_SELECTOR,
        ".react-datepicker__year-select"
    ).click()
    driver.find_element(
        By.CSS_SELECTOR,
        ".react-datepicker__year-select option[value='2025']"
    ).click()
    driver.find_element(
        By.CSS_SELECTOR,
        ".react-datepicker__month-select"
    ).click()
    driver.find_element(
        By.CSS_SELECTOR,
        ".react-datepicker__month-select option[value='10']"
    ).click()
    driver.find_element(
        By.XPATH,
        "//div[contains(@class,'react-datepicker__day') and text()='31']"
    ).click()
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    subject_input = driver.find_element(By.CSS_SELECTOR, "[class*='subjects-auto-complete__value-container'] input")
    subject_input.send_keys("a")
    driver.find_element(
        By.XPATH, "//div[text()='Arts']").click()
    driver.find_element(
        By.CSS_SELECTOR,
        "label[for='hobbies-checkbox-3']"
    ).click()
    current_address_field = driver.find_element(By.ID, 'currentAddress')
    current_address_field.send_keys('Moscow, ul.Pushkina, dom Kolotushkina')
    driver.find_element(
        By.XPATH,
        "//div[text()='Select State']"
    ).click()
    driver.find_element(
        By.XPATH,
        "//div[contains(@class,'option') and text()='Haryana']"
    ).click()
    driver.find_element(
        By.XPATH,
        "//div[text()='Select City']").click()
    driver.find_element(
        By.XPATH,
        "//div[contains(@class,'option') and text()='Karnal']"
    ).click()
    submit_button = driver.find_element(By.ID, 'submit')
    submit_button.click()
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".modal-content"))
    )

    WebDriverWait(driver, 5).until(
        lambda d: d.find_element(
            By.XPATH,
            "//td[text()='Student Name']/following-sibling::td"
            ).text.strip() != ""
    )

    expected_name = "Test Testovikh"
    expected_email = "testovich@test.test"
    expected_gender = "Male"
    expected_mobile = "9999999999"
    expected_dob = "31 October,2025"
    expected_subjects = "Arts"
    expected_hobbies = "Music"
    expected_picture = ""
    expected_address = "Moscow, ul.Pushkina, dom Kolotushkina"
    expected_state_city = "Haryana Karnal"

    actual_name = driver.find_element(
        By.XPATH,
        "//td[text()='Student Name']/following-sibling::td"
    ).text
    actual_email = driver.find_element(
        By.XPATH,
        "//td[text()='Student Email']/following-sibling::td"
    ).text
    actual_gender = driver.find_element(
        By.XPATH,
        "//td[text()='Gender']/following-sibling::td"
    ).text
    actual_mobile = driver.find_element(
        By.XPATH,
        "//td[text()='Mobile']/following-sibling::td"
    ).text
    actual_dob = driver.find_element(
        By.XPATH,
        "//td[text()='Date of Birth']/following-sibling::td"
    ).text
    actual_subjects = driver.find_element(
        By.XPATH,
        "//td[text()='Subjects']/following-sibling::td"
    ).text
    actual_hobbies = driver.find_element(
        By.XPATH,
        "//td[text()='Hobbies']/following-sibling::td"
    ).text
    actual_picture = driver.find_element(
        By.XPATH,
        "//td[text()='Picture']/following-sibling::td"
    ).text
    actual_address = driver.find_element(
        By.XPATH,
        "//td[text()='Address']/following-sibling::td"
    ).text
    actual_state_city = driver.find_element(
        By.XPATH,
        "//td[text()='State and City']/following-sibling::td"
    ).text

    print("\n--- РЕЗУЛЬТАТЫ СРАВНЕНИЯ ---")
    print(f"Name:        Expected: '{expected_name}' | Actual: '{actual_name}'")
    print(f"Email:       Expected: '{expected_email}' | Actual: '{actual_email}'")
    print(f"Gender:      Expected: '{expected_gender}' | Actual: '{actual_gender}'")
    print(f"Mobile:      Expected: '{expected_mobile}' | Actual: '{actual_mobile}'")
    print(f"DOB:         Expected: '{expected_dob}' | Actual: '{actual_dob}'")
    print(f"Subjects:    Expected: '{expected_subjects}' | Actual: '{actual_subjects}'")
    print(f"Hobbies:     Expected: '{expected_hobbies}' | Actual: '{actual_hobbies}'")
    print(f"Picture:     Expected: '{expected_picture}' | Actual: '{actual_picture}'")
    print(f"Address:     Expected: '{expected_address}' | Actual: '{actual_address}'")
    print(f"State/City:  Expected: '{expected_state_city}' | Actual: '{actual_state_city}'")
    print("-----------------------------------\n")

    assert actual_name == expected_name
    assert actual_email == expected_email
    assert actual_gender == expected_gender
    assert actual_mobile == expected_mobile
    assert actual_dob == expected_dob
    assert actual_subjects == expected_subjects
    assert actual_hobbies == expected_hobbies
    assert actual_picture == expected_picture
    assert actual_address == expected_address
    assert actual_state_city == expected_state_city

    print("Тест пройден!")


test_few_inputs()


def choose_language():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(5)

    driver.get('https://www.qa-practice.com/elements/select/single_select')

    lang_dropdown = driver.find_element(By.ID, "id_choose_language")
    select = Select(lang_dropdown)
    select.select_by_visible_text("Ruby")
    selected = select.first_selected_option.text
    assert selected == "Ruby"
    print("Выбранный язык:", selected)
    print("Тест пройден!")


choose_language()


def start_button():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(5)

    driver.get('https://the-internet.herokuapp.com/dynamic_loading/2')
    driver.find_element(By.XPATH, "//button[text()='Start']").click()
    hello_text = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//h4[text()='Hello World!']"))
    )

    print("Текст:", hello_text.text)
    print("Тест пройден!")


start_button()
