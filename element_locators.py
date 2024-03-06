import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.microsoft import EdgeChromiumDriverManager

class DemoFindElementbyIDandName:
    def __init__(self, url):
        self.url = url

    def initialize_driver(self):
        edge_service = webdriver.EdgeService(executable_path=EdgeChromiumDriverManager().install())
        return webdriver.Edge(service=edge_service)

    def locate_by_id_demo(self):
        try:
            driver = self.initialize_driver()
            driver.get(self.url)

            input_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "#mat-input-1"))
            )

            input_element.send_keys('test@test.com')

        except Exception as e:
            print(f"An error occurred: {e}")

        finally:
            driver.quit()

# Example Usage
url_to_test = ("https://zbgis.skgeodesy.sk/mkzbgis/sk/zakladna-mapa/login?pos=48.800000,19.530000,8")
find_by_id = DemoFindElementbyIDandName(url_to_test)
find_by_id.locate_by_id_demo()
