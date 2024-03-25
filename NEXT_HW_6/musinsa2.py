from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from datetime import datetime
import csv
chromedriver_path = 'C:/Users/dowonkim/Desktop/NEXT/HW/NEXT_HW_6/chromedriver-win64/chromedriver-win64/chromedriver.exe'
user_data_dir = "C:/Users/dowonkim/Desktop/NEXT/HW/NEXT_HW_6/cash"

chrome_options = Options()
chrome_options.add_argument(f"user-data-dir={user_data_dir}")
service = Service(executable_path=chromedriver_path)

driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get('https://www.musinsa.com/app/')

rankbtn = driver.find_element(By.XPATH, '//*[@id="topCommonPc"]/header/div[2]/nav/ul/li[3]/a')
rankbtn.click()
time.sleep(3)

today = datetime.now().strftime('%Y%m%d')

file = open(f'{today}musinsa.csv', mode="w", newline='')
writer = csv.writer(file)
writer.writerow(["rank", "brand", "product"])


infos = driver.find_elements(By.XPATH, '//*[@id="goodsRankList"]/li')
for i, info in enumerate(infos[:50], start=1):
    rank = i
    brand = info.find_element(By.XPATH, './div[3]/div[2]/p[1]/a').text
    product = info.find_element(By.XPATH, './div[3]/div[2]/p[2]/a').text
    
    writer.writerow([rank, brand, product])

file.close()
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

while True:
    pass
