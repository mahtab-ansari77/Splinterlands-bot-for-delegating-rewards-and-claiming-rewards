import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Define usernames, password = posting key, and keys = private keys
credentials = [
    {"username": "your_username", "password": "your_posting_key", "key": "your_private_key"},
    {"username": "your_username", "password": "your_posting_key", "key": "your_private_key"},
    {"username": "your_username", "password": "your_posting_key", "key": "your_private_key"},
    {"username": "your_username", "password": "your_posting_key", "key": "your_private_key"},
    {"username": "your_username", "password": "your_posting_key", "key": "your_private_key"}
]

#you can add many accounts above.

#for login
def perform_login(driver, username, password):
    print(f"Logging in as: {username}")
    driver.find_element(By.XPATH, "//button[text()='Log In']").click()
    driver.implicitly_wait(10)
    driver.find_element(By.CSS_SELECTOR, "input[placeholder='EMAIL / USERNAME']").send_keys(username)
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.XPATH, "//button[@type = 'submit']").click()
    time.sleep(15)
    driver.refresh()
    time.sleep(10)

#this is for sps claiming
def reward_claim(driver):
    driver.find_element(By.XPATH, "//div[text()='SPLINTERSHARDS']").click()
    time.sleep(4)
    driver.find_element(By.XPATH, "//button[text()='Claim All']").click()
    time.sleep(10)

#this is for sps dashboard
def perform_action(driver):
    driver.find_element(By.CSS_SELECTOR, ".sps-container").click()
    time.sleep(4)
    driver.find_element(By.XPATH, "//button[text()='REWARD DELEGATIONS']").click()
    time.sleep(10)


#this is for remove sps delegation
def remove_delegation(driver, key):
    driver.find_element(By.XPATH, "//button[text()='REMOVE ALL']").click()
    driver.find_element(By.CSS_SELECTOR, ".c-igOdUr").send_keys(key)
    driver.find_element(By.XPATH, "//button[text()='APPROVE TRANSACTION']").click()
    time.sleep(10)

#this is for delegation update
def perform_transaction(driver, target_user, amount, key):
    driver.find_element(By.XPATH, "//input[@type = 'text']").send_keys(target_user)
    driver.find_element(By.XPATH, "//input[@type = 'number']").send_keys(amount)
    driver.find_element(By.XPATH, "//button[text()='UPDATE']").click()
    driver.find_element(By.CSS_SELECTOR, ".c-igOdUr").send_keys(key)
    driver.find_element(By.XPATH, "//button[text()='APPROVE TRANSACTION']").click()
    time.sleep(10)

def logout(driver):
    driver.find_element(By.CSS_SELECTOR, ".c-evEMnK").click()
    driver.find_element(By.LINK_TEXT, "Log Out").click()
    print(f"{cred['username']} logout")
    time.sleep(10)

service_obj = Service("D:/chromedriver.exe")   #add your chrome webdriver path here
driver = webdriver.Chrome(service=service_obj)
driver.get("https://splinterlands.com/")
driver.maximize_window()


for cred in credentials:
    perform_login(driver, cred["username"], cred["password"])
    perform_action(driver)
    remove_delegation(driver, cred["key"])
    perform_transaction(driver, "mahtabansari370", "100", cred["key"])
    reward_claim(driver)
    logout(driver)

driver.quit()
