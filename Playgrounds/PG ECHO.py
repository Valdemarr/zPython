import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import pyautogui

# DOWNLOAD AND NAME
URL = 'https://color-wander.surge.sh/'

driver = webdriver.Chrome(ChromeDriverManager().install())
action = ActionChains(driver)
driver.get(URL)

# When real time comes, wait 15 seconds in total
time.sleep(3)

# RIGHT CLICK AND SAVE, RENAME AND NOTHING
image = driver.find_element(By.ID, "canvas")
action.context_click(image).perform()
pyautogui.moveTo(548, 588, duration=1)
time.sleep(1)
pyautogui.leftClick()

time.sleep(1)

pyautogui.write(str(time.monotonic()))

pyautogui.hotkey("enter")

time.sleep(2)

# CROP
