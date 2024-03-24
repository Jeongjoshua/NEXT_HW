from bs4 import BeautifulSoup as bs
import requests
from datetime import datetime
from openpyxl import Workbook

url= 'https://www.investing.com/indices/major-indices'

try:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    #응답상태 확인
    if response.status_code == 200:
        html_text = response.text
        #step5.beautifulsoup에서 
        soup = bs(response.text, 'html.parser')
        #제목
        name=soup.find_all(class_="block overflow-hidden text-ellipsis whitespace-nowrap")
        name = list(map(lambda x: x.text.strip(), name))
        print(name)
        
        lastPrice=soup.find_all(class_="datatable-v2_cell__IwP1U dynamic-table-v2_col-other__zNU4A text-right rtl:text-right")
        lastPrice = list(map(lambda x: x.text.strip(), lastPrice))
        print(lastPrice)

        
        chgPercentage = soup.find_all(class_="datatable-v2_cell__IwP1U datatable-v2_cell--down__sYmZ4 datatable-v2_cell--bold__cXQUV dynamic-table-v2_col-other__zNU4A text-right font-bold rtl:text-right")
        chgPercentage = list(map(lambda x: x.text.strip(), chgPercentage))
        print(chgPercentage)
        
        wb = Workbook()
        ws = wb.active
        
        ws.append(["시장", "종가", "변동률"])
        
        for i, (name, lastPrice, chgPercentage) in enumerate(zip(name, lastPrice, chgPercentage), start=1):
            ws.append([name, lastPrice, chgPercentage])
        #날짜
        today = datetime.now().strftime('%Y%m%d')
        
        filename = f'stockMarketIndex_{today}.csv'
        wb.save(filename)
        print(f"엑셀에 저장 완료: {filename}")
    else: 
        print(f"Error: HTTP 요청실패. 상태코드{response.status_code}")
        
except requests.exceptions.RequestException as e:
     print(f"Error: 요청 중 오류 발생. 오류 메세지{e}")