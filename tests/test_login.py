from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Chrome options
options = webdriver.ChromeOptions()
options.add_argument("--headless")  

# Setup driver
service = Service(ChromeDriverManager().install())
time.sleep(2)
driver = webdriver.Chrome(service=service, options=options)
time.sleep(2)

driver.get("http://127.0.0.1:5050")
time.sleep(2)

wait = WebDriverWait(driver, 10)
username_field = wait.until(EC.presence_of_element_located((By.NAME, "username")))
password_field = driver.find_element(By.NAME, "password")

time.sleep(2)
username_field.send_keys("admin")
time.sleep(2)
password_field.send_keys("secret")
time.sleep(2)
password_field.send_keys(Keys.RETURN)

time.sleep(10)

body_text = driver.find_element(By.TAG_NAME, "body").text
assert "Login successful!" in body_text

print("Test Passed")

driver.quit()
