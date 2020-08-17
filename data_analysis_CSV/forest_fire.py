import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
#pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)

#read csv files from local disk C
df = pd.read_csv("c://forestfires.csv")
df.info()


#Bar graph
data = df.groupby('month')['area'].mean()
print(data)

#arrange month orders from the result mean data
label =['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
ind = np.arange(len(label))
area =[0,6.28,4.36,8.89,19.24,5.84,14.37,12.49,17.94,6.64,0,13.33]

plt.bar(ind, area, align='center', alpha=0.5, color='Navy')
plt.xticks(ind, label)
plt.ylabel('Burned Area(Ha)')
plt.title('Burned Area of the Forest in 2007')

plt.show()




#calculate RH mean, std and so on
print(df.RH.describe())

#Pie chart
# Pie chart, where the slices will be ordered and plotted counter-clockwise:
data = df.groupby('month')['RH'].mean()
print(data)
labels = 'Apr', 'Aug', 'Dec', 'Feb', 'Jan', 'Jul', 'Jun', 'Mar', 'May', 'Nov', 'Oct', 'Sep'
explode = (0,0,0,0,0.1,0,0,0,0,0,0,0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots(figsize=(7,6))
ax1.pie(data, explode=explode, labels=labels, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.suptitle("Relative Humidity based on Month")
plt.show()




#Line Graph

data = df.groupby('month')['temp'].mean()
print(data)

#mean temp data according to month
temp=[5.25,9.64,13.08,9.635,14.65,20.49,22.11,21.63,19.61,17.09,11.8,4.52]
plt.plot(label,temp)
plt.title("Changes of Forest's Temperature in 2007")
plt.xlabel("Month")
plt.ylabel("Temperature (Celcius)")
