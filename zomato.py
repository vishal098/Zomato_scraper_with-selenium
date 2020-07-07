# from selenium import webdriver
# import pandas as pd
# import selenium
# import requests
# driver=webdriver.Chrome('/home/bijusrt/Downloads/to/chromedriver')
# url=('http://www.zomato.com/india')
# r=driver.get(url)
# print(r)
# print(r.content.decode())


# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager 
# from bs4 import BeautifulSoup               
# import time,pprint,json,os
# if os.path.exists("zomato data"):
# 	with open("zomato.json","r") as z:
# 		zz=json.load(z)
# 		zz=json.loads(zz)
# 	pprint.pprint(zz)
# else:                                  # Waiting function  
# 	URL = 'https://www.zomato.com/ncr/restaurants'      # Define URL 
# 	driver = webdriver.Chrome(ChromeDriverManager().install())
# 	driver.get(URL)
# 	page=driver.execute_script("return document.documentElement.outerHTML")
# 	# print(page)
# 	driver.quit()
# 	time.sleep(1)

# 	soup=BeautifulSoup(page,"lxml")
# 	b=soup.find("div",class_="ui cards",id="orig-search-list")
# 	b=b.findAll("div",class_="content")
# 	g=[]
# Actions
 
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager 
from bs4 import BeautifulSoup               
import time,pprint,json,os
def zomato_scrape():
	if os.path.exists("zomato.json"):
		with open("zomato.json","r") as z:
			zz=json.load(z)
			zz=json.loads(zz)
		return zz
	else:
		empty=[]
		                            # Waiting function  
		URL = 'https://www.zomato.com/ncr'    # Define URL 
		driver = webdriver.Chrome(ChromeDriverManager().install())
		driver.get(URL)
		page=driver.execute_script("return document.documentElement.outerHTML")
		soup=BeautifulSoup(page,'html.parser') #u can use lxmx also
		# print(soup.prettify())
		# clearfix=soup.find('div',class_="pbot clearfix")
		ui=soup.find('div',class_="ui segment row")
		a=ui.findAll('a')
		for i in a:
			dic1={'name':'','url':''}
			name=(i.text.split('(')[0].strip("\n").strip())
			dic1['name']=name
			dic1['url']=i['href']
			empty.append(dic1)
		with open("zomato.json","w+") as file:
			c=json.dumps(empty)
			c=json.dump(c,file)
		driver.quit()
		time.sleep(1)

if __name__=='__main__':
	pprint.pprint(zomato_scrape())
