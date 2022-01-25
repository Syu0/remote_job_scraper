import remoteok , stack_over_flow,wework_remotely


if __name__ == "__main__":
    search_by = 'python'
    all_jobs = []
    all_jobs.extend(remoteok.get_jobs(search_by) ) 
    all_jobs.extend(stack_over_flow.get_jobs(search_by) ) 
    all_jobs.extend(wework_remotely.get_jobs(search_by) )
    
    print(len(all_jobs))
