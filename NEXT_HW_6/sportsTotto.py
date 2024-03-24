from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime
import csv
from selenium.common.exceptions import TimeoutException

chromedriver_path ='C:/Users/Jeong/Desktop/NEXT/HW/NEXT_HW_6/chromedriver-win64/chromedriver.exe'
user_data_dir ="C:/Users/Jeong/Desktop/NEXT/HW/NEXT_HW_6"

chrome_options = Options()
chrome_options.add_argument(f"user-data-dir={user_data_dir}")
service = Service(executable_path=chromedriver_path)

driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get('https://betway.com/en/sports')
# wait = WebDriverWait(driver, 10)


element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div/div[3]/div/div[1]/div/div[1]/div[2]/div/div[2]/div[1]/div/div/div[1]/div')))
element.click()
element2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div/div[3]/div/div[1]/div/div[2]/div[4]/div/div[1]/div/div/div[2]/div/button/div[1]/div/a')))
element2.click()
driver.find_element(By.TAG_NAME,'body').send_keys(Keys.PAGE_DOWN)


today = datetime.now().strftime('%Y%m%d')

file = open(f'{today}bettingOdds.csv', mode="w", newline='')
writer = csv.writer(file)
writer.writerow(["date","match","home","draw", "away"])
for a in range(1,4):   
    for i in range(1, 8):
        match_xpath = "/html/body/div[1]/div/div[3]/div/div[1]/div/div[2]/div[4]/div/div[2]/div/div[3]/div/div[2]/div/div[3]/div[2]/div/div[" + str(a) + "]/div[2]/div/div[" + str(i) + "]/article/div[1]/div[1]/header/div/div/div/div[2]/a"
        home_xpath = "/html/body/div[1]/div/div[3]/div/div[1]/div/div[2]/div[4]/div/div[2]/div/div[3]/div/div[2]/div/div[3]/div[2]/div/div[" + str(a) + "]/div[2]/div/div[" + str(i) + "]/article/div[1]/div[2]/div/div/div[2]/div/div[2]/div[2]/div/div[4]/div"
        draw_xpath = "/html/body/div[1]/div/div[3]/div/div[1]/div/div[2]/div[4]/div/div[2]/div/div[3]/div/div[2]/div/div[3]/div[2]/div/div[" + str(a) + "]/div[2]/div/div[" + str(i) + "]/article/div[1]/div[2]/div/div/div[2]/div/div[2]/div[3]/div/div[4]/div"
        away_xpath = "/html/body/div[1]/div/div[3]/div/div[1]/div/div[2]/div[4]/div/div[2]/div/div[3]/div/div[2]/div/div[3]/div[2]/div/div[" + str(a) + "]/div[2]/div/div[" + str(i) + "]/article/div[1]/div[2]/div/div/div[2]/div/div[2]/div[4]/div/div[4]/div"
        date_xpath = "/html/body/div[1]/div/div[3]/div/div[1]/div/div[2]/div[4]/div/div[2]/div/div[3]/div/div[2]/div/div[3]/div[2]/div/div[" + str(a) + "]/div[1]/div[2]/div[1]"
        try:
            match = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, match_xpath)))
            home = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, home_xpath)))
            draw = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, draw_xpath)))
            away = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, away_xpath)))
            date = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, date_xpath)))
            match_txt = match.text
            home_txt = home.text
            draw_txt = draw.text
            away_txt = away.text
            date_txt = date.text
            print(date_txt,match_txt, home_txt, draw_txt, away_txt)
            writer.writerow([date_txt, match_txt, home_txt, draw_txt, away_txt])
        except TimeoutException:
                continue

file.close()
