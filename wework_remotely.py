
# https://weworkremotely.com/

 
 
from bs4 import BeautifulSoup
import requests
HOME = 'https://weworkremotely.com'
headers = {
    'referer': '{HOME}/remote-jobs/search?term={search_by}',
    'user-agent': f'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
}


def  get_jobs(search_by):
    jobs = []
    
    URL = f"https://weworkremotely.com/remote-jobs/search?term={search_by}"
    response = requests.get(URL,headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    categories = soup.find_all('section',{'class':'jobs'})
    for article in categories :
        li_list = article.find('ul').find_all('li')
        
        for li in li_list:
            spans = li.find_all('span',{'class':'company'})            
            if len(spans) == 0:
                continue

            if len(spans) == 2 : 
                company_name, job_type = li.find_all('span',{'class':'company'})
                region = ''
                company_name = company_name.get_text()
            elif len(spans) >2 : 
                company_name, job_type, region = li.find_all('span',{'class':'company'})
                company_name = company_name.get_text()
            title = li.find('span',{'class':'title'})
            if title :
                title = title.get_text().strip()
            if job_type and region:
                location = job_type.get_text().strip() + '/' + region.get_text().strip()
            link = HOME + li.find('a')['href']
            jobs.append({'title' : title, 'location':location, 'company':company_name,'apply':link})        

    return jobs

if __name__ == "__main__":
    search_by = 'dd'
    all_jobs = get_jobs(search_by) 
    print(all_jobs)
