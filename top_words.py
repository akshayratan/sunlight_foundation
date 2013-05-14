#Searching for Top Words and phrases
import requests
import pprint

query_params = { 'apikey': 'API_KEY',
				 'per_page': 3,
		   		 'entity_type': 'month',
                 'entity_value': '201210',
		 'sort': 'count desc'
		 		}

#Sorting by count tag and in descending order

endpoint= 'http://capitolwords.org/api/phrases.json'

response = requests.get(endpoint, params=query_params)
data=response.json
pprint.pprint(data)
