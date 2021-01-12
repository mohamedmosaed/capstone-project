#!/usr/bin/env python
# coding: utf-8

# ##### Finding the resturant near the location using foursquare AIP

# In[1]:


import requests # library to handle requests
import pandas as pd # library for data analsysis
import numpy as np # library to handle data in a vectorized manner
import random # library for random number generation


get_ipython().system('conda install -c conda-forge geopy --yes')
from geopy.geocoders import Nominatim # module to convert an address into latitude and longitude values

# libraries for displaying images
from IPython.display import Image 
from IPython.core.display import HTML 
    
# tranforming json file into a pandas dataframe library
from pandas.io.json import json_normalize


get_ipython().system('conda install -c conda-forge folium=0.5.0 --yes')
import folium


# In[2]:


CLIENT_ID = 'X232G0AO4NMXBK2Q0OBC1TOXU30TK3HJ0YVWYFQ4X2CPID5R' # your Foursquare ID
CLIENT_SECRET = '50F4KNMIKPOKIGIKM1JUE5MBWTEBZTSVZ0CAMKRTREHUPCEC' # your Foursquare Secret
ACCESS_TOKEN = 'restaurant' # your FourSquare Access Token
VERSION = '20210112'
LIMIT = 30


# In[3]:


address = '102 North End Ave, New York, NY'

geolocator = Nominatim(user_agent="foursquare_agent")
location = geolocator.geocode(address)
latitude = location.latitude
longitude = location.longitude
print(latitude, longitude)


# In[4]:


search_query = 'Italian'
radius = 500


# In[5]:


url = 'https://api.foursquare.com/v2/venues/search?client_id={}&client_secret={}&ll={},{}&oauth_token={}&v={}&query={}&radius={}&limit={}'.format(CLIENT_ID, CLIENT_SECRET, latitude, longitude,ACCESS_TOKEN, VERSION, search_query, radius, LIMIT)
url


# In[6]:


results = requests.get(url).json()
results


# In[ ]:


venues = results['response']['venues']

# tranform venues into a dataframe
dataframe = json_normalize(venues)
dataframe.head()


# In[7]:


def getNearbyVenues(names, latitudes, longitudes):
    venues_list=[]
    for name, lat, lng in zip(names, latitudes, longitudes):
        print(name)
        
        
        results = requests.get(url).json()["respones"]['groups'][0]['items']
        
        venues_list.append([(name, lat, log,
                            v['venue']['name'],
                            v['venue']['location']['lat'],
                            v['venue']['location']['log'],
                            v['venue']['categories'][0]['name']) for v in results])
        
        return (venues_list)


# In[8]:


antwerp_venues = getNearbyVenues(names= df['Name'],
                                latitudes = df['Latitude'],
                                longitudes = df['Longitude'])


# In[ ]:


nearby_venues = pd.DataFrame([item for venues_list in antwerp_venues for antwery_venues for item in venues_list])


# In[ ]:


nearby_venues.head()

