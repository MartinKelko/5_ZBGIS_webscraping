# MSEdge
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Target URL
url_MSE = "https://test-zbgis2023.skgeodesy.sk/rts-next/sk/transform"

# Input Variables
Y_coordinate_MSE = "-530212.396"
X_coordinate_MSE = "-1329074.630"

# Webdriver initialization
driver = webdriver.Edge()
driver.get(url_MSE)
driver.maximize_window()
sleep(2)

# Click on "insert_format"
insert_format_selector_MSE = "#mat-select-value-1"
insert_format_MSE = driver.find_element(By.CSS_SELECTOR, insert_format_selector_MSE)
insert_format_MSE.click()
sleep(0.5)

# Click on "transformacia_bodu_jednotlivo"
TBJ_selector_MSE = "/html/body/div[2]/div[2]/div/div/mat-option[2]/span"
TBJ_MSE = driver.find_element(By.XPATH, TBJ_selector_MSE)
TBJ_MSE.click()
sleep(0.5)

# Click on "INPUT_CRS"
input_CRS_selector_MSE = "/html/body/app-layout/mat-drawer-container/mat-drawer-content/app-transform/app-dropzone/div[1]/form/div[2]/mat-form-field[1]/div[1]/div/div[2]/mat-select/div/div[1]/span"
input_CRS_MSE = driver.find_element(By.XPATH, input_CRS_selector_MSE)
input_CRS_MSE.click()
sleep(0.5)

# Click on "INPUT_SJTSK-JTSK"
input_SJTSK_selector_MSE = "/html/body/div[2]/div[2]/div/div/mat-option[2]/span"
input_SJTSK_MSE = driver.find_element(By.XPATH, input_SJTSK_selector_MSE)
input_SJTSK_MSE.click()
sleep(0.5)

# Click on "OUTPUT_CRS"
output_CRS_selector_MSE = "/html/body/app-layout/mat-drawer-container/mat-drawer-content/app-transform/app-dropzone/div[1]/form/div[3]/mat-form-field[1]/div[1]/div/div[2]/mat-select/div/div[1]/span"
output_CRS_MSE = driver.find_element(By.XPATH, output_CRS_selector_MSE)
output_CRS_MSE.click()
sleep(0.5)

# Click on "OUTPUT_Bessel_JTSK"
output_Bessel_JTSK_selector_MSE = "/html/body/div[2]/div[2]/div/div/mat-option[3]/span"
output_Bessel_JTSK_MSE = driver.find_element(By.XPATH, output_Bessel_JTSK_selector_MSE)
output_Bessel_JTSK_MSE.click()
sleep(0.5)

# Click on "INPUT_Y_coordinates"
#input_Y_coordinates_selector_MSE = "/html/body/app-layout/mat-drawer-container/mat-drawer-content/app-transform/app-dropzone/div[1]/form/div[5]/mat-form-field/div[1]/div/div[2]/input"
#input_Y_coordinates_MSE = driver.find_element(By.XPATH, input_Y_coordinates_selector_MSE)
#input_Y_coordinates_MSE.click()
#sleep(0.5)

# Y_coordinate_variable
Y_coordinate_MSE_selector = "/html/body/app-layout/mat-drawer-container/mat-drawer-content/app-transform/app-dropzone/div[1]/form/div[5]/mat-form-field/div[1]/div/div[2]/input"
Y_coordinate_MSE_field = driver.find_element(By.XPATH, Y_coordinate_MSE_selector)
Y_coordinate_MSE_field.send_keys(Y_coordinate_MSE)
sleep(0.5)

# Click on "INPUT_X_coordinates"
#input_X_coordinates_selector_MSE = "/html/body/app-layout/mat-drawer-container/mat-drawer-content/app-transform/app-dropzone/div[1]/form/div[6]/mat-form-field/div[1]/div/div[2]/input"
#input_X_coordinates_MSE = driver.find_element(By.XPATH, input_X_coordinates_selector_MSE)
#input_X_coordinates_MSE.click()
#sleep(0.5)

# X_coordinate_variable
X_coordinate_MSE_selector = "/html/body/app-layout/mat-drawer-container/mat-drawer-content/app-transform/app-dropzone/div[1]/form/div[6]/mat-form-field/div[1]/div/div[2]/input"
X_coordinate_MSE_field = driver.find_element(By.XPATH, X_coordinate_MSE_selector)
X_coordinate_MSE_field.send_keys(X_coordinate_MSE)
sleep(5)

# Click on "transform"
#transform_selector_MSE = "body > app-layout > mat-drawer-container > mat-drawer-content > app-transform > app-dropzone > div.container.row > form > div:nth-child(7) > div > button:nth-child(2) > span.mat-mdc-button-touch-target"
#transform_MSE = driver.find_element(By.CSS_SELECTOR, transform_selector_MSE)
#transform_MSE.click()
#leep(5)

# Hit Enter
Enter_button_selector_MSE = "#mat-input-4"
Enter_button_MSE = driver.find_element(By.CSS_SELECTOR, Enter_button_selector_MSE)
Enter_button_MSE.send_keys(Keys.ENTER)
sleep(5)

print("Successfully transformed in Microsoft Edge browser")

driver.quit()