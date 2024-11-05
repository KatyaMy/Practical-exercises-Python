import allure

from tests_tutors_web.locators import Login
from tests_tutors_web.data import *
from tests_tutors_web.page_login import LoginPage

# links
signup_link = "http://195.133.27.184/signup/"
login_link = "http://195.133.27.184/login/"
main_page_link = "http://195.133.27.184/list/"


@allure.title("Login")
def test_login(driver):
    login_page = LoginPage(driver)
    login_page.sign_in()
    assert driver.current_url == main_page_link, 'Login Failed'


@allure.title('Incorrect login-user not found')
@allure.description('Negative test')
def test_incorrect_login(driver, wait):
    driver.get(login_link)
    title = driver.find_element(*Login.title)
    assert title.is_displayed(), 'Page Incorrect'
    driver.find_element(*Login.username).send_keys(incorrect_username)
    driver.find_element(*Login.password).send_keys(password)
    driver.find_element(*Login.submit_button).click()
    assert driver.current_url == main_page_link, 'User not found'


@allure.title('Incorrect login-MMS element is displayed')
@allure.description('Positive test--MMS element is displayed')
def test_incorrect_login_mms(driver, wait):
    driver.get(login_link)
    title = driver.find_element(*Login.title)
    assert title.is_displayed(), 'Page Incorrect'
    driver.find_element(*Login.username).send_keys(incorrect_username)
    driver.find_element(*Login.password).send_keys(password)
    driver.find_element(*Login.submit_button).click()
    element = driver.find_element(*Login.alert_mms)
    assert element.text == mms_login_alert, "Alert MMS element is not displayed"


def test_empty_filed_validation(driver, wait):
    driver.get(login_link)
    title = driver.find_element(*Login.title)
    assert title.is_displayed(), 'Page Incorrect'
    driver.find_element(*Login.username)
    driver.find_element(*Login.password)
    driver.find_element(*Login.submit_button).click()
    alert_mms_login = driver.find_element(*Login.alert_required_field_login).text
    alert_mms_password = driver.find_element(*Login.alert_required_filed_password).text
    assert alert_mms_login == mms_empty_login
    assert alert_mms_password == mms_empty_password
