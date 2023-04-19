from random import randint
import requests

web_sites = (
    "google.com",
    "facebook.com",
    "tiktok.com",
    "airbnb.com"
)

result = {
    
}

for site in web_sites:
    if not site.startswith('https://'):
        web_site = f"https://{site}"
        response = requests.get(web_site)
        if(response.status_code == 200):
            result[web_site] = 'OK'
        else:
            result[web_site] = 'FAILED'

print(result)