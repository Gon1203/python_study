web_sites = (
    "google.com",
    "airbnb.com",
    "twitter.com",
    "facebook.com",
    "tiktok.com"
)
count = 0

for site in web_sites:

    ## not is same with === false 
    if not (site.startswith("https://")):
        web_site = f"https://{site}"
        print(web_site)

    
