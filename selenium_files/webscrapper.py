from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import urllib

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://images.google.com/")
query = "Cars"
search_url_element = driver.find_element(by=By.NAME, value="q")
search_url_element.send_keys(query)
search_url_element.send_keys(Keys.RETURN)

# To load the entire page we first scroll to the bottom. 
def scroll_to_bottom():
    last_height = driver.execute_script('\
    return document.body.scrollHeight')
 
    while True:
        driver.execute_script('\
        window.scrollTo(0,document.body.scrollHeight)')
        time.sleep(3)
 
        new_height = driver.execute_script('\
        return document.body.scrollHeight')
 
        # Click on "Show more results"
        try:
            driver.find_element(By.CSS_SELECTOR, ".YstHxe input").click()
            time.sleep(3)
        except:
            pass
 
        if new_height == last_height:
            break
        last_height = new_height

# element = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.CLASS_NAME, "OztcRd"))
# )

scroll_to_bottom()
time.sleep(2)

# Parse through the first 50 images on the webpage and save them as screenshots.
for i in range(50):
    try:
        image = driver.find_element(By.XPATH, '//*[@id="islrg"]/div[1]/div['+str(i)+']/a[1]/div[1]/img')
        image.screenshot("C:/Users/Nexus/Documents/Selenium Webscrapper/webscraper_results/" + query + "_" + str(i) + ".png")
    except:
        continue




# time.sleep(5)
# driver.quit()