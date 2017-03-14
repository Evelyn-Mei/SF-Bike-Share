
# coding: utf-8

# In[17]:

import pandas as pd
data=pd.read_csv("201408_trip_data.csv")
data.shape
stationNames=set(data['Start Station'])
stationNames=list(stationNames)


# In[91]:

#subset=data[0:50]
c=data.groupby('Start Station').count()
count_start_station=c[[0]]
count_start_station.columns=['count']
count_start_station.to_csv('Count Start Station.csv')


# In[70]:

from geopy.geocoders import Nominatim
geolocator = Nominatim()
lats=[]
lngs=[]
#sf=Location((37.7792808, -122.4192362, 0.0))
for station,count in count_start_station.iterrows():
    #print station
    location = geolocator.geocode(str(station)+ " SF")
    if (location==None):
        lats.append("37.7792808")
        lngs.append("-122.4192362")
    else:
        lats.append(location.latitude)
        lngs.append(location.longitude)

#location.latitude, location.longitude
#print(location.address)
#print((location.latitude, location.longitude))


# In[83]:


#lats[lats=='37.7792808']=37.7792808
lats_float=[float(i) for i in lats]
lngs_float=[float(i) for i in lngs]
count_start_station['lat']=lats_float
count_start_station['lng']=lngs_float
count_start_station.to_csv("Count Start Station with lat lng.csv")


# In[121]:

#start charting
import folium
map_osm=folium.Map(location=[37.7792808, -122.4192362],zoom_start=13)
map_osm.save('sf_bike.html')
map_osm


# In[122]:

count_start_station=pd.read_csv("Count Start Station with lat lng.csv")
count_start_station=count_start_station[count_start_station.lat!=37.779280799999995]

#count_start_station


# In[ ]:




# In[128]:


marker_cluster = folium.MarkerCluster("Cluster Name").add_to(map_osm)
for station,row in count_start_station.iterrows():
    #print row['NaicsDescription']
    folium.CircleMarker(location=[row['lat'],row['lng']],radius=row['Count']/100,color='red',fill_color='red',popup=str(row['Start Station']) +" | Nnumber of bikes borrowed: "+ str(row['Count'])).add_to(marker_cluster)

#for index,row in subset.iterrows():
#    folium.CircleMarker(location=[row['lat'],row['lng']],radius=200,popup=row['NaicsDescription'],color='#3186cc').add_to(marker_cluster)

#for i in range(len(lats)):
#    folium.CircleMarker(location=[subset[i]['lat'],subset[i]['lng']],radius=200,popup=subset[i]['NaicsDescription'],color='#3186cc').add_to(marker_cluster)
map_osm.save('sf_bike.html')
map_osm


# In[40]:

#Google geocode - does not work
#from apiclient import build
#from googleapiclient import sample_tools
#service = build('geocoder', 'v1', developerKey="AIzaSyDrhB8oOmgNuQC2tu0yNJtoFJfkccLIyJw")

