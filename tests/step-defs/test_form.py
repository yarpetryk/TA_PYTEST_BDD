import allure

from pytest_bdd import scenario, given, when, then, parsers
from helpers import GenerateData
from pages.locators import FormLocators


# Initialization
faker = GenerateData

# Constants
URL = 'https://fd7.formdesk.com/demo/application2'

# Scenarios
@scenario('../features/form.feature', 'Apply the form')
def test_form():
    pass

# Given Steps
@given('go to webpage')
@allure.step('And go to web page')
def load_page(driver):
    driver.get(URL)

# When Steps
@when('select the gender')
@allure.step('And select the gender')
def select_gender(driver):
    driver.find_elements(*FormLocators.GENDER)[0].click()

@when('enter the name')
@allure.step('And enter the name')
def enter_name(driver):
    driver.find_element(*FormLocators.NAME).send_keys(faker.first_name())

@when('enter the address')
@allure.step('And enter the address')
def enter_address(driver):
    driver.find_element(*FormLocators.ADDRESS).send_keys(faker.address())

@when('enter the zip_code')
@allure.step('And enter the zip_code')
def enter_zip_code(driver):
    driver.find_element(*FormLocators.Zipcode).send_keys(faker.zip_code())

@when('enter the city')
@allure.step('And enter the city')
def enter_city(driver):
    driver.find_element(*FormLocators.CITY).send_keys(faker.city())

@when('enter the phone_number')
@allure.step('And enter the phone_number')
def enter_phone_number(driver):
    driver.find_element(*FormLocators.PHONE).send_keys(faker.phone_number())

@when('enter the email')
@allure.step('And enter the email')
def enter_email(driver):
    driver.find_element(*FormLocators.EMAIL).send_keys(faker.email())

@when('enter the birth_day')
@allure.step('And enter the birth_day')
def enter_birth_day(driver):
    driver.find_element(*FormLocators.BIRTH).send_keys(faker.birth_day())

@when('submit the form')
@allure.step('And submit the form')
def submit_form(driver):
    driver.find_element(*FormLocators.SUBMIT).click()

# Then Steps
@then(parsers.parse('page should contain {text}'))
@allure.step('And page should contain text')
def check_result(driver, text):
    actual_result = driver.find_element(*FormLocators.RESULT).text
    assert text in actual_result
