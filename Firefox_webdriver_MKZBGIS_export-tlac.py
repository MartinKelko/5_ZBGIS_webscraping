from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

# Target URL
url = "https://test-zbgis2023.skgeodesy.sk/mkzbgis-76ad218b-8807-4c9e-9697-e534b77197a9/sk/zakladna-mapa?pos=48.667687,19.297270,13"

# Webdriver initialization
driver = webdriver.Firefox()
driver.get(url)
sleep(8)

# Click on "release notes window"
release_notes_window_selector = ".mat-mdc-dialog-actions > button:nth-child(1) > span:nth-child(2)"
release_notes_window = driver.find_element(By.CSS_SELECTOR, release_notes_window_selector)
release_notes_window.click()
sleep(2)

# Click on "menu"
menu_selector = "div.control:nth-child(3) > app-search-box:nth-child(1) > div:nth-child(1) > app-menu-button:nth-child(1) > button:nth-child(1) > span:nth-child(4)"
menu = driver.find_element(By.CSS_SELECTOR, menu_selector)
menu.click()
sleep(2)

# Click on "tlac do PDF"
tlac_do_PDF_button_selector = "a.mat-mdc-list-item:nth-child(6) > span:nth-child(2) > span:nth-child(1)"
tlac_do_PDF_button = driver.find_element(By.CSS_SELECTOR, tlac_do_PDF_button_selector)
tlac_do_PDF_button.click()
sleep(3)

# Click on "Tlacit do PDF pre-export"
tlac_do_PDF_button_export_selector = "button.mdc-button:nth-child(4) > span:nth-child(2)"
tlac_do_PDF_button_export = driver.find_element(By.CSS_SELECTOR, tlac_do_PDF_button_export_selector)
tlac_do_PDF_button_export.click()
sleep(15)

print("Successfully exported to PDF")

driver.quit()