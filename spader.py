from selenium import webdriver
import time
from bs4 import BeautifulSoup
import json

def get_url(key):
	return "https://www.yfull.com/snp-list/?page="+ str(key)

def get_data(url):
	result=[]
	browser = webdriver.Chrome(executable_path="d:/tools for spader/chromedriver.exe")
	browser.get(url)
	content = browser.page_source.encode('utf-8')
	soup=BeautifulSoup(content,"lxml")
	tr = soup.find_all('tr')
	for i in tr:
		temp=[]
		infos=i.find_all('td')
		for info in infos:
			if info.a:
				temp.append(info.a.string)
			else:
				temp.append(info.string)
			# temp.append(info.string)
		if len(temp)>8:
			result.append(temp)
	return result

def save_json(name,data):
    with open(name,'w') as f:
        json.dump(data,f)

if __name__=='__main__':
	for i in range(147,168):
		url = get_url(i)
		data = get_data(url)
		save_json('new_data/'+str(i) + '.json', data)
		time.sleep(15)
