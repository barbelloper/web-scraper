import requests
from bs4 import BeautifulSoup
LIMIT = 50
URL ="https://weworkremotely.com/remote-jobs/search?term="
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


def get_info(job_name):
  informs=[] 
  result = requests.get(URL+job_name['job'],headers=headers)
  soup = BeautifulSoup(result.text, "html.parser")
  block = soup.find_all("li",class_="feature")
  for info in block:
    link="https://weworkremotely.com"+info.find("a")["href"]
    job_title=info.find("span",class_="title").string
    company_name=info.find("span",class_="company").string
    informs.append({"title":job_title,"company_name":company_name,"link":link})

  return informs
  

