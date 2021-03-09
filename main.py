import requests
from flask import Flask, render_template, request,send_file,redirect
from so import get_info as get_so_info
from so import get_last_page
from remote import get_info as get_rm_info
from wework import get_info as get_we_info
from exporter import save_to_file

"""
These are the URLs that will give you remote jobs for the word 'python'

https://stackoverflow.com/jobs?r=true&q=python
https://weworkremotely.com/remote-jobs/search?term=python
https://remoteok.io/remote-dev+python-jobs

Good luck!
"""

app = Flask("My_job_scraper")
db={}


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/read")
def read():
  arguments = request.args
  check=arguments.get('job')
  if check:
    check=check.lower()
    fromDb = db.get(check)
    if fromDb:
      all_info=fromDb
    else:
      all_info=get_so_info(arguments,get_last_page(arguments))+get_rm_info(arguments)+get_we_info(arguments)
      db[check]= all_info
  else:
    return redirect("/")
  
  return render_template("read.html",argu=arguments['job'],all_info=all_info,all_info_len=len(all_info))

@app.route("/export")
def export():
  try:
    check = request.args.get('job')
    check=check.lower()
    if not check:
      raise Exception()
    all_info = db.get(check)
    if not all_info:
      raise Exception()
    save_to_file(all_info)
    return send_file("jobs.csv",mimetype="text/csv",attachment_filename=f"{check}.csv",as_attachment=True)
  except Exception as e:
    print(e)
    return redirect("/")


app.run(host="0.0.0.0")



