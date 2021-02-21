#!/usr/bin/env python
# coding: utf-8

# # Importing the necessary Lib

# In[1]:


import pandas as pd
import numpy as np


# ## Scrapping the data

# In[2]:


df=pd.read_html("https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M")


# In[3]:


print(len(df))


# In[4]:


df1=df[0]
df1.head()


# ### Data Wrangling

# In[5]:


df1[df1["Neighbourhood"]== 'Not assigned']


# In[6]:


df1.shape


# In[7]:


df2=df1[~df1['Borough'].str.contains('Not assigned')]
df2


# In[8]:


df1.Neighbourhood.value_counts()


# In[9]:


df2.Neighbourhood.value_counts()


# In[10]:


df1.Borough.value_counts()


# In[11]:


df2.Borough.value_counts()


# In[12]:


df2.shape


# In[13]:


df2.isnull().sum()


# # Dataframe of the postal code of each neighborhood 

# In[14]:


get_ipython().system('pip install geocoder')
import geocoder


# In[15]:


neigh=pd.read_csv("https://cocl.us/Geospatial_data")


# In[16]:


neigh.head()


# In[17]:


neigh.shape


# In[18]:


df3=df2.merge(neigh, on='Postal Code')


# In[19]:


df3.head(30)


# In[24]:


import json 

get_ipython().system('conda install -c conda-forge geopy --yes ')
from geopy.geocoders import Nominatim

import requests 
from pandas.io.json import json_normalize 


import matplotlib.cm as cm
import matplotlib.colors as colors


from sklearn.cluster import KMeans

get_ipython().system('conda install -c conda-forge folium=0.5.0 --yes ')
import folium 

print('Libraries imported.')


# In[29]:


address = 'Canada, tn'

geolocator = Nominatim(user_agent="tn_explorer")
location = geolocator.geocode(address)
latitude = location.latitude
longitude = location.longitude
print('The geograpical coordinate of Canada City are {}, {}.'.format(latitude, longitude))


# In[33]:



map_canada = folium.Map(location=[latitude, longitude], zoom_start=10)

# add markers to map
for lat, lng, borough, Neighbourhood in zip(df3['Latitude'], df3['Longitude'], df3['Borough'], df3['Neighbourhood']):
    label = '{}, {}'.format(Neighbourhood, borough)
    label = folium.Popup(label, parse_html=True)
    folium.CircleMarker(
        [lat, lng],
        radius=5,
        popup=label,
        color='blue',
        fill=True,
        fill_color='#3186cc',
        fill_opacity=0.7,
        parse_html=False).add_to(map_canada)  
    
map_canada


# Toronto Data

# In[45]:


Toronto_data= df3[df3['Borough'].str.contains('Toronto')].reset_index(drop=True)
Toronto_data.head()


# In[47]:


address = 'Toronto, TO'

geolocator = Nominatim(user_agent="to_explorer")
location = geolocator.geocode(address)
latitude = location.latitude
longitude = location.longitude
print('The geograpical coordinate of Toronto are {}, {}.'.format(latitude, longitude))


# In[48]:


map_Toronto = folium.Map(location=[latitude, longitude], zoom_start=11)

# add markers to map
for lat, lng, label in zip(Toronto_data['Latitude'], Toronto_data['Longitude'], Toronto_data['Neighbourhood']):
    label = folium.Popup(label, parse_html=True)
    folium.CircleMarker(
        [lat, lng],
        radius=5,
        popup=label,
        color='blue',
        fill=True,
        fill_color='#3186cc',
        fill_opacity=0.7,
        parse_html=False).add_to(map_Toronto)  
    
map_Toronto


# In[49]:


CLIENT_ID = '04FLOU31ELGGC4IEHHAUXUGCUS3GCE2XIZLHYPF0RZVR12VA' # your Foursquare ID
CLIENT_SECRET = 'ZREANKWAQ0DLH2CL0LPGCUCEGWDKQ2MAVGRQIOAZJD24H2HE' # your Foursquare Secret
ACCESS_TOKEN = 'FOPJUITJODG1FBTDSIPIVNRPQ2SKB3D1ACNFDS034QJ3NDQH' # your FourSquare Access Token
VERSION = '20180604'
LIMIT = 30
print('Your credentails:')
print('CLIENT_ID: ' + CLIENT_ID)
print('CLIENT_SECRET:' + CLIENT_SECRET)


# In[51]:


Toronto_data.loc[0, 'Neighbourhood']


# In[52]:


neighborhood_latitude = Toronto_data.loc[0, 'Latitude'] # 
neighborhood_longitude = Toronto_data.loc[0, 'Longitude'] # 

neighborhood_name = Toronto_data.loc[0, 'Neighbourhood'] 

print('Latitude and longitude values of {} are {}, {}.'.format(neighborhood_name, 
                                                               neighborhood_latitude, 
                                                               neighborhood_longitude))


# In[ ]:




