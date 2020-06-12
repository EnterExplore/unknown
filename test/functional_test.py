from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get('http://47.112.201.214:80')
print(driver.title)

driver.find_element_by_xpath('/html/body/div/div/form/p/input[1]').send_keys('印度')
time.sleep(2)
driver.find_element_by_xpath('/html/body/div/div/form/p/input[2]').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="navigation"]/p[1]/big/a').click()
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[3]/table/tbody/tr[2]/td/a').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="basic"]/p[2]/a').click()

time.sleep(5)