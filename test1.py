import time
from selenium import webdriver

# Initialize Edge driver using EdgeChromiumDriverManager
driver_path = r"C:\browserdrivers\msedgedriver.exe"  # Correct the path and extension
driver = webdriver.Edge(executable_path=driver_path)

# Set page load timeout (not in quotes, and it's an integer)
driver.set_page_load_timeout(10)

# Navigate to the website
driver.get("https://www.google.com/")

# Find the search input by name and enter text
driver.find_element_by_name("q").send_keys("Automation Step by Step")

# Find the search button by name and click
driver.find_element_by_name("btnK").click()

# Wait for a few seconds to see the search results
time.sleep(4)

# Close the browser window
driver.quit()
