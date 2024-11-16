import allure
from tests_tutors_web.locators import SignUp, TutorProfile
from tests_tutors_web.pages.registration_page import fill_signup_form
from tests_tutors_web.config import WEB_USERNAME, WEB_PASSWORD, T_PASSWORD, T_NAME


# links
signup_link = "http://195.133.27.184/signup/"
login_link = "http://195.133.27.184/login/"
main_page_link = "http://195.133.27.184/list/"


@allure.title("Create account for user")
def test_create_acc_user(driver, wait):
    fill_signup_form(driver, username=WEB_USERNAME, password=WEB_PASSWORD)
    btn_out = driver.find_elements(*SignUp.btn_logout)
    # assert len(btn_out) == 1, 'Registration is failed'
    assert btn_out[0].is_displayed(), 'Registration is failed'


@allure.title("Create account for teacher")
def test_create_acc_teacher(driver, wait):
    fill_signup_form(driver, username=T_NAME, password=T_PASSWORD, check_terms=True)
    btn_create_case = driver.find_elements(*TutorProfile.create_case)
    assert btn_create_case[0].is_displayed(), 'Registration is failed'

