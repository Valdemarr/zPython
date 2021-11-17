import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import pyautogui

URL = 'https://www.google.com/'
search_term = "Avengers Endgame"

driver = webdriver.Chrome(ChromeDriverManager().install())
action = ActionChains(driver)
driver.get(URL)

agree_to_terms = driver.find_element_by_xpath('//*[@id="L2AGLb"]/div').click()

time.sleep(2)

# SEARCH FOR KEYWORD
search = driver.find_element_by_name('q')
search.send_keys(search_term)
search.send_keys(Keys.RETURN)

time.sleep(1)

# SWITCH TO IMAGE TAB
image_tab = driver.find_element_by_xpath('//*[@id="hdtb-msb"]/div[1]/div/div[2]/a').click()

time.sleep(1)

# CLICK THUMBNAIL
thumbnail_click = driver.find_element_by_xpath(
    '//*[@id="islrg"]/div[1]/div[1]/a[1]/div[1]/img').click()

time.sleep(1)

# RIGHT CLICK AND SAVE, RENAME AND NOTHING
required_image = driver.find_element_by_xpath(
    '//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div/a/img')
action.context_click(required_image).perform()
pyautogui.moveTo(796, 717, duration=1)
time.sleep(2)
pyautogui.leftClick()

pyautogui.write(f"{search_term} - {str(time.monotonic())}")

pyautogui.hotkey("enter")

time.sleep(2)
