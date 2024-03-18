from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

# Microsoft Edge
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

#ActionChains(self.driver).send_keys(Keys.ENTER).perform()

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
sleep(0.5)

# option 1 # Click on "transform" - NEFUNGUJE
#transform_selector_MSE = "/html/body/app-layout/mat-drawer-container/mat-drawer-content/app-transform/app-dropzone/div[1]/form/div[7]/div/button[2]/span[2]"
#transform_MSE = driver.find_element(By.XPATH, transform_selector_MSE)
#transform_MSE.click()
#sleep(10)

# option 2 # Hit Enter - FUNGUJE
transform_MSE_selector = "/html/body/app-layout/mat-drawer-container/mat-drawer-content/app-transform/app-dropzone/div[1]/form/div[6]/mat-form-field/div[1]/div/div[2]/input"
transform_MSE = driver.find_element(By.XPATH, transform_MSE_selector)
transform_MSE.send_keys(Keys.ENTER)
sleep(10)

print("Successfully transformed in Microsoft Edge browser")

driver.quit()

# Google Chrome
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

# Target URL
url_CHR = "https://test-zbgis2023.skgeodesy.sk/rts-next/sk/transform"

# Input Variables
Y_coordinate_CHR = "-530212.396"
X_coordinate_CHR = "-1329074.630"

# Webdriver initialization
driver = webdriver.Chrome()
driver.get(url_CHR)
driver.maximize_window()
sleep(2)

# Click on "insert_format"
insert_format_selector_CHR = "/html/body/app-layout/mat-drawer-container/mat-drawer-content/app-transform/app-dropzone/div[1]/form/div[1]/mat-form-field/div[1]/div/div[2]/mat-select/div/div[1]/span"
insert_format_CHR = driver.find_element(By.XPATH, insert_format_selector_CHR)
insert_format_CHR.click()
sleep(0.5)

# Click on "transformacia_bodu_jednotlivo"
TBJ_selector_CHR = "/html/body/div[2]/div[2]/div/div/mat-option[2]/span"
TBJ_CHR = driver.find_element(By.XPATH, TBJ_selector_CHR)
TBJ_CHR.click()
sleep(0.5)

# Click on "INPUT_CRS"
input_CRS_selector_CHR = "/html/body/app-layout/mat-drawer-container/mat-drawer-content/app-transform/app-dropzone/div[1]/form/div[2]/mat-form-field[1]/div[1]/div/div[2]/mat-select/div/div[1]/span"
input_CRS_CHR = driver.find_element(By.XPATH, input_CRS_selector_CHR)
input_CRS_CHR.click()
sleep(0.5)

# Click on "INPUT_SJTSK-JTSK"
input_SJTSK_selector_CHR = "/html/body/div[2]/div[2]/div/div/mat-option[2]/span"
input_SJTSK_CHR = driver.find_element(By.XPATH, input_SJTSK_selector_CHR)
input_SJTSK_CHR.click()
sleep(0.5)

# Click on "OUTPUT_CRS"
output_CRS_selector_CHR = "/html/body/app-layout/mat-drawer-container/mat-drawer-content/app-transform/app-dropzone/div[1]/form/div[3]/mat-form-field[1]/div[1]/div/div[2]/mat-select/div/div[1]/span"
output_CRS_CHR = driver.find_element(By.XPATH, output_CRS_selector_CHR)
output_CRS_CHR.click()
sleep(0.5)

# Click on "OUTPUT_Bessel_JTSK"
output_Bessel_JTSK_selector_CHR = "/html/body/div[2]/div[2]/div/div/mat-option[3]/span"
output_Bessel_JTSK_CHR = driver.find_element(By.XPATH, output_Bessel_JTSK_selector_CHR)
output_Bessel_JTSK_CHR.click()
sleep(0.5)

# Click on "INPUT_Y_coordinates"
#input_Y_coordinates_selector_CHR = "#mat-input-1"
#input_Y_coordinates_CHR = driver.find_element(By.CSS_SELECTOR, input_Y_coordinates_selector_CHR)
#input_Y_coordinates_CHR.click()
#sleep(0.5)

# Y_coordinate_variable
Y_coordinate_CHR_selector = "/html/body/app-layout/mat-drawer-container/mat-drawer-content/app-transform/app-dropzone/div[1]/form/div[5]/mat-form-field/div[1]/div/div[2]/input"
Y_coordinate_CHR_field = driver.find_element(By.XPATH, Y_coordinate_CHR_selector)
Y_coordinate_CHR_field.send_keys(Y_coordinate_CHR)
sleep(0.5)

# Click on "INPUT_X_coordinates"
#input_X_coordinates_selector_CHR = "/html/body/app-layout/mat-drawer-container/mat-drawer-content/app-transform/app-dropzone/div[1]/form/div[5]/mat-form-field/div[1]/div/div[2]/input"
#input_X_coordinates_CHR = driver.find_element(By.XPATH, input_X_coordinates_selector_CHR)
#input_X_coordinates_CHR.click()
#sleep(0.5)

# X_coordinate_variable
X_coordinate_CHR_selector = "/html/body/app-layout/mat-drawer-container/mat-drawer-content/app-transform/app-dropzone/div[1]/form/div[6]/mat-form-field/div[1]/div/div[2]/input"
X_coordinate_CHR_field = driver.find_element(By.XPATH, X_coordinate_CHR_selector)
X_coordinate_CHR_field.send_keys(X_coordinate_CHR)
sleep(5)

# Click on "transform"
#transform_selector_CHR = "/html/body/app-layout/mat-drawer-container/mat-drawer-content/app-transform/app-dropzone/div[1]/form/div[7]/div/button[2]/mat-icon"
#transform_CHR = driver.find_element(By.XPATH, transform_selector_CHR)
#transform_CHR.click()
#sleep(50)

# option 2 # Hit Enter
transform_CHR_selector = "/html/body/app-layout/mat-drawer-container/mat-drawer-content/app-transform/app-dropzone/div[1]/form/div[6]/mat-form-field/div[1]/div/div[2]/input"
transform_CHR = driver.find_element(By.XPATH, transform_CHR_selector)
transform_CHR.send_keys(Keys.ENTER)
sleep(10)

print("Successfully transformed in Google Chrome browser")

driver.quit()

# Mozilla Firefox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

# Target URL
url_FF = "https://test-zbgis2023.skgeodesy.sk/rts-next/sk/transform"

# Input Variables
Y_coordinate_FF = "-530212.396"
X_coordinate_FF = "-1329074.630"

# Webdriver initialization
driver = webdriver.Firefox()
driver.get(url_FF)
driver.maximize_window()
sleep(2)

# Click on "insert_format"
insert_format_selector_FF = "#mat-select-value-1"
insert_format_FF = driver.find_element(By.CSS_SELECTOR, insert_format_selector_FF)
insert_format_FF.click()
sleep(0.5)

# Click on "transformacia_bodu_jednotlivo"
TBJ_selector_FF = "#mat-option-5 > span:nth-child(1)"
TBJ_FF = driver.find_element(By.CSS_SELECTOR, TBJ_selector_FF)
TBJ_FF.click()
sleep(0.5)

# Click on "INPUT_CRS"
input_CRS_selector_FF = "#mat-select-value-3"
input_CRS_FF = driver.find_element(By.CSS_SELECTOR, input_CRS_selector_FF)
input_CRS_FF.click()
sleep(0.5)

# Click on "INPUT_SJTSK-JTSK"
input_SJTSK_selector_FF = "#mat-select-2"
input_SJTSK_FF = driver.find_element(By.CSS_SELECTOR, input_SJTSK_selector_FF)
input_SJTSK_FF.click()
sleep(0.5)

# Click on "OUTPUT_CRS"
output_CRS_selector_FF = "#mat-select-value-7"
output_CRS_FF = driver.find_element(By.CSS_SELECTOR, output_CRS_selector_FF)
output_CRS_FF.click()
sleep(0.5)

# Click on "OUTPUT_Bessel_JTSK"
output_Bessel_JTSK_selector_FF = "#mat-option-42 > span:nth-child(1)"
output_Bessel_JTSK_FF = driver.find_element(By.CSS_SELECTOR, output_Bessel_JTSK_selector_FF)
output_Bessel_JTSK_FF.click()
sleep(0.5)

# Click on "INPUT_Y_coordinates"
#input_Y_coordinates_selector_FF = "#mat-input-1"
#input_Y_coordinates_FF = driver.find_element(By.CSS_SELECTOR, input_Y_coordinates_selector_FF)
#input_Y_coordinates_FF.click()
#sleep(0.5)

# Y_coordinate_variable
Y_coordinate_FF_selector = "#mat-input-1"
Y_coordinate_FF_field = driver.find_element(By.CSS_SELECTOR, Y_coordinate_FF_selector)
Y_coordinate_FF_field.send_keys(Y_coordinate_FF)
sleep(0.5)

# Click on "INPUT_X_coordinates"
#input_X_coordinates_selector_FF = "#mat-input-2"
#input_X_coordinates_FF = driver.find_element(By.CSS_SELECTOR, input_X_coordinates_selector_FF)
#input_X_coordinates_FF.click()
#sleep(0.5)

# X_coordinate_variable
X_coordinate_FF_selector = "#mat-input-2"
X_coordinate_FF_field = driver.find_element(By.CSS_SELECTOR, X_coordinate_FF_selector)
X_coordinate_FF_field.send_keys(X_coordinate_FF)
sleep(5)

# option 1 # Click on "transform"
#transform_selector_FF = "button.mdc-button:nth-child(2) > span:nth-child(5)"
#transform_FF = driver.find_element(By.CSS_SELECTOR, transform_selector_FF)
#transform_FF.click()
#sleep(5)

# option 2 # Hit Enter
transform_FF_selector = "#mat-input-2"
transform_FF = driver.find_element(By.CSS_SELECTOR, transform_FF_selector)
transform_FF.send_keys(Keys.ENTER)
sleep(5)

print("Successfully transformed in Mozilla Firefox browser")

driver.quit()