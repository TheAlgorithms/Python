import math
import csv
import time
import numpy as np
import collections
from sklearn.cluster import KMeans
from sklearn.metrics.cluster import adjusted_rand_score


def eucl_distance(point_one, point_two):                  
	if(len(point_one) != len(point_two)):                  
		raise Exception("Error: non comparable points")    

	sum_diff = 0.0                                                 
	for i in range(len(point_one)):                                
		diff = pow((float(point_one[i]) - float(point_two[i])), 2)  
		sum_diff += diff                                           
	final = math.sqrt(sum_diff)                                    
	return final

global dimensions, num_clusters, num_points,dimensions,data,flag

print("Enter the number of clusters you want to make: ")
num_clusters = input()
num_clusters = int(num_clusters)
start_time = time.time()
with open('3D_spatial_network2.csv','rb') as f:
    reader = csv.reader(f)
    data = list(reader)

data.pop(0)
for i in range (len(data)):
    data[i].pop(0)
data=np.array(data).astype(np.float)
data=data[0:10000]

kmeans = KMeans(n_clusters=num_clusters, random_state=0).fit(data).labels_
initial=[]
for i in xrange(num_clusters):
    initial.append(data[i])
initial=np.vstack(initial)

num_points = len(data)                                    
dimensions = len(data[0])                                 
flag= True
while flag==True:

	cluster=[]
	dist =np.zeros((len(data),len(initial)))


	for j in range(len(initial)):
		for i in range(len(data)):
			dist[i][j]=np.linalg.norm(initial[j]-data[i])
	for i in range (len(dist)):										
		cluster.append(np.argmin(dist[i])+1)                       
	Q_clusts=collections.Counter(cluster)							
	

	centroid=np.zeros((len(initial),len(initial[0])))
	for k in range (1,num_clusters+1):
		indices = [i for i, j in enumerate(cluster) if j == k]
		centroid[k-1]=np.divide((np.sum([data[i] for i in indices], axis=0)).astype(np.float),Q_clusts[k])


		
	
	if np.all(centroid==initial):
		flag=False
		
		print ("Execution time %s seconds" % (time.time() - start_time))
	else:
		initial= centroid 
	
	print('adjusted_rand_score',adjusted_rand_score(kmeans,cluster))

