import pandas as pd
import requests
from bs4 import BeautifulSoup
from html.parser import HTMLParser
import sys, os
import time
import argparse
import config

def getPrice(url):
	result = requests.get(url)
	bs_obj = BeautifulSoup(result.content, "html.parser")
	no_today = bs_obj.find("p", {"class": "no_today"})
	blind = no_today.find("span", {"class": "blind"})
	now_price = blind.text
	now_price = now_price.replace(",", "")
	now_price = int(now_price)
	return now_price

def get_code(df, name):
    if(code_df['name']==name).any():
        code = df.query("name=='{}'".format(name))['code'].to_string(index=False)
        code = code.strip()
        return code
    else:
        print("It is not in the list.")
        sys.exit()


def showResult(price):
	t = time.localtime()
	out = [t.tm_year, t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min, t.tm_sec, price]
	print(out)
	return

def compareValue(target_url, stock_name, target_price, current_price):
	if(target_price > current_price):
		return
	else:
		print("The current price is over target price!\n")
		print("The information sent to your email. check your email please\n")
		r = requests.post(target_url, data={"value1" : stock_name, 
				"value2" : str(target_price)+"원", "value3": str(current_price) +"원"})
		time.sleep(15)
		return

parser = argparse.ArgumentParser()
parser.add_argument('name', type=str,
            help="What is the name of stock?")
parser.add_argument('target_price', type=int,
                help="What is the target price?")
args = parser.parse_args()
code_name = args.name
target_price = args.target_price
code_df = pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download', header=0)[0]

code_df = code_df[['회사명', '종목코드']]
code_df.head()
code_df = code_df.rename(columns={'회사명': 'name', '종목코드': 'code'})
code_df.code = code_df.code.map('{:06d}'.format)

code = get_code(code_df, code_name)
target_url = config.target_url
url = "https://finance.naver.com/item/main.nhn?code={}".format(code)



os.environ['TZ'] = 'Asia/Seoul'
t = time.localtime()

while(t.tm_hour<=15 and t.tm_hour>=9):
    if(t.tm_hour == 15):
        while(t.tm_min < 30):
            price = getPrice(url)
            showResult(price)
            compareValue(target_url, code_name, target_price, price)
            if(t.tm_min >= 30):
                print("Market is closed.\n")
                break
    else:
        price = getPrice(url)
        showResult(price)
        compareValue(target_url, code_name, target_price, price)
