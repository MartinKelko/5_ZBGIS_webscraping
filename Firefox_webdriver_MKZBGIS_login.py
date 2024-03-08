# YTB tutorial https://www.youtube.com/watch?v=-fgrIBag6AI

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

# Click on "release notes window" > in the URL hit F12 button (or in the browser right click on release notes window button "Pokracovat" > Inspect > choose element and copy text of the element
# or right click on element and Copy > Copy CSS Selector etc.)
release_notes_window_selector = ".mat-mdc-dialog-actions > button:nth-child(1) > span:nth-child(2)"
release_notes_window = driver.find_element(By.CSS_SELECTOR, release_notes_window_selector)
release_notes_window.click()
sleep(1)

# Email input field
email_field_selector = "#mat-input-1"
email_field = driver.find_element(By.CSS_SELECTOR, email_field_selector)
email_field.send_keys(username)
sleep(2)

# Password input field
password_field_selector = "#mat-input-2"
password_field = driver.find_element(By.CSS_SELECTOR, password_field_selector)
password_field.send_keys(password)
sleep(2)

# Click on "Prihlasit"
prihlasit_button_selector = "button.mdc-button:nth-child(2) > span:nth-child(2)"
prihlasit_button = driver.find_element(By.CSS_SELECTOR, prihlasit_button_selector)
prihlasit_button.click()
sleep(2)

print("Logged in successfully")

driver.quit()
