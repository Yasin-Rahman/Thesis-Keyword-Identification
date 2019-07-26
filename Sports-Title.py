from urllib.request import urlopen
from bs4 import BeautifulSoup as soup

# range= 2489
for page_num in range(1, 2):
#for i in range(93,141):
		my_url = "https://www.prothomalo.com/sports/article?page=110"
		uClient=urlopen(my_url)
		page_html=uClient.read()
		uClient.close
		page_soup = soup(page_html, "lxml")
		page_links = page_soup.find("div", {"class": "row"}).find_all("a", {"class": "link_overlay"})
		print(len(page_links))
		for page_link in page_links:
			addition_part = page_link.get("href")
			full_link = "http://www.prothomalo.com" + str(addition_part)
			cClient = urlopen(full_link)
			comment_html = cClient.read()
			cClient.close()
			comment_soup = soup(comment_html, "lxml")
			comment_portion = comment_soup.find("div", {"class": "right_title"}).find("h1",{"class": "title mb10"}).text
			print("\n")
			print(comment_portion)
			cmnt_file_name = "Test_Title1.txt"
			cf = open(cmnt_file_name, "a", encoding='utf-8')
			cf.write(comment_portion)
			cf.write("\n")

			cf.close()




