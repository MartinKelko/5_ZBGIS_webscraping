# Mozilla Firefox
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

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

# Click on "transform"
#transform_selector_FF = "button.mdc-button:nth-child(2) > span:nth-child(5)"
#transform_FF = driver.find_element(By.CSS_SELECTOR, transform_selector_FF)
#transform_FF.click()
#sleep(5)

# Hit Enter
Enter_button_selector_FF = "#mat-input-3"
Enter_button_FF = driver.find_element(By.CSS_SELECTOR, Enter_button_selector_FF)
Enter_button_FF.send_keys(Keys.ENTER)

print("Successfully transformed in Mozilla Firefox browser")

driver.quit()