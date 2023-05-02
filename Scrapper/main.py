# from requests import get
from extractors.wwr import extract_wwr_jobs
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


options = Options()
options.add_experimental_option("detach", True)
options.add_argument("--no-sandbox")
options.add_argument('--disable-dev-shm-usage')

base_url = "https://kr.indeed.com/jobs?q=python&limit=50"

browser = webdriver.Chrome(options=options)


browser.get(base_url)

print(browser.page_source)



# search_term = "python"


# headers= {
#     "Accept": "*/*", 
#     "Accept-Encoding": "gzip, deflate", 
#     "Host": "httpbin.org", 
#     "User-Agent": "python-requests/2.26.0", 
# }


# # response = get(f"{base_url}{search_term}",headers=headers )
# response = get(base_url)


# if(response.status_code == 200):
#     print(response.text)
# else:
#     print(response.status_code)
#     print(response.headers)
    

