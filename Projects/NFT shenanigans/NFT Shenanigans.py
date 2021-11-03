from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

# Using Chrome to access web
driver = webdriver.Chrome(ChromeDriverManager().install())
url = "https://tinkersynth.com/slopes/"

# Open the website
driver.get(url)

time.sleep(7)

# Select the id box
id_box = driver.find_element_by_class_name(
    "UnstyledButton-lw1m82-0 Button__Wrapper-ikf7gj-0 Button__LargeButton-ikf7gj-2 hJLKbV")

time.sleep(7)

id_box.click()

time.sleep(7)

png = driver.find_element_by_class_name("DownloadVariant__Overlay-sc-3v1shs-2 cnnBWt")
png.click()
