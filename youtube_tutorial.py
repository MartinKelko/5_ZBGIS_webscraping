import time
from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager

class DemoFindElementbyIDandName:
    def locate_by_id_demo(self):
        driver = None  # Initialize the driver variable outside the try block
        try:
            # Use EdgeChromiumDriverManager to manage the Edge WebDriver
            webdriver_manager = EdgeChromiumDriverManager()
            edge_path = webdriver_manager.install()

            # Use Edge class directly
            driver = webdriver.Edge(executable_path=edge_path)

            driver.get("https://zbgis.skgeodesy.sk/mkzbgis/sk/zakladna-mapa/login?pos=48.800000,19.530000,8")

            # Find the element using CSS selector and send keys
            input_element = driver.find_element_by_css_selector("#mat-input-1")
            input_element.send_keys('test@test.com')

            # Optional: Wait for some time to see the changes on the page
            time.sleep(10)

        except Exception as e:
            print(f"An error occurred: {e}")

        finally:
            if driver:
                # Close the browser window only if the driver is not None
                driver.quit()

# Example Usage
find_by_id = DemoFindElementbyIDandName()
find_by_id.locate_by_id_demo()
