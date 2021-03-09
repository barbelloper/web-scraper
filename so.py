import requests
from bs4 import BeautifulSoup
LIMIT = 50
URL ="https://stackoverflow.com/jobs?r=true&q="
"""
These are the URLs that will give you remote jobs for the word 'python'

https://stackoverflow.com/jobs?r=true&q=python
https://weworkremotely.com/remote-jobs/search?term=python
https://remoteok.io/remote-dev+python-jobs

Good luck!
"""
headers = {
    'User-Agent':
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
}

def get_last_page(job_name):
    result = requests.get(URL+job_name['job'], headers=headers)
    soup = BeautifulSoup(result.text, "html.parser")
    pages = soup.find("div", {"class": "s-pagination"}).find_all("a")
    last_page = pages[-3].get_text(strip=True)
    return int(last_page)


def get_info(job_name,last_page):
  informs=[]
  for page in range(last_page):
    result = requests.get(URL+job_name['job']+f"&pg={(page+1)}",headers=headers)
    soup = BeautifulSoup(result.text, "html.parser")
    block = soup.find_all("div",class_="js-result")
    for info in block:
      link="https://stackoverflow.com"+info.find("a",class_="s-link")["href"]
      job_title=info.find("a",class_="s-link")["title"]
      company_name=info.find("h3").find("span").string
      informs.append({"title":job_title,"company_name":company_name,"link":link})

  return informs
  

