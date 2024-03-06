from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

# Target URL
url = "https://test-zbgis2023.skgeodesy.sk/mkzbgis-76ad218b-8807-4c9e-9697-e534b77197a9/sk/zakladna-mapa/login?pos=48.800000,19.530000,8"

# Input variables
username = "bbrodian"
password = "Spinka75??"

# Webdriver initialization
driver = webdriver.Firefox()
driver.get(url)
sleep(8)

# Click on "window"
window_selector = ".mat-mdc-dialog-actions > button:nth-child(1) > span:nth-child(2)"
window = driver.find_element(By.CSS_SELECTOR, window_selector)
window.click()
sleep(2)

# Email input field
email_field_selector = "#mat-input-1"
email_field = driver.find_element(By.CSS_SELECTOR, email_field_selector)
email_field.send_keys(username)
sleep(3)

# Password input field
password_field_selector = "#mat-input-2"
password_field = driver.find_element(By.CSS_SELECTOR, password_field_selector)
password_field.send_keys(password)
sleep(3)

# Click on "Prihlasit"
prihlasit_button_selector = "button.mdc-button:nth-child(2) > span:nth-child(2)"
prihlasit_button = driver.find_element(By.CSS_SELECTOR, prihlasit_button_selector)
prihlasit_button.click()
sleep(3)

print("Logged in successfully")

driver.quit()
