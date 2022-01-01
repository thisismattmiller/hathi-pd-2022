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
			if 'lccn' in rec:
				if rec['lccn'] != None:
					lccn = rec['lccn'][0]

					
					if not exists('lccn/'+lccn):
						lccn=lccn.split('/')[0]
						print(lccn)
						url = f"https://lccn.loc.gov/{lccn}/marcxml"
						r = requests.get(url)
						time.sleep(6)
						with open('lccn/'+lccn,'w') as out:

							out.write(r.text)
							time.sleep(1)
							




