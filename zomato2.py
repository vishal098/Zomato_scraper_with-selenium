from zomato import *

# delhi=zomato_scrape()
# # print(delhi)
# def _input(delhi):
# 	ask=input('enter the palace name').lower()
# 	for i in delhi:
# 		# print(i['name'])
# 		if ask == i['name'].lower():
# 			return i['url']
# 	else:
# 		return('invalid name')
# url=_input(delhi)

if os.path.exists("zomato.data"):
	with open("zomato1.json","r") as z:
		zz=json.load(z)
		zz=json.loads(zz)
else:	                            # Waiting function  
	driver = webdriver.Chrome(ChromeDriverManager().install())
	driver.get('https://www.zomato.com/ncr/connaught-place-delhi-restaurants')
	page=driver.execute_script("return document.documentElement.outerHTML")
	soup=BeautifulSoup(page,'html.parser') 
	page1=soup.find('div',class_='card  search-snippet-card     search-card  ')
	
	page2=page1.find('div',class_="res-snippet-small-establishment mt5")
	print(page2)
	# for i in page2:
	# 	print(i,'\n')
	driver.quit()
	time.sleep(1)