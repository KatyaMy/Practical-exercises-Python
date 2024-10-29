from selenium.webdriver.common.by import By


# locators
class SignUp:
    username = By.ID, 'id_username'
    password = By.ID, 'id_password1'
    password_confirmation = By.ID, 'id_password2'
    submit_button = By.CSS_SELECTOR, '[type="submit"]'


class Login:
    username = By.ID, 'id_username'
    password = By.ID, 'id_password'
    submit_button = By.CSS_SELECTOR, '[type="submit"]'
    title = By.XPATH, '//*[@class="text-center"]'