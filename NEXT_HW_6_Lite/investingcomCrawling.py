from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from datetime import datetime
from openpyxl import Workbook
import time

# Set up Selenium WebDriver
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_service = Service('C:/Users/Jeong/Desktop/NEXT/HW/NEXT_HW_6_Lite/chromedriver.exe')  # Update with the full path to your ChromeDriver executable

driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

try:
    url = 'https://www.musinsa.com/main/113?utm_source=google_shopping&utm_medium=sh&utm_campaign=pmax_ongoing&source=GOSHSAP001&utm_source=google_shopping&utm_medium=sh&utm_campaign=pmax_ongoing&source=GOSHSAP001&gad_source=1&gclid=CjwKCAjwg8qzBhAoEiwAWagLrIhYIuWm6vR3XHbMXlVqqBfDb6_t3wRA4Y-TkSGMiZyvU70xx8s3KxoCs1MQAvD_BwE'
    driver.get(url)
    time.sleep(5)  # Wait for the page to fully load

    # Locate the button using XPath or any other selector
    button = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/main/div/section[1]/div[1]/button[4]')
    button.click()  # Press the button
    print("Button has been pressed.")
    
    # You can add more code here to handle the next actions after pressing the button

except Exception as e:
    print(f"Error: {e}")

finally:
    driver.quit()
