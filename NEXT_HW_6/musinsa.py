import requests
from bs4 import BeautifulSoup as bs
from datetime import datetime
from openpyxl import Workbook
url = 'https://www.musinsa.com/ranking/best'

try:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        html_text = response.text

        soup = bs(response.text, 'html.parser')

        # 상품 목록을 담고 있는 요소를 찾습니다.
        brand = soup.find_all(class_='item_title')
        brand = list(map(lambda x: x.text.strip(), brand))
        print(brand)        
        
        products = soup.find_all(class_='list_info')
        products = list(map(lambda x: x.text.strip(), products))
        print(products)
        
        wb = Workbook()
        ws = wb.active
        
        ws.append(["순위", "브랜드", "제품명"])
        
        for i, (brand, products) in enumerate(zip(brand, products), start=1):
            ws.append([i, brand, products])

        today = datetime.now().strftime('%Y%m%d')
        
        filename = f'musinsa_rank_{today}.xlsx'
        wb.save(filename)
        print(f"엑셀 파일 저장 완료: {filename}")
    else:
        print(f"Error: HTTP 요청 실패. 상태 코드: {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"Error: 요청 중 오류 발생. 오류 메시지: {e}")
