from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# Target URL
url_FF = "https://test-zbgis2023.skgeodesy.sk/mkzbgis-76ad218b-8807-4c9e-9697-e534b77197a9/sk/zakladna-mapa?pos=48.667687,19.297270,13"

# Input Variables
nazov_FF = "Hrochot"

# Webdriver initialization
driver = webdriver.Firefox()
driver.get(url_FF)
driver.maximize_window()
sleep(8)

# Click on "release notes window"
release_notes_window_selector_FF = ".mat-mdc-dialog-actions > button:nth-child(1) > span:nth-child(2)"
release_notes_window_FF = driver.find_element(By.CSS_SELECTOR, release_notes_window_selector_FF)
release_notes_window_FF.click()
sleep(2)

# Click on "menu"
menu_selector_FF = "div.control:nth-child(3) > app-search-box:nth-child(1) > div:nth-child(1) > app-menu-button:nth-child(1) > button:nth-child(1) > span:nth-child(4)"
menu_FF = driver.find_element(By.CSS_SELECTOR, menu_selector_FF)
menu_FF.click()
sleep(2)

# Click on "tlac do PDF"
tlac_do_PDF_button_selector_FF = "a.mat-mdc-list-item:nth-child(6) > span:nth-child(2) > span:nth-child(1)"
tlac_do_PDF_button_FF = driver.find_element(By.CSS_SELECTOR, tlac_do_PDF_button_selector_FF)
tlac_do_PDF_button_FF.click()
sleep(6)

# double click in Nazov input field
double_click_selector_FF = "#mat-input-1"
double_click_FF = driver.find_element(By.CSS_SELECTOR, double_click_selector_FF)
double_click_FF.click()
action_chains = ActionChains(driver)
action_chains.double_click(double_click_FF).perform()
sleep(6)

# Nazov input field
nazov_field_selector_FF = "#mat-input-1"
nazov_field_FF = driver.find_element(By.CSS_SELECTOR, nazov_field_selector_FF)
nazov_field_FF.send_keys(nazov_FF)
sleep(2)

# Click on "Tlacit do PDF pre-export"
tlac_do_PDF_button_export_selector_FF = "button.mdc-button:nth-child(4) > span:nth-child(2)"
tlac_do_PDF_button_export_FF = driver.find_element(By.CSS_SELECTOR, tlac_do_PDF_button_export_selector_FF)
tlac_do_PDF_button_export_FF.click()
sleep(15)

print("Successfully exported to PDF")

driver.quit()

# Target URL
url_CHR = "https://test-zbgis2023.skgeodesy.sk/mkzbgis-76ad218b-8807-4c9e-9697-e534b77197a9/sk/zakladna-mapa?pos=48.667687,19.297270,13"

# Input Variables
nazov_CHR = "Hrochot"

# Webdriver initialization
driver = webdriver.Chrome()
driver.get(url_CHR)
driver.maximize_window()
sleep(8)

# Click on "release notes window"
release_notes_window_selector_CHR = "/html/body/div[2]/div[2]/div/mat-dialog-container/div/div/app-about-modal/mat-dialog-actions/button/span[2]"
release_notes_window_CHR = driver.find_element(By.XPATH, release_notes_window_selector_CHR)
release_notes_window_CHR.click()
sleep(2)

# Click on "menu"
menu_selector_CHR = "/html/body/app-root/app-content-layout/mat-drawer-container/mat-drawer-content/mat-drawer-container/mat-drawer-content/div[1]/app-search-box/div/app-menu-button/button/span[3]"
menu_CHR = driver.find_element(By.XPATH, menu_selector_CHR)
menu_CHR.click()
sleep(2)

# Click on "tlac do PDF"
tlac_do_PDF_button_selector_CHR = "/html/body/app-root/app-content-layout/mat-drawer-container/mat-drawer/div/app-menu/ng-scrollbar/div/div/div/div/mat-nav-list[1]/a[6]/span"
tlac_do_PDF_button_CHR = driver.find_element(By.XPATH, tlac_do_PDF_button_selector_CHR)
tlac_do_PDF_button_CHR.click()
sleep(6)

# double click in Nazov input field
double_click_selector_CHR = "/html/body/app-root/app-content-layout/mat-drawer-container/mat-drawer-content/mat-drawer-container/mat-drawer/div/app-print/div/div/mat-form-field/div[1]/div/div[2]/input"
double_click_CHR = driver.find_element(By.XPATH, double_click_selector_CHR)
double_click_CHR.click()
action_chains = ActionChains(driver)
action_chains.double_click(double_click_CHR).perform()
sleep(6)

# Nazov input field
nazov_field_selector_CHR = "/html/body/app-root/app-content-layout/mat-drawer-container/mat-drawer-content/mat-drawer-container/mat-drawer/div/app-print/div/div/mat-form-field/div[1]/div/div[2]/input"
nazov_field_CHR = driver.find_element(By.XPATH, nazov_field_selector_CHR)
nazov_field_CHR.send_keys(nazov_CHR)
sleep(2)

# Click on "Tlacit do PDF pre-export"
tlac_do_PDF_button_export_selector_CHR = "/html/body/app-root/app-content-layout/mat-drawer-container/mat-drawer-content/mat-drawer-container/mat-drawer/div/app-print/div/div/button/span[2]"
tlac_do_PDF_button_export_CHR = driver.find_element(By.XPATH, tlac_do_PDF_button_export_selector_CHR)
tlac_do_PDF_button_export_CHR.click()
sleep(15)

print("Successfully exported to PDF")

driver.quit()

# Target URL
url_MSE = "https://test-zbgis2023.skgeodesy.sk/mkzbgis-76ad218b-8807-4c9e-9697-e534b77197a9/sk/zakladna-mapa?pos=48.667687,19.297270,13"

# Input Variables
nazov_MSE = "Hrochot"

# Webdriver initialization
driver = webdriver.Edge()
driver.get(url_MSE)
driver.maximize_window()
sleep(8)

# Click on "release notes window"
release_notes_window_selector_MSE = "/html/body/div[2]/div[2]/div/mat-dialog-container/div/div/app-about-modal/mat-dialog-actions/button/span[2]"
release_notes_window_MSE = driver.find_element(By.XPATH, release_notes_window_selector_MSE)
release_notes_window_MSE.click()
sleep(2)

# Click on "menu"
menu_selector_MSE = "body > app-root > app-content-layout > mat-drawer-container > mat-drawer-content > mat-drawer-container > mat-drawer-content > div.control.top-left.ng-star-inserted > app-search-box > div > app-menu-button > button > span.mat-mdc-button-touch-target"
menu_MSE = driver.find_element(By.CSS_SELECTOR, menu_selector_MSE)
menu_MSE.click()
sleep(4)

# Click on "tlac do PDF"
tlac_do_PDF_button_selector_MSE = "body > app-root > app-content-layout > mat-drawer-container > mat-drawer > div > app-menu > ng-scrollbar > div > div > div > div > mat-nav-list:nth-child(2) > a:nth-child(6) > span > span.mat-mdc-list-item-title.mdc-list-item__primary-text"
tlac_do_PDF_button_MSE = driver.find_element(By.CSS_SELECTOR, tlac_do_PDF_button_selector_MSE)
tlac_do_PDF_button_MSE.click()
sleep(6)

# double click in Nazov input field
double_click_selector_MSE = "/html/body/app-root/app-content-layout/mat-drawer-container/mat-drawer-content/mat-drawer-container/mat-drawer/div/app-print/div/div/mat-form-field/div[1]/div/div[2]/input"
double_click_MSE = driver.find_element(By.XPATH, double_click_selector_MSE)
double_click_MSE.click()
action_chains = ActionChains(driver)
action_chains.double_click(double_click_MSE).perform()
sleep(6)

# Nazov input field
nazov_field_selector_MSE = "/html/body/app-root/app-content-layout/mat-drawer-container/mat-drawer-content/mat-drawer-container/mat-drawer/div/app-print/div/div/mat-form-field/div[1]/div/div[2]/input"
nazov_field_MSE = driver.find_element(By.XPATH, nazov_field_selector_MSE)
nazov_field_MSE.send_keys(nazov_MSE)
sleep(2)

# Click on "Tlacit do PDF pre-export"
tlac_do_PDF_button_export_selector_MSE = "body > app-root > app-content-layout > mat-drawer-container > mat-drawer-content > mat-drawer-container > mat-drawer > div > app-print > div > div > button > span.mdc-button__label"
tlac_do_PDF_button_export_MSE = driver.find_element(By.CSS_SELECTOR, tlac_do_PDF_button_export_selector_MSE)
tlac_do_PDF_button_export_MSE.click()
sleep(15)

print("Successfully exported to PDF")

driver.quit()