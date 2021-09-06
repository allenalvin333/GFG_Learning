import os
import json
import requests

# Loading variable from .env
from dotenv import load_dotenv
load_dotenv()
api=os.getenv('API_KEY')

# JSON using API
r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Bangalore&appid={}'.format(api))
for k1, v1 in r.json().items(): 
    if(k1=='main' or k1=='coord' or k1=='sys'):
        for k2, v2 in v1.items(): print(k2, ":", v2)
    else: print(k1, ":", v1)
r.close()

# https://realpython.com/api-integration-in-python/

