import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# Initialize Edge driver using EdgeChromiumDriverManager
driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

# Navigate to the website
driver.get("https://zbgis.skgeodesy.sk/mkzbgis/")
driver.maximize_window()
time.sleep(10)
print(driver.title)



