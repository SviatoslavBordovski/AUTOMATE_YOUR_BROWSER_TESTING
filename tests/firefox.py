frm selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC

#FIREFOX BROWSER TEST

driver = webdriver.Firefox(executable_path='your\path\geckodriver')  #Don't forget to install gecko driver anb tell the path to it on the laptop (required)
driver.get('https://google.com')
driver.find_element_by_name('q').send_keys('Python is awesome')
wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.NAME, 'btnK')))

driver.find_element_by_name('btnK').click()
driver.close()
driver.quit()
