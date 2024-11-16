from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

ids_to_find = ['xhkVEkgm', 'QCg2vOX7', '8KvuO5ja', 'CFoCZ3Ze', '8CiPCnNB', 'XuEMunrz', 'vmlzQ3gH', 'axhUiw2I',
               'jolHZqD1', 'ZM6Ms3tw', '25a2X14r', 'aOSMX9tb', 'YySk7Ze3', 'QQK13iyY', 'j7kD7uIR']


def test(driver, wait):
    driver.get("https://parsinger.ru/selenium/5.9/3/index.html")
    for idd in ids_to_find:
        element = wait.until(
            EC.visibility_of_element_located((By.ID, idd))
        )
        element.click()

    alert = WebDriverWait(driver, 10).until(
        EC.alert_is_present()
    )
    print(alert.text)
