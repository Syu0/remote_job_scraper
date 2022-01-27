import remoteok , stack_over_flow,wework_remotely

import datetime,asyncio

async def main():
    search_by = 'python'
    all_jobs = []
    start = datetime.datetime.now()
    
    print('hello')
    
    result = await asyncio.gather( wework_remotely.get_jobs(search_by),
        remoteok.get_jobs(search_by),
        stack_over_flow.get_jobs(search_by)
    )

    for jobs in result : 
        all_jobs.extend(jobs)

    print(len(all_jobs))
    await asyncio.sleep(1)
    end = datetime.datetime.now()
    print('process end : ', end - start )
    


if __name__ == "__main__":
    result = asyncio.run(main())
