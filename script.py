#Copyright: Akshay Ratan <akshayratan@gmail.com>
import requests
import pprint

query_params = { 'apikey': '0fce6ca142d042dca0f49936c212fe1e',
			     'per_page': 3,
			     'phrase': 'election night',	
			     'state' : 'MD',
		       }

endpoint = 'http://capitolwords.org/api/text.json'
response = requests.get(endpoint, params=query_params)
data=response.json
pprint.pprint(data)
 
