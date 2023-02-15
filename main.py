import os
import time
from urllib.parse import urlparse
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import urllib.request
from datetime import datetime


                ######### For headless   #########
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")

driver = webdriver.Chrome((ChromeDriverManager().install()), options=chrome_options)

                ######### For not headless  #########
#driver = webdriver.Chrome(ChromeDriverManager().install())
print("Uh, hold on a sec. Once we finish downloading those images, we'll show you the directory they're saved in. Thanks for your patience.")
driver.maximize_window()
driver.implicitly_wait(5)

                ######### For Dynamic input by terminal  #########
#baseUrl = input("Input Url from which page you want to downlaod photo:")

                ######### For Static input by terminal  #########
baseUrl = "https://www.munna.cyou/"
driver.get(baseUrl)

                ######### Check www  #########

if("www" in baseUrl):
    domainNameParse = urlparse(baseUrl).hostname
    domainName = domainNameParse.split('.')[1]
else:
    domainNameParse = urlparse(baseUrl).hostname
    domainName = domainNameParse.split('.')[0]


                ######### For collect Current datetime  #########
dateTime = datetime.now().strftime("%Y%m%d-%H%M%S")
directoryName = domainName + dateTime
os.mkdir("Photos" + "/" + directoryName)

imageTag = []

                ######### Scroll Top to bottom   #########
height = driver.execute_script("return document.body.scrollHeight")
scrollSpeed = 1
scrollPauseTime = 0
while scrollSpeed > 0:
    scrollSpeed -= 1
    for x in range(0, height, 5):
        driver.execute_script(f"window.scrollTo(0, {x});")
        imageTag.extend(driver.find_elements(By.TAG_NAME, 'img'))
        time.sleep(scrollPauseTime)

imageTag = set(imageTag)
i = 1
for images in imageTag:
    imageSrc = images.get_attribute('src')
    try:
        urllib.request.urlretrieve(imageSrc,( "Photos" + "/" + directoryName + "/" + domainName + str(i) +".png" ))
        i = i+1
    except:
        continue
print("Images are here: Photos/"+directoryName)



