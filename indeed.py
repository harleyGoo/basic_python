import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = "https://www.indeed.com/jobs?as_and=python&limit={LIMIT}"

def extract_indeed_pages():
  result = requests.get(URL) # print해보면 200이 나와야 OK.

  soup = BeautifulSoup(result.text, "html.parser")

  pagination = soup.find("div", {"class": "pagination"}) # div 중에 class명이 "pagination"인 요소를 추출.

  links = pagination.find_all('a') # pagination안의 a요소를 모두 추출.
  pages = []
  for link in links[:-1]: # Get all the links except the last one.
    pages.append(int(link.find("span").string)) # same with pages.append(int(link.string))

  max_page = pages[-1]

  return max_page

def extract_indeed_jobs(last_pages):
  jobs = []
  #for page in range(last_pages):
  result = requests.get(f"{URL}&start={0*LIMIT}")
  
  soup = BeautifulSoup(result.text, "html.parser")
  results = soup.find_all("a", {"class": "fs-unmask"})
  for result in results:
    title = result.find("h2", {"class": "jobTitle"}).find("span", title=True).text  # Chaning(체이닝)
    print(title)

  return jobs