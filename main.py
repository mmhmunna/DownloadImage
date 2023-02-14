import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import urllib.request

'''
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")

driver = webdriver.Chrome((ChromeDriverManager().install()), options=chrome_options)
'''
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
baseUrl = input("Input Url from which page you want to downlaod photo:")
if (baseUrl[0:8] == "https://"):
    baseurl = baseUrl
else:
    baseurl = "https://"+baseUrl
driver.get(baseUrl)
title = driver.title
imageTag = driver.find_elements(By.TAG_NAME,'img')
i = 1
for images in imageTag:
    imageSrc = images.get_attribute('src')
    try:
        urllib.request.urlretrieve(imageSrc,("Photos" + '/' + title +"/" + "photo"+ str(i) +".png" ))
        i = i+1
    except:
        continue


