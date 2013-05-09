#Copyright: Akshay Ratan <akshayratan@gmail.com>
import requests

query_params = { 'apikey': 'API_KEY',
			     'phrase': 'fiscal cliff'
		       }

endpoint = 'http://capitolwords.org/api/text.json'
response = requests.get(endpoint, params=query_params)
request_url=response

