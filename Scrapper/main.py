from bs4 import BeautifulSoup
import requests

base_url = "https://weworkremotely.com/remote-jobs/search?&term="
search_term = "python"



response = requests.get(f"{base_url}{search_term}")

if response.status_code != 200:
    print("Can't request website")
else:
    soup = BeautifulSoup(response.text, "html.parser")
    jobs = soup.findAll("section",class_="jobs")
    for job_section in jobs:
        job_post = job_section.find_all('li', class_="feature")
        for post in job_post:
            print(post)
            print("//////////////")

# def say_hello(name, age):
#     print(f"Hello {name} you are {age} years old")


# say_hello("gon", 12)
# say_hello(age=12, name="gon")


