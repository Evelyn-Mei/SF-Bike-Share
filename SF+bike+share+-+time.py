
# coding: utf-8

# In[14]:

import pandas as pd
data=pd.read_csv("201408_trip_data.csv")


# In[15]:

from datetime import datetime
datetime_objects=[]
dates=[]
hours=[]
weekdays=[]
for index,row in data.iterrows():
    datetime_object = datetime.strptime(row['Start Date'], '%m/%d/%Y %H:%M')
    datetime_objects.append(datetime_object)
    dates.append(datetime_object.timetuple().tm_mday)
    hours.append(datetime_object.timetuple().tm_hour)
    weekdays.append(datetime_object.timetuple().tm_wday)


# In[16]:

data['datetime_objects']=datetime_objects
data['date']=dates
data['hour']=hours
data['weekday']=weekdays


# In[17]:


volume_by_day=data.groupby('date').count()

volume_by_hour=data.groupby('hour').count()

volume_by_weekday=data.groupby('weekday').count()
#plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d'))
#plt.gca().xaxis.set_major_locator(mdates.DayLocator())
#plt.plot(y)
#plt.show()


# In[72]:

#plt.style.use('dark_background')
plt.style.use('seaborn-talk')
fig = plt.figure(1)
ax = fig.add_subplot(111)
plt.plot(volume_by_hour,'o-')
for index,row in volume_by_hour.iterrows():
    if index==8 or index==17:
        ax.annotate(index,xy=(index,row[1]),color='green',horizontalalignment='middle', verticalalignment='top',fontsize=15)

    #ax.annotate('(%s, %s)' % xy, xy=xy, textcoords='data') 
plt.title('Bike share activity in SF by time of the day (2014 Aug)')
plt.ylabel('Number of riders')
plt.xlabel('Hour of the day')

plt.figure(2)
plt.subplot(211)
plt.plot(volume_by_weekday,'o-')
plt.title('Bike share activity in SF by day of the week (2014 Aug)')
plt.ylabel('Number of riders')


plt.subplot(212)
plt.plot(volume_by_day,'--')
plt.title('Bike share activity in SF by day of the month (2014 Aug)')
plt.ylabel('Number of riders')



plt.show()


