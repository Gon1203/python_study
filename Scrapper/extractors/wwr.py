from bs4 import BeautifulSoup
import requests

def extract_wwr_jobs(keyword):
    base_url = "https://weworkremotely.com/remote-jobs/search?&term="
    search_term = keyword
    
    response = requests.get(f"{base_url}{search_term}")

    if response.status_code != 200:
        print("Can't request website")
    else:
        results = []
        soup = BeautifulSoup(response.text, "html.parser")
        jobs = soup.findAll("section",class_="jobs")
        for job_section in jobs:
            job_post = job_section.find_all('li', class_="feature")
            for post in job_post:
                anchors = post.find_all('a')
                anchor = anchors[1]
                link = anchor['href']
                company, kind, region = anchor.find_all('span',class_="company")
                title = anchor.find('span',class_="title")
                job_data = {
                    'company' : company.string,
                    'kind':kind.string,
                    'region': region.string,
                    'title':title.string
                }
                results.append(job_data)
        return results