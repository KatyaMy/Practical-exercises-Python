import allure
from time import sleep
from tests_tutors_web.locators import Login
from tests_tutors_web.data import *

# links
signup_link = "http://195.133.27.184/signup/"
login_link = "http://195.133.27.184/login/"
main_page_link = "http://195.133.27.184/list/"


@allure.title("Login")
def test_login(driver, wait):
    driver.get(login_link)
    title = driver.find_element(*Login.title)
    assert title.is_displayed(), 'Page Incorrect'
    # assert driver.current_url == login_link, 'Not found'
    driver.find_element(*Login.username).send_keys(username)
    driver.find_element(*Login.password).send_keys(password)
    driver.find_element(*Login.submit_button).click()
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
