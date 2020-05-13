from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC

#Install geckodriver and tell the path to it on the laptop like in the example below (required)
driver = webdriver.Firefox(executable_path='/home/incognito/Desktop/chromedriverlinux/chromedriver')

#Where do we go?
driver.get('https://google.com')

#Find the input field on the page and type the text that should be found
driver.find_element_by_name('q').send_keys('Python is a programming language')
wait = WebDriverWait(driver, 10)

#Click find on the button 'Google search'
element = wait.until(EC.element_to_be_clickable((By.NAME, 'btnK')))
driver.find_element_by_name('btnK').click()

#Finish test
print('Test completed!')
driver.close()
driver.quit()
