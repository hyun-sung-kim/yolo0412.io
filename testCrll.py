### 파이썬 크롤링 테스트 ###
import requests
from bs4 import BeautifulSoup

baseaddress = "https://finance.naver.com/sise/sise_market_sum.naver"
res = requests.post(baseaddress, data={'page':'1','fieldIds':[1,2,3,4,5,6] ,'sosok':'1'})
soup = BeautifulSoup(res.content,'html.parser')
section = soup.find('tbody')
items = section.find_all('tr', onmouseover="mouseOver(this)")

for item in items:
    basic_info = item.get_text()
    sinfo = basic_info.split("\n")
    print("\t" + sinfo[1] + "\t\t" + sinfo[2] + "\t\t\t" + sinfo[3])

# def return_value(address):
#     res = requests.get(address)
#     soup = BeautifulSoup(res.content,'html.parser')

#     section = soup.find('tbody')
#     items = section.find_all('tr', onmouseover="mouseOver(this)")
#     for item in items:
#         basic_info = item.get_text()
#         sinfo = basic_info.split("\n")
#         print("\t" + sinfo[1] + "\t\t" + sinfo[2] + "\t\t\t" + sinfo[3])

# baseaddress = "https://finance.naver.com/sise/sise_market_sum.naver?&page="

# for i in range(1,3):
    # return_value(baseaddress+str(i))
