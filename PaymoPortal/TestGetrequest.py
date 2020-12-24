# TODO
#  find user,
#  project tasklist,
#  entry notes,
#  start time,
#  end time,
#  decimal time,
#  project description,
#  rolls,
import requests
import datetime


email = 'a.cain@rotterdamengineering.nl'
password = 'hnnHFff7'

headers = {'Accept': 'application/json'}
r = requests.get('https://app.paymoapp.com/api/projects', headers=headers, auth=(email, password))
#l = requests.get('https://app.paymoapp.com/api/projects', headers=headers, auth=(email, password))

# List project names
for project in r.json()['projects']:
   print("Naam:",(project['name']))
   print("Description:", (project['description']))
   print("manager:", project['managers'])
   print("project:", project['users']) # list
   print("client_id:", project['client_id'])
   print("project_status:", project['status_id'])
    # tasklist?
   print("start_time: ", (project['created_on'])) # TODO pars date
   print("last_update: ", (project['updated_on']))
   print("\n")
    # end time?
   #print("end_time: " + (project['closed_on'])) closed_on is not a key TODO find key
    # decimal time







