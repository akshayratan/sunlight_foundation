#Limiting the query by date specification
# The phrase 'holiday season' is searched from Nov 1,2012 to Dec 31,2012 of US Congress

import requests
import pprint

query_params = { 'apikey': '0fce6ca142d042dca0f49936c212fe1e',
				 'per_page': 3,
                 'phrase' : 'holiday season' ,
		   		 'start_date' : '2012-11-01',
                 'end_date' : '2012-12-31'  
		 		}

endpoint = 'http://capitolwords.org/api/text.json'

response = requests.get(endpoint, params=query_params)

data = response.json
pprint.pprint(data)
