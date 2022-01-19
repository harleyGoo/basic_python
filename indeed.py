import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = "https://www.indeed.com/jobs?as_and=python&limit={LIMIT}"


def extract_indeed_pages():
    result = requests.get(URL)  # print해보면 200이 나와야 OK.
    # print(result)

    soup = BeautifulSoup(result.text, "html.parser")

    pagination = soup.find(
        "div", {"class": "pagination"})  # div 중에 class명이 "pagination"인 요소를 추출.

    links = pagination.find_all('a')  # pagination안의 a요소를 모두 추출.
    pages = []
    for link in links[:-1]:  # Get all the links except the last one.
        pages.append(int(link.find(
            "span").string))  # same with pages.append(int(link.string))

    max_page = pages[-1]

    return max_page


def extract_indeed_jobs(last_pages):
  jobs = []
  for page in range(last_pages):
    print(f"Scrapping page {page}")
    result = requests.get(f"{URL}&start={page*LIMIT}")
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("a", {"class": "fs-unmask"})
    for html_result in results:
        job = extract_job(html_result)
        jobs.append(job)

  return jobs


def extract_job(html_result):
    title = html_result.find("h2", {
        "class": "jobTitle"
    }).find("span", title=True).text  # Chaning(체이닝)
    company = html_result.find("span", {"class": "companyName"})
    if company is not None:
        company_anchor = company.find("a")
        if (company_anchor is not None):
            company = company_anchor.text
        else:
            company = company.text
    #print(f"{title}: {company}")
    location = html_result.find("div", {"class": "companyLocation"}).text
    job_id = html_result["data-jk"]

    return {
        'title': title,
        'company': company,
        'location': location,
        'link': f"https://www.indeed.com/viewjob?jk={job_id}"
    }
