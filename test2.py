import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

os.environ['PATH'] += r";C:\browserdrivers"
driver = webdriver.Chrome()

driver.get('https://zbgis.skgeodesy.sk/rts/sk/Transform')
driver.implicitly_wait(5)

try:
    # Correct the find_element_by_id method, and remove the redundant string 'InputFormat'
    no_button = driver.find_element_by_class_name('btn waves-effect waves-green white grey-text text-darken-4')
    no_button.click()
except:
    print('No element with this ID. Skipping ....')

sum1 = driver.find_element_by_id('File')

# Add a space between Keys.NUMPAD1 and Keys.NUMPAD5
sum1.send_keys(Keys.NUMPAD1, Keys.NUMPAD5)

btn = driver.find_element_by_css_selector('button[onclick="return total()"]')
btn.click()


