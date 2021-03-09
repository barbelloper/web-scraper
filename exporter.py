import csv

def save_to_file(all_info):
  file = open("jobs.csv",mode="w")
  writer = csv.writer(file)
  writer.writerow(["title","company","link"])
  for info in all_info:
    writer.writerow(list(info.values()))
  return