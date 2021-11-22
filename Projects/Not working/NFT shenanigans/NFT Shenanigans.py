from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

# Using Chrome to access web
driver = webdriver.Chrome(ChromeDriverManager().install())
url = "https://color-wander.surge.sh/"
action_chains = ActionChains(driver)

# Open the website
driver.get(url)

time.sleep(2)

# Select the id box
#test = driver.find_element(By.CLASS_NAME, "eicon_menu_bar").click()
# test = driver.find_element_by_xpath("//button[@class='DestructiveCluster__ButtonWrapper-sc-1r2htg2-4 losDRq']").click()
test = driver.find_element(
    By.CSS_SELECTOR, "button.UnstyledButton-lw1m82-0 BigOminousButton__Button-sc-11cjywl-0 hgQwJV")

test.click()

time.sleep(3)
