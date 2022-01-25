"""
These are the URLs that will give you remote jobs for the word 'python'

https://stackoverflow.com/jobs?r=true&q=python
https://weworkremotely.com/remote-jobs/search?term=python
https://remoteok.io/remote-dev+python-jobs

Good luck!
"""


from flask import Flask, render_template,redirect,request, send_file
import stack_over_flow as sof
import remoteok as remok
import wework_remotely as wework
from exporter import save_to_file
app = Flask("JobScrapper")
fakeDB = {}

@app.route('/')
def hello_world():
    return render_template('search.html')

@app.route('/search')
def search():
  return render_template('search.html')

@app.route('/report')
def report():
  word = request.args.get('word')
  count = 0
  existingJobs = []
  if word:
    print(f'Searching by {word}')
    word= word.lower()
    
    fromDb = fakeDB.get(word)

    if fromDb:
      existingJobs = fakeDB[word]
    else:
      existingJobs.extend( sof.get_jobs(word) )
      existingJobs.extend( remok.get_jobs(word) )
      existingJobs.extend( wework.get_jobs(word) )
      count= len(existingJobs)
      fakeDB[word] = existingJobs
      
    print('Search result :' ,count)

  else:
    redirect("/")
  

  return render_template('report.html',search_by=word,count=count,jobs=existingJobs)

@app.route('/export')
def export():
  try:
    word = request.args.get('word')
    if not word:
      raise Exception()
    word= word.lower()
    jobs = fakeDB.get(word)
    if not jobs:
      raise Exception()

    save_to_file(jobs)

    return send_file("jobs.csv")

  except:
    redirect("/")




app.run()