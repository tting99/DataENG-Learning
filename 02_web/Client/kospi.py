# kodpi.py

import requests
from bs4 import BeautifulSoup

#pip install requests 해서 requests설치
res = requests.get('https://finance.naver.com/sise/')
# res.text하면 그 페이지의 html을 다 가져온다 하지만 거기서 작업할려면 이 구문을 이해시켜야 하는 과정이 필요(파싱)
# 그렇기 때문에 pip install beautifulsoup4 을 해줘서 파싱을 진행해보자. 깔고 임포트 해주기.

soup = BeautifulSoup(res.text, 'html.parser') #"해석을 할것은 res.text이고 해석할 방법은 html.parser이다" 라는 말.
# print(soup.title)

# print(type(soup.title))
tag = soup.select_one('#KOSPI_NOW') # 내가 가져오고자 하는 데이터의 id를 셀렉트뒤에 넣고 이 값을 출력해볼게

print(soup.select('#KOSPI_NOW'))