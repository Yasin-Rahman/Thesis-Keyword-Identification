from urllib.request import urlopen,Request
from bs4 import BeautifulSoup as soup
# range= 2489
for page_num in range(1,2):
	url = "https://www.prothomalo.com/sports/article?page=132"
	print(url)

# Opening up connection, grabbing the page
headers={'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7',} 
req = Request(url, None, headers)
uClient = urlopen(req)
page_html = uClient.read()
uClient.close()

# HTML parser
page_soup = soup(page_html, "lxml")

page_links = page_soup.find("div",{"class": "row"}).find_all("a",{"class": "link_overlay"})
print(len(page_links))
for page_link in page_links:
	addition_part = page_link.get("href")
	full_link = "http://www.prothomalo.com" + str(addition_part)
	print(full_link)
	print("\n")

	# Opening up connection, grabbing the page
	cClient = urlopen(full_link)
	comment_html = cClient.read()
	cClient.close()
	comment_soup = soup(comment_html, "lxml")
	comment_portion = comment_soup.find("div", {"class": "right_title"}).find("h1", {"class":"title mb10"}).text
	print(comment_portion)
	# print(len(comment_portion))
	cmnt_file_name = "Test_Title1.txt"
	cf = open(cmnt_file_name, "a", encoding='utf-8')
	cf.write(comment_portion)
	cf.write("\n")

	# print(page_links)
	
	cf.close()
