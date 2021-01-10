import requests
from bs4 import BeautifulSoup

URL = f"https://stackoverflow.com/jobs?q=python&sort=i"

def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    pages = soup.find("div", {"class": "s-pagination"}).find_all("a")
    last_page = pages[-2].get_text(strip=True)
    return int(last_page)

def extract_job(html):
    #title = html.find("div", {"class":"-title"}).find("h2").find("a")["title"]
    title = html.find("h2").find("a")["title"]
    row = html.find("h3").find_all("span")
    company = row[0].get_text(strip=True)
    location = row[1].get_text(strip=True)
    job_id = html['data-jobid']
    return {"title": title, "company": company, "location": location, "link": f"https://stackoverflow.com/jobs/{job_id}"}

def extract_jobs(last_page):
    print("Starting SO...")
    jobs = []
    for page in range(last_page):
        result = requests.get(f"{URL}&pg={page+1}")
        print(f"Scrapped SO Page {page+1} of {last_page}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class":"-job"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs

def get_jobs():
    last_page = get_last_page()
    jobs = extract_jobs(last_page)
    return jobs

