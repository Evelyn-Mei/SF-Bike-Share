
# coding: utf-8

# In[1]:

import pandas as pd
data=pd.read_csv("201408_trip_data.csv")


# In[2]:

#subset=data[0:50]
s=data.groupby('Start Station').count()
e=data.groupby('End Station').count()
count_start_station=s[[0]]
count_start_station.columns=['count']
count_start_station.to_csv('Count Start Station.csv')
count_end_station=e[[0]]
count_end_station.columns=['count']
count_end_station.to_csv('Count End Station.csv')


# In[9]:

station_start_end=count_start_station.join(count_end_station,lsuffix=' start', rsuffix=' end')
station_start_end


# In[12]:

num_bikes_short=station_start_end['count start']-station_start_end['count end']


# In[45]:

station_start_end['num bikes short']=num_bikes_short
station_start_end.to_csv("num of bikes short.csv")


# In[46]:

station_start_end=pd.read_csv("num of bikes short.csv")


# In[79]:

station_start_end.sort('num bikes short',ascending=False)


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[71]:

#start charting
import folium
map_osm=folium.Map(location=[37.7792808, -122.4192362],zoom_start=13)
map_osm.save('sf_bike_excess_map.html')
map_osm


# In[72]:

station_excess_bikes=station_start_end[station_start_end['num bikes short']<0]
station_excess_bikes


# In[74]:

#marker_cluster = folium.MarkerCluster("Cluster Name").add_to(map_osm)
for station,row in station_excess_bikes.iterrows():
    if (row['num bikes short']>(-500)):
        c='lime'
    else:
        c='green'
    folium.CircleMarker(location=[row['lat'],row['lng']],radius=row['num bikes short']/(-10),color=c,fill_color=c,popup=str(row['Start Station']) +" | Nnumber of bikes short: "+ str(row['num bikes short'])).add_to(map_osm)
map_osm.save('sf_bike_excess_map.html')
map_osm


# In[ ]:




# In[ ]:




# In[81]:

#start charting
import folium
map_osm=folium.Map(location=[37.7792808, -122.4192362],zoom_start=13)
map_osm.save('sf_bike_shortage_map.html')
map_osm


# In[67]:

station_shortage_bikes=station_start_end[station_start_end['num bikes short']>0]
station_shortage_bikes


# In[82]:

#marker_cluster = folium.MarkerCluster("Cluster Name").add_to(map_osm)
for station,row in station_shortage_bikes.iterrows():
    if (row['num bikes short']<500):
        c='tomato'
    else:
        c='red'
    folium.CircleMarker(location=[row['lat'],row['lng']],radius=row['num bikes short']/10,color=c,fill_color=c,popup=str(row['Start Station']) +" | Nnumber of bikes short: "+ str(row['num bikes short'])).add_to(map_osm)

map_osm.save('sf_bike_shortage_map.html')
map_osm


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[40]:

#Google geocode - does not work
#from apiclient import build
#from googleapiclient import sample_tools
#service = build('geocoder', 'v1', developerKey="AIzaSyDrhB8oOmgNuQC2tu0yNJtoFJfkccLIyJw")

