from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize Chrome WebDriver
driver = webdriver.Chrome(executable_path='path_to_chromedriver')

# Open the bank application page
driver.get('https://yourbankapp.com')

# Enter login credentials
username = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID, "password")

username.send_keys("test_user")
password.send_keys("test_password")

# Click the login button
login_button = driver.find_element(By.ID, "login_button")
login_button.click()

# Check if login was successful
try:
    dashboard = driver.find_element(By.ID, "dashboard")
    print("Login successful.")
except:
    print("Login failed.")
