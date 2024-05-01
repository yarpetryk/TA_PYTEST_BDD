from selenium.webdriver.common.by import By

class FormLocators:
    GENDER = (By.XPATH, '//*[contains(text(), "Male")]')
    NAME = (By.ID, 'Name')
    ADDRESS = (By.ID, 'Address')
    Zipcode = (By.ID, 'Zipcode___')
    CITY = (By.ID, 'city')
    PHONE = (By.ID, 'Phonenumbe')
    EMAIL = (By.ID, 'Email_addr')
    BIRTH = (By.ID, 'Date_of_bi')
    SUBMIT = (By.ID, 'btnSubmit')
    RESULT = (By.ID, 'set-viewport')
