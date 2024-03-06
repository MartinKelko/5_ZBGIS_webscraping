from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

# Target URL
url = "https://test-zbgis2023.skgeodesy.sk/mkzbgis-76ad218b-8807-4c9e-9697-e534b77197a9/sk/zakladna-mapa/login?pos=48.800000,19.530000,8"

# Input variables
username = "bbrodian"
password = "Spinka75??"

# Webdriver initialization
driver = webdriver.Chrome()
driver.get(url)

# Email input field
email_field_selector = "#mat-mdc-form-field-label-2 > mat-label"
email_field = driver.find_element(By.CSS_SELECTOR, email_field_selector)
email_field.send_keys(username)
sleep(3)

# Password input field
password_field_selector = "#mat-input-2"
password_field = driver.find_element(By.CSS_SELECTOR, password_field_selector)
password_field.send_keys(password)
sleep(3)

# Click on "Prihlasit"
prihlasit_button_selector = "body > app-root > app-content-layout > mat-drawer-container > mat-drawer-content > mat-drawer-container > mat-drawer > div > app-login > div > form > ng-scrollbar > div > div > div > div > div > div.actions > button > span.mdc-button__label"
prihlasit_button = driver.find_element(By.CSS_SELECTOR, prihlasit_button_selector)
prihlasit_button.click()
sleep(3)

print("Logged in successfully")

driver.quit()