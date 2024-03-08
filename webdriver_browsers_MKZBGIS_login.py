from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

# Target URL
url_FF = "https://test-zbgis2023.skgeodesy.sk/mkzbgis-76ad218b-8807-4c9e-9697-e534b77197a9/sk/zakladna-mapa/login?pos=48.800000,19.530000,8"

# Input variables
username_FF = "bbrodian"
password_FF = "Spinka75??"

# Webdriver initialization
driver = webdriver.Firefox()
driver.get(url_FF)
sleep(8)

# Click on "release notes window" > in the URL hit F12 button (or in the browser right click on release notes window button "Pokracovat" > Inspect > choose element and copy text of the element
# or right click on element and Copy > Copy CSS Selector etc.)
release_notes_window_selector_FF = ".mat-mdc-dialog-actions > button:nth-child(1) > span:nth-child(2)"
release_notes_window_FF = driver.find_element(By.CSS_SELECTOR, release_notes_window_selector_FF)
release_notes_window_FF.click()
sleep(1)

# Email input field
email_field_selector_FF = "#mat-input-1"
email_field_FF = driver.find_element(By.CSS_SELECTOR, email_field_selector_FF)
email_field_FF.send_keys(username_FF)
sleep(2)

# Password input field
password_field_selector_FF = "#mat-input-2"
password_field_FF = driver.find_element(By.CSS_SELECTOR, password_field_selector_FF)
password_field_FF.send_keys(password_FF)
sleep(2)

# Click on "Prihlasit"
prihlasit_button_selector_FF = "button.mdc-button:nth-child(2) > span:nth-child(2)"
prihlasit_button_FF = driver.find_element(By.CSS_SELECTOR, prihlasit_button_selector_FF)
prihlasit_button_FF.click()
sleep(2)

print("Logged in successfully")

driver.quit()

# Target URL
url_MSE = "https://test-zbgis2023.skgeodesy.sk/mkzbgis-76ad218b-8807-4c9e-9697-e534b77197a9/sk/zakladna-mapa/login?pos=48.800000,19.530000,8"

# Input variables
username_MSE = "bbrodian"
password_MSE = "Spinka75??"

# Webdriver initialization
driver = webdriver.Edge()
driver.get(url_MSE)
sleep(8)

# Click on "release notes window"
release_notes_window_selector_MSE = "/html/body/div[2]/div[2]/div/mat-dialog-container/div/div/app-about-modal/mat-dialog-actions/button/span[2]"
release_notes_window_MSE = driver.find_element(By.XPATH, release_notes_window_selector_MSE)
release_notes_window_MSE.click()
sleep(2)

# Email input field
email_field_selector_MSE = "/html/body/app-root/app-content-layout/mat-drawer-container/mat-drawer-content/mat-drawer-container/mat-drawer/div/app-login/div/form/ng-scrollbar/div/div/div/div/div/mat-form-field[1]/div[1]/div/div[2]/input"
email_field_MSE = driver.find_element(By.XPATH, email_field_selector_MSE)
email_field_MSE.send_keys(username_MSE)
sleep(3)

# Password input field
password_field_selector_MSE = "/html/body/app-root/app-content-layout/mat-drawer-container/mat-drawer-content/mat-drawer-container/mat-drawer/div/app-login/div/form/ng-scrollbar/div/div/div/div/div/mat-form-field[2]/div[1]/div/div[2]/input"
password_field_MSE = driver.find_element(By.XPATH, password_field_selector_MSE)
password_field_MSE.send_keys(password_MSE)
sleep(3)

# Click on "Prihlasit"
prihlasit_button_selector_MSE = "/html/body/app-root/app-content-layout/mat-drawer-container/mat-drawer-content/mat-drawer-container/mat-drawer/div/app-login/div/form/ng-scrollbar/div/div/div/div/div/div[1]/button/span[2]"
prihlasit_button_MSE = driver.find_element(By.XPATH, prihlasit_button_selector_MSE)
prihlasit_button_MSE.click()
sleep(3)

print("Logged in successfully")

driver.quit()

# Target URL
url_CHR = "https://test-zbgis2023.skgeodesy.sk/mkzbgis-76ad218b-8807-4c9e-9697-e534b77197a9/sk/zakladna-mapa/login?pos=48.800000,19.530000,8"

# Input variables
username_CHR = "bbrodian"
password_CHR = "Spinka75??"

# Webdriver initialization
driver = webdriver.Chrome()
driver.get(url_CHR)
sleep(8)

# Click on "release notes window"
release_notes_window_selector_CHR = "/html/body/div[2]/div[2]/div/mat-dialog-container/div/div/app-about-modal/mat-dialog-actions/button/span[2]"
release_notes_window_CHR = driver.find_element(By.XPATH, release_notes_window_selector_CHR)
release_notes_window_CHR.click()
sleep(2)

# Email input field
email_field_selector_CHR = "/html/body/app-root/app-content-layout/mat-drawer-container/mat-drawer-content/mat-drawer-container/mat-drawer/div/app-login/div/form/ng-scrollbar/div/div/div/div/div/mat-form-field[1]/div[1]/div/div[2]/input"
email_field_CHR = driver.find_element(By.XPATH, email_field_selector_CHR)
email_field_CHR.send_keys(username_CHR)
sleep(3)

# Password input field
password_field_selector_CHR = "#mat-input-2"
password_field_CHR = driver.find_element(By.CSS_SELECTOR, password_field_selector_CHR)
password_field_CHR.send_keys(password_CHR)
sleep(3)

# Click on "Prihlasit"
prihlasit_button_selector_CHR = "/html/body/app-root/app-content-layout/mat-drawer-container/mat-drawer-content/mat-drawer-container/mat-drawer/div/app-login/div/form/ng-scrollbar/div/div/div/div/div/div[1]/button/span[2]"
prihlasit_button_CHR = driver.find_element(By.XPATH, prihlasit_button_selector_CHR)
prihlasit_button_CHR.click()
sleep(3)

print("Logged in successfully")

driver.quit()