from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

# Target URL
url = "https://test-zbgis2023.skgeodesy.sk/mkzbgis-76ad218b-8807-4c9e-9697-e534b77197a9/sk/zakladna-mapa?pos=48.667687,19.297270,13"

# Webdriver initialization
driver = webdriver.Chrome()
driver.get(url)
sleep(8)

# Click on "window"
window_selector = "/html/body/app-root/app-content-layout/mat-drawer-container/mat-drawer-content/mat-drawer-container/mat-drawer-content/div[1]/app-search-box/div/app-menu-button/button/span[3]"
window = driver.find_element(By.XPATH, window_selector)
window.click()
sleep(2)

# Click on "Prihlasit"
prihlasit_button_selector = "/html/body/app-root/app-content-layout/mat-drawer-container/mat-drawer/div/app-menu/ng-scrollbar/div/div/div/div/mat-nav-list[1]/a[6]/span/span[1]"
prihlasit_button = driver.find_element(By.XPATH, prihlasit_button_selector)
prihlasit_button.click()
sleep(3)

# Click on "Prihlasit"
prihlasit_button_selector = "/html/body/app-root/app-content-layout/mat-drawer-container/mat-drawer-content/mat-drawer-container/mat-drawer/div/app-print/div/div/button/span[2]"
prihlasit_button = driver.find_element(By.XPATH, prihlasit_button_selector)
prihlasit_button.click()
sleep(3)

print("Logged in successfully")

driver.quit()