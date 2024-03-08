from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# Target URL
url = "https://test-zbgis2023.skgeodesy.sk/mkzbgis-76ad218b-8807-4c9e-9697-e534b77197a9/sk/zakladna-mapa?pos=48.667687,19.297270,13"

# Input Variables
nazov = "Hrochot"

# Webdriver initialization
driver = webdriver.Edge()
driver.get(url)
driver.maximize_window()
sleep(8)

# Click on "release notes window"
release_notes_window_selector = "/html/body/div[2]/div[2]/div/mat-dialog-container/div/div/app-about-modal/mat-dialog-actions/button/span[2]"
release_notes_window = driver.find_element(By.XPATH, release_notes_window_selector)
release_notes_window.click()
sleep(2)

# Click on "menu"
menu_selector = "body > app-root > app-content-layout > mat-drawer-container > mat-drawer-content > mat-drawer-container > mat-drawer-content > div.control.top-left.ng-star-inserted > app-search-box > div > app-menu-button > button > span.mat-mdc-button-touch-target"
menu = driver.find_element(By.CSS_SELECTOR, menu_selector)
menu.click()
sleep(4)

# Click on "tlac do PDF"
tlac_do_PDF_button_selector = "body > app-root > app-content-layout > mat-drawer-container > mat-drawer > div > app-menu > ng-scrollbar > div > div > div > div > mat-nav-list:nth-child(2) > a:nth-child(6) > span > span.mat-mdc-list-item-title.mdc-list-item__primary-text"
tlac_do_PDF_button = driver.find_element(By.CSS_SELECTOR, tlac_do_PDF_button_selector)
tlac_do_PDF_button.click()
sleep(6)

# double click in Nazov input field
double_click_selector = "/html/body/app-root/app-content-layout/mat-drawer-container/mat-drawer-content/mat-drawer-container/mat-drawer/div/app-print/div/div/mat-form-field/div[1]/div/div[2]/input"
double_click = driver.find_element(By.XPATH, double_click_selector)
double_click.click()
action_chains = ActionChains(driver)
action_chains.double_click(double_click).perform()
sleep(6)

# Nazov input field
nazov_field_selector = "/html/body/app-root/app-content-layout/mat-drawer-container/mat-drawer-content/mat-drawer-container/mat-drawer/div/app-print/div/div/mat-form-field/div[1]/div/div[2]/input"
nazov_field = driver.find_element(By.XPATH, nazov_field_selector)
nazov_field.send_keys(nazov)
sleep(2)

# Click on "Tlacit do PDF pre-export"
tlac_do_PDF_button_export_selector = "body > app-root > app-content-layout > mat-drawer-container > mat-drawer-content > mat-drawer-container > mat-drawer > div > app-print > div > div > button > span.mdc-button__label"
tlac_do_PDF_button_export = driver.find_element(By.CSS_SELECTOR, tlac_do_PDF_button_export_selector)
tlac_do_PDF_button_export.click()
sleep(15)

print("Successfully exported to PDF")

driver.quit()