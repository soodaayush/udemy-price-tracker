from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

url = 'https://www.udemy.com/courses/search/?src=ukw&q=Python'

driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))

driver.get(url)

print(driver.page_source)