import time
from selenium import webdriver

browser = webdriver.Chrome()


browser.get("https://translate.google.com/?hl=ru")

time.sleep(3)

expectedResult = "Привет"
browser.find_element_by_css_selector('[jsname="BJE2fc"]').send_keys("Hello")

time.sleep(3)

actualResult = browser.find_element_by_css_selector('[jsname="W297wb"]').text

assert actualResult == expectedResult

