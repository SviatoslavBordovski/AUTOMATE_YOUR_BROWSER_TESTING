from selenium import webdriver                  
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC

#CHROME BROWSER TEST

#Tell the path to chromedriver on your computer (required)
driver = webdriver.Chrome("/home/sb/Desktop/chromedriverlinux/chromedriver")

#Lets set browser window size
driver.set_window_size(1980,1080)

#Where we go?
driver.get('https://google.com')

#What do we find and type?
driver.find_element_by_name('q').send_keys('Python is awesome')

#Oh wait! This should be clickable... o_O
wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.NAME, 'btnK')))

#Click me, geeez
driver.find_element_by_name('btnK').click()

#Take care, sweety!
driver.quit()

#FIREFOX BROWSER TEST
driver = webdriver.Firefox()  #Don't forget to install gecko driver anb tell the path to it on the laptop (required)
driver.get('https://google.com')
driver.find_element_by_name('q').send_keys('Python is awesome')
wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.NAME, 'btnK')))

driver.find_element_by_name('btnK').click()
driver.quit()
