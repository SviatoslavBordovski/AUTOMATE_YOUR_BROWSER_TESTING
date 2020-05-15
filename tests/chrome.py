from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC

#Tell the path to chromedriver on your laptop like in the example below (required)
driver = webdriver.Chrome('/home/sb/Desktop/chromedriverlinux/chromedriver')

#Lets set browser window size for test run
driver.set_window_size(1980,1080)

#What website should we open?
driver.get('https://google.com')

#What do we find and type?
driver.find_element_by_name('q').send_keys('Python is awesome')

#Oh wait! This should be clickable, so we need to wait for a while ...
wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.NAME, 'btnK')))

#Click me, geeez!
driver.find_element_by_name('btnK').click()

#Finish test
print('Chrome UI test completed!')
driver.close()
driver.quit()
