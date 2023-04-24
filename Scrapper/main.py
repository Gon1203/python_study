from requests import get
from extractors.wwr import extract_wwr_jobs

base_url = "https://kr.indeed.com/jobs?q="
search_term = "python"


headers= {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.26.0", 
}


response = get(f"{base_url}{search_term}",headers=headers )


if(response.status_code == 200):
    print(response.text)
else:
    print(response.status_code)
    print(response.headers)
    

