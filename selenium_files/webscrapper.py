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

driver.get("https://www.pakwheels.com/")
driver.maximize_window()
# query = "Cars"
# search_url_element = driver.find_element(by=By.NAME, value="q")
# search_url_element.send_keys(query)
# search_url_element.send_keys(Keys.RETURN)

scroll_to_height(700)
one_thousandCC_cars_element = driver.find_element(By.XPATH, '//*[@id="browesCTGSlider"]/div[1]/ul[1]/li[1]/a/img')
two_thousandCC_cars_element = driver.find_element(By.XPATH, '//*[@id="browesCTGSlider"]/div[1]/ul[1]/li[2]/a/img')
one_thousandCC_cars_element.click()

ad_titles = []
for i in range(50):
    ad_titles.append(driver.find_element(By.XPATH, '//*[@id="main_ad_6255096"]/div/div[2]/div[1]/div/div/a/h3'))
    '//*[@id="main_ad_6203273"]/div/div[2]/div[1]/div/div/a/h3'

element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "OztcRd"))
)

# Parse through the first 50 images on the webpage and save them as screenshots.
for i in range(50):
    try:
        image = driver.find_element(By.XPATH, '//*[@id="islrg"]/div[1]/div['+str(i)+']/a[1]/div[1]/img')
        image.screenshot("C:/Users/Nexus/Documents/Selenium Webscrapper/webscraper_results/" + query + "_" + str(i) + ".png")
    except:
        continue


