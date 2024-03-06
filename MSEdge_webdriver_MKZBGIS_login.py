from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

# Target URL
url = "https://test-zbgis2023.skgeodesy.sk/mkzbgis-76ad218b-8807-4c9e-9697-e534b77197a9/sk/zakladna-mapa/login?pos=48.800000,19.530000,8"

# Input variables
username = "bbrodian"
password = "Spinka75??"

# Webdriver initialization
driver = webdriver.Edge()
driver.get(url)

# Input field found by Copy > CSS Selector
email_field = "#mat-mdc-form-field-label-2 > mat-label"
driver.find_element(By.CSS_SELECTOR, email_field).send_keys()
sleep(1)

# Input field found by Copy > CSS Selector
password_field = "#mat-input-2"
driver.find_element(By.CSS_SELECTOR, password_field).send_keys()
sleep(1)

# Click "Prihlasit"
prihlasit_button = "body > app-root > app-content-layout > mat-drawer-container > mat-drawer-content > mat-drawer-container > mat-drawer > div > app-login > div > form > ng-scrollbar > div > div > div > div > div > div.actions > button > span.mdc-button__label"
driver.find_element(By.CSS_SELECTOR, prihlasit_button).click()
sleep(1)

print("Logged in successfully")

driver.quit()