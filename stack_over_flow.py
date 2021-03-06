from bs4 import BeautifulSoup
import requests,asyncio,aiohttp


headers = {
    'referer': 'https://stackoverflow.com/jobs?q={search_by}',
    'user-agent': f'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
}
HOME = 'https://stackoverflow.com'

async def get_page_numbers(search_by='python'):
    page_numbers = []
    search_by = search_by.lower()
    URL = f"https://stackoverflow.com/jobs?q={search_by}&amp;so_source=JobSearch&amp;so_medium=Internal&amp;pg=1"
    
    headers = {
        'referer': 'https://stackoverflow.com/jobs?q={search_by}',
        'user-agent': f'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
    }
    async with aiohttp.ClientSession() as session:
        response =await session.get(URL, headers=headers)
        soup = BeautifulSoup(await response.text(), 'html.parser')
        
    try:
        atags= soup.find('div',{'class':'s-pagination'}).find_all('a',{'class':
        's-pagination--item'})[:-1]
        
        for atag in atags:  
            page_numbers.append(int(atag.get_text(strip=True)))
    except Exception:
        print("Faild to scraping Stack Over Flow site.")
    return page_numbers

async def  get_jobs(search_by):
    pages = await get_page_numbers(search_by)
    jobs = []
    async with aiohttp.ClientSession() as session:
        for last_page in pages:
            URL = f"https://stackoverflow.com/jobs?q={search_by}&amp;so_source=JobSearch&amp;so_medium=Internal&amp;pg={last_page}&sort=p"
            response = await session.get(URL,headers=headers)
            soup = BeautifulSoup(await response.text(), 'html.parser')
            divs = soup.find('div',{'class':'listResults'}).find_all('div',recursive=False)
            for div in divs :
                a_tag = div.find('h2').find('a')
                if a_tag : 
                    #job title
                    title = a_tag['title']
                
                    h3 = div.find('h3')
                    loc , office = h3.find_all('span')
                    company = loc.text.strip()
                    location = office.text.strip()
                    link = HOME + a_tag['href']
                    # place = f'{loc.text.strip()} ??? {office.text.strip()}'
                    jobs.append({'title' : title, 'location':location,'company':company, 'apply':link})        

    return jobs

if __name__ == "__main__":
    search_by = 'python'
    all_jobs = asyncio.run(get_jobs('nest'))
    print(len(all_jobs))
    
