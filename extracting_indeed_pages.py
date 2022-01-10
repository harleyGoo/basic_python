import requests
from bs4 import BeautifulSoup

indeed_result = requests.get("https://www.indeed.com/jobs?as_and=python&limit=50") # print해보면 200이 나와야 OK.

indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")
# print(indeed_soup)

pagination = indeed_soup.find("div", {"class": "pagination"}) # div 중에 class명이 "pagination"인 요소를 추출.

links = pagination.find_all('a') # pagination안의 a요소를 모두 추출.
pages = []
for link in links[:-1]: # Get all the links except the last one.
  pages.append(int(link.find("span").string)) # same with pages.append(int(link.string))

max_page = pages[-1]
