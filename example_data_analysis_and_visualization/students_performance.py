import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


#pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)

#remember to place csv file in local disk c
filepath = 'c://StudentsPerformance.csv'
df = pd.read_csv(filepath)

print(df.columns)

#calculate mean, std and so on
print(df.describe())


#Bar graph
male = df[df.gender == 'male']
female = df[df.gender == 'female']
male = male.groupby('parental level of education')['math score'].mean()
female = female.groupby('parental level of education')['math score'].mean()
print(male)
print(female)

labels ='Associate Degree','Bachelor Degree','High school', 'Master Degree','Some College','Some High School'
print(labels)

ind = np.arange(len(male))  # the x locations for the groups
width = 0.35  # the width of the bars

fig, ax = plt.subplots(figsize=(12,10))
rects1 = ax.bar(ind - width/2, male, width,
                color='DarkRed', label='Male')
rects2 = ax.bar(ind + width/2, female, width,
                color='Crimson', label='Female')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Math Score')
ax.set_title('Average Math Score by different Parental Level of Education and Gender')
ax.set_xticks(ind)
ax.set_xticklabels(labels)
ax.legend()



#Pie Chart

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels ='Associate Degree','Bachelor Degree','High school', 'Master Degree','Some College','Some High School'
data = df.groupby('parental level of education')['writing score'].mean()
print(data)

explode = (0,0,0,0.1,0,0)  # only "explode" the 2nd slice (i.e. 'Hogs')
fig1, ax1 = plt.subplots()
ax1.pie(data, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.suptitle("Average Writing Score based on Parental Level of Education")
plt.show()




#Scatter Plot

plt.figure()
x = df['reading score']
y = df['writing score']
plt.title("Reading Score by Writing Score")
plt.xlabel("Reading Score")
plt.ylabel("Writing Score")
plt.scatter(x,y)
plt.show()
