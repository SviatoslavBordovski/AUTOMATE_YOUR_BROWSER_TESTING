from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC

#Tell the path to ChromeDriver on your laptop like in the example below (required)
driver = webdriver.Chrome('/home/sb/Desktop/chromedriverlinux/chromedriver')

#Lets set browser window size for test run
driver.set_window_size(1980,1080)

#What website in the browser should we open?
driver.get('https://google.com')

#What do we want to find?
driver.find_element_by_name('q').send_keys('Python is a programming language')

#Oh wait! Element on the webpage should be clickable, so we need to wait for a while...
wait = WebDriverWait(driver, 5)
element = wait.until(EC.element_to_be_clickable((By.NAME, 'btnK')))

#Click the button to start search
driver.find_element_by_name('btnK').click()

#Finish this test
print('Chrome UI test completed!')
driver.close()
driver.quit()
