from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By

# Using Chrome to access web
driver = webdriver.Chrome(ChromeDriverManager().install())
url = "https://easternsnow.com/da"

# Open the website
driver.get(url)

# time.sleep(8)

# Select the id box
# test = driver.find_element(By.CSS_SELECTOR, "i.eicon-menu-bar") #works
# test = driver.find_element(By.XPATH, "//*[@id='header']/div/div/div[3]/div/div/section/div/div/div[2]/div/div/div/div/div/i") #works
# test = driver.find_element(By.CLASS_NAME, "eicon-menu-bar") #works
test = driver.find_element(By.CLASS_NAME, "elementor-menu-toggle")  # works

test.click()

time.sleep(3)
