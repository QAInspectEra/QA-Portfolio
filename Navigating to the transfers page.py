# Navigating to the transfers page
transfers_link = driver.find_element(By.LINK_TEXT, "Transfers")
transfers_link.click()

# Entering transfer details
from_account = driver.find_element(By.ID, "from_account")
to_account = driver.find_element(By.ID, "to_account")
amount = driver.find_element(By.ID, "amount")

from_account.send_keys("123456789")
to_account.send_keys("987654321")
amount.send_keys("500")

# Clicking the transfer button
transfer_button = driver.find_element(By.ID, "transfer_button")
transfer_button.click()

# Checking if the transfer was successful
confirmation = driver.find_element(By.ID, "confirmation_message")
if "Transfer successful" in confirmation.text:
    print("Transfer completed successfully.")
else:
    print("Transfer failed.")
