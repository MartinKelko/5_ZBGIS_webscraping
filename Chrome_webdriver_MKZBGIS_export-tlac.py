from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

# Target URL
url = "https://test-zbgis2023.skgeodesy.sk/mkzbgis-76ad218b-8807-4c9e-9697-e534b77197a9/sk/zakladna-mapa?pos=48.667687,19.297270,13"

# Webdriver initialization
driver = webdriver.Chrome()
driver.get(url)
sleep(8)

# Click on "release notes window"
release_notes_window_selector = "/html/body/div[2]/div[2]/div/mat-dialog-container/div/div/app-about-modal/mat-dialog-actions/button/span[2]"
release_notes_window = driver.find_element(By.XPATH, release_notes_window_selector)
release_notes_window.click()
sleep(2)

# Click on "menu"
menu_selector = "/html/body/app-root/app-content-layout/mat-drawer-container/mat-drawer-content/mat-drawer-container/mat-drawer-content/div[1]/app-search-box/div/app-menu-button/button/span[3]"
menu = driver.find_element(By.XPATH, menu_selector)
menu.click()
sleep(2)

# Click on "tlac do PDF"
tlac_do_PDF_button_selector = "/html/body/app-root/app-content-layout/mat-drawer-container/mat-drawer/div/app-menu/ng-scrollbar/div/div/div/div/mat-nav-list[1]/a[6]/span"
tlac_do_PDF_button = driver.find_element(By.XPATH, tlac_do_PDF_button_selector)
tlac_do_PDF_button.click()
sleep(3)

# Click on "Tlacit do PDF pre-export"
tlac_do_PDF_button_export_selector = "/html/body/app-root/app-content-layout/mat-drawer-container/mat-drawer-content/mat-drawer-container/mat-drawer/div/app-print/div/div/button/span[2]"
tlac_do_PDF_button_export = driver.find_element(By.XPATH, tlac_do_PDF_button_export_selector)
tlac_do_PDF_button_export.click()
sleep(15)

print("Successfully exported to PDF")

driver.quit()