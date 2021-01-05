from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options 
import time

PATH = "/home/hackrimony/Videos/yeah/chromedriver"




extension_path = '/home/hackrimony/Desktop/extension_2_7_0_0.crx'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_extension(extension_path)
driver = webdriver.Chrome(executable_path=PATH, chrome_options=chrome_options) 


driver.get("http://www.mangareader.net/martial-peak")
time.sleep(40)

for x in range(169,617):
    actions = ActionChains(driver)
    search = driver.find_element_by_id("pdfButton_"+ str(x))
    time.sleep(30)
    search.click()
    time.sleep(50)
    search.click()
    actions.perform()

time.sleep(5)

driver.quit()
