from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = r"C:\Users\Nexus\Documents\Selenium Webscrapper\selenium_files\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://images.google.com/")
print(driver.title)

search_url_element = driver.find_element(by=By.NAME, value="q")
search_url_element.send_keys("Cars")
search_url_element.send_keys(Keys.RETURN)



try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "OztcRd"))
    )
finally:
    driver.quit()


# time.sleep(5)
# driver.quit()