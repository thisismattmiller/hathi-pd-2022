import json
from os.path import exists
import requests
import time

search_results = json.load(open('search_results_enriched.json'))


count = 0
nolcc = 0

for rec in search_results['gathers']:
	count+=1
	if 'classify' not in rec:
		if '050a' not in rec:
			if '090a' not in rec:
				
				print(rec)
				nolcc+=1

print(nolcc)