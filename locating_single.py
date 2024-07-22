from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
query = "laptop"
driver.get(f"https://www.amazon.in/s?k={query}&crid=3727JAH5BQD82&sprefix=laptop%2Caps%2C209&ref=nb_sb_noss_1")

elem = driver.find_element(By.CLASS_NAME, "puis-card-container")
#print(elem.text)
print(elem.get_attribute("outerHTML"))

time.sleep(2)
driver.close()