from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome('path/to/chromedriver')


driver.get('http://125.26.15.143:13132/')

username_input = driver.find_element(By.ID, 'username')
username_input.send_keys('oz4899')
password_input = driver.find_element(By.ID, 'password')
password_input.send_keys('1234')


login_button = driver.find_element(By.XPATH, '//button[contains(text(), "Login")]')
login_button.click()

wait = WebDriverWait(driver, 10)
welcome_message = wait.until(EC.visibility_of_element_located((By.XPATH, '//h1[contains(text(), "Welcome")]')))


if welcome_message.is_displayed():
    print("Login successful!")
else:
    print("Login failed.")
driver.quit()