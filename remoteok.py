
# https://remoteok.com/

 
from email.policy import default
import aiohttp
from bs4 import BeautifulSoup 
import requests ,asyncio,aiohttp
HOME = 'https://remoteok.com'
headers = {
    'referer': 'https://remoteok.com/',
    'user-agent': f'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
}


async def  get_jobs(search_by='python'):
    jobs = []
    async with aiohttp.ClientSession() as session:
        URL = 'https://remoteok.com/remote-python-jobs'
        response = await session.get(URL,headers=headers)        
        soup = BeautifulSoup(await response.text(), 'html.parser')
    

    tr_tags = soup.find_all('tr',{'class':'job'})    
    for tr in tr_tags :        
        job = tr.find('td',{'class':'company'})
        if job :
            company = job.find('span').find('h3').get_text()            
            title = job.find('a').find('h2').get_text().replace('\n','')
            apply = URL + job.find('a')['href']
            location= job.find('div',{'class':'location'}).get_text()        
 
            jobs.append({'title' : title, 'location':location, 'company':company, 'apply':apply})        

    return jobs

if __name__ == "__main__":
    search_by = 'python'
    all_jobs = asyncio.run(get_jobs('nest'))
    print(len(all_jobs))
    
