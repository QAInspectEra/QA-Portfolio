from selenium import webdriver
from selenium.webdriver.common.by import By
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

# Navigate to the deposit page
deposit_link = driver.find_element(By.LINK_TEXT, "Deposit")
deposit_link.click()

# Enter deposit details
account = driver.find_element(By.ID, "account")
amount = driver.find_element(By.ID, "amount")

account.send_keys("123456789")
amount.send_keys("1000")

# Click the deposit button
deposit_button = driver.find_element(By.ID, "deposit_button")
deposit_button.click()

# Check if the deposit was successful
confirmation = driver.find_element(By.ID, "confirmation_message")
if "Deposit successful" in confirmation.text:
    print("Deposit completed successfully.")
else:
    print("Deposit failed.")
