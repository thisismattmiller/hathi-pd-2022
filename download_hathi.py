import json
from os.path import exists
import requests
import time

search_results = json.load(open('search_results.json'))

counter = 0
total = len(search_results['gathers'])
for rec in search_results['gathers']:

	counter+=1

	url = rec['catalog_url'] + '.json'

	filename = rec['catalog_url'].split('/')[-1] + '.json'

	if not exists('data/'+filename+'.json'):

		
		try:
			r = requests.get(url)
			data = json.loads(r.text)

			json.dump(data,open('data/'+filename+'.json','w'),indent=2)

			print(counter,'/',total)
		except:
			print(counter,'/',total, "ERROR")
