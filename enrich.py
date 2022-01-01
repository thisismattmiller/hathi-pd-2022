
import json
import os
import xml.etree.ElementTree as ET

search_results = json.load(open('search_results.json'))




count = 0
nolcc = 0

for rec in search_results['gathers']:
	count+=1
	print(count, nolcc)

	if 'oclc' in rec:

		if rec['oclc'] != None:

			oclc = rec['oclc'][0]

			if os.path.isfile('classify_by_oclc/'+oclc):

				oclc_text = open('classify_by_oclc/'+oclc).read()


				if '<response code="102"/>' not in oclc_text:

					

					element = ET.ElementTree(ET.fromstring(oclc_text)).getroot()



					e = element.find('{http://classify.oclc.org}recommendations/{http://classify.oclc.org}lcc/{http://classify.oclc.org}mostPopular')
					if e != None:


						rec['classify'] = e.attrib['sfa']


	filename = rec['catalog_url'].split('/')[-1] + '.json'
	if os.path.isfile('data/'+filename+'.json'):

		marc = json.load(open('data/'+filename+'.json'))
		
		for field in marc['fields']:

			if '050' in field:

				for subfield in field['050']['subfields']:
					if 'a' in subfield:
						rec['050a'] = subfield['a']


		for field in marc['fields']:

			if '090' in field:
				if 'a' in subfield:
					rec['090a'] = subfield['a']



	if 'classify' not in rec:
		if '050a' not in rec:
			if '090a' not in rec:
				nolcc=nolcc+1



json.dump(search_results,open('search_results_enriched.json','w'),indent=2)

