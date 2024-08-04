#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install folium')


# In[2]:


import folium

# Create a map centered around Waterloo, Ontario
waterloo_map = folium.Map(location=[43.4643, -80.5204], zoom_start=13)

# Add markers or other elements to the map if needed
folium.Marker([43.4643, -80.5204], popup='Waterloo').add_to(waterloo_map)

# Display the map in the Jupyter Notebook
waterloo_map


# In[3]:


import folium

# Create a map centered around Waterloo, Ontario with a nicer tileset and higher zoom level
waterloo_map = folium.Map(location=[43.4643, -80.5204], zoom_start=15, tiles='Stamen Terrain')

# Add a marker for a specific location
folium.Marker([43.4643, -80.5204], popup='Waterloo', icon=folium.Icon(color='blue')).add_to(waterloo_map)

# Add circle markers for additional points of interest
poi_locations = [
    {"location": [43.4686, -80.5375], "name": "University of Waterloo"},
    {"location": [43.4504, -80.4922], "name": "Wilfrid Laurier University"},
    # Add more points of interest here
]

for poi in poi_locations:
    folium.CircleMarker(
        location=poi["location"],
        radius=8,
        color='green',
        fill=True,
        fill_color='green',
        fill_opacity=0.7,
        popup=poi["name"]
    ).add_to(waterloo_map)

# Display the map in the Jupyter Notebook
waterloo_map


# In[7]:


pip install folium geopy


# In[9]:


import folium
from geopy.geocoders import Nominatim

# Get latitude and longitude of Waterloo using geopy
geolocator = Nominatim(user_agent="waterloo_map")
location = geolocator.geocode("Waterloo, Canada")
latitude = location.latitude
longitude = location.longitude

# Create a base map centered at Waterloo
waterloo_map = folium.Map(location=[latitude, longitude], zoom_start=13)

# Add markers and popups
folium.Marker([latitude, longitude], popup="Waterloo").add_to(waterloo_map)

# Save the map to an HTML file
waterloo_map.save("/Users/zarrintasneem/Documents/waterloo_map.html")

print("Map saved as waterloo_map.html")


# In[10]:


import folium
from geopy.geocoders import Nominatim

# Get latitude and longitude of Waterloo using geopy
geolocator = Nominatim(user_agent="waterloo_map")
location = geolocator.geocode("Waterloo, Canada")
latitude = location.latitude
longitude = location.longitude

# Create a base map centered at Waterloo
waterloo_map = folium.Map(location=[latitude, longitude], zoom_start=15, tiles='Stamen Terrain')

# Add a marker and popup for Waterloo
folium.Marker(
    location=[latitude, longitude],
    popup="Welcome to Waterloo!",
    icon=folium.Icon(icon="cloud")
).add_to(waterloo_map)

# Add a circle to highlight an area of interest
folium.Circle(
    location=[latitude, longitude],
    radius=500,  # in meters
    color="blue",
    fill=True,
    fill_color="blue",
    fill_opacity=0.2,
    popup="Downtown Waterloo"
).add_to(waterloo_map)

# Add a custom layer control
folium.LayerControl().add_to(waterloo_map)

# Save the map to an HTML file
waterloo_map.save("/Users/zarrintasneem/Documents/waterloo_map.html")

print("Map saved as waterloo_map.html")


# In[ ]:




