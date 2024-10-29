from time import sleep
from tests_tutors_web.locators import SignUp, Login
from tests_tutors_web.data import username, password

# links
signup_link = "http://195.133.27.184/signup/"
login_link = "http://195.133.27.184/login/"
main_page_link = "http://195.133.27.184/list/"


def test_create_acc(driver):
    driver.get(signup_link)
    driver.find_element(*SignUp.username).send_keys("TestUser_1")
    sleep(1)
    driver.find_element(*SignUp.password).send_keys("test5test78")
    driver.find_element(*SignUp.password_confirmation).send_keys("test5test78")
    driver.find_element(*SignUp.submit_button).click()
    # assert


def test_login(driver):
    driver.get(login_link)
    title = driver.find_element(*Login.title)
    assert title.is_displayed(), 'Page Incorrect'
    # assert driver.current_url == login_link, 'Not found'
    driver.find_element(*Login.username).send_keys(username)
    driver.find_element(*Login.password).send_keys(password)
    driver.find_element(*Login.submit_button).click()
    assert driver.current_url == main_page_link, 'Login Failed'
