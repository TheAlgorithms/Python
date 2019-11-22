import math
import csv
import time
import numpy as np
import collections
from mpi4py import MPI
from sklearn.cluster import KMeans
from sklearn.metrics.cluster import adjusted_rand_score



#===================================================Devide data set to further scattering=====================
def chunkIt(seq, num):
    avg = len(seq) / float(num)
    out = []
    last = 0.0

    while last < len(seq):
        out.append(seq[int(last):int(last + avg)])
        last += avg
    return out
#===================================================Count lables for recalculating means of centroids=====================	
def addCounter(counter1, counter2, datatype):
    for item in counter2:
        counter1[item] += counter2[item]
    return counter1

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
global dimensions, num_clusters, num_points,dimensions,data,flag
num_clusters=0


if rank==0: 													#master part
	#===============================================reading and preparing data set======================
	
	print("Enter the number of clusters you want to make: ")
	num_clusters = input()
	num_clusters = int(num_clusters)
	start_time = time.time() 										#turn on a timer which allows us to estimate performane of this algorithm

	with open('3D_spatial_network2.csv','rb') as f:
		reader = csv.reader(f)
		data = list(reader)
		
	data.pop(0)
	for i in range (len(data)):
		data[i].pop(0)
	data=data[0:10000]
	data=np.array(data).astype(np.float)

	kmeans = KMeans(n_clusters=num_clusters, random_state=0).fit(data).labels_

	initial=[]
	for i in xrange(num_clusters):
		initial.append(data[i])
	initial=np.vstack(initial)

	num_points = len(data)                                    #number of rows
	dimensions = len(data[0])                                 #number of columns
	chunks=chunkIt(data,size)								  #deviding data set on parts for further scattering
else:														  
	chunks = None											  
	initial = None											  
	data = None											      
	dimensions = None										  
	num_points = None										  
	cluster= None											  
	Q_clust= None											  
	num_clusters= None										  
	centroid=None
	kmeans= None
	start_time=None
start_time=comm.bcast(start_time,root=0)
data=comm.scatter(chunks, root=0)							  
num_clusters=comm.bcast(num_clusters,root=0)
initial=comm.bcast(initial, root = 0)						  
flag= True
while flag==True:
	clusters=[]											  		  
	cluster=[]
	#print str(rank) + ': ' + str(data)
	#===================================Calculating dist matrix in each process==============================
	dist =np.zeros((len(data),len(initial)))


	for j in range(len(initial)):
		for i in range(len(data)):
			dist[i][j]=np.linalg.norm(initial[j]-data[i])
	#print('rank',rank,dist)		
	#===================================Initilize lable for each sample in each process======================
	for i in range (len(dist)):										
		clusters.append(np.argmin(dist[i])+1)                       
	Q_clusts=collections.Counter(clusters)							
	counterSumOp = MPI.Op.Create(addCounter, commute=True)

	totcounter = comm.allreduce(Q_clusts, op=counterSumOp)
	comm.Barrier()
	cluster=comm.gather(clusters, root=0)
	comm.Barrier()
	if rank==0:
		cluster=[item for sublist in cluster for item in sublist]

	centroids=np.zeros((len(initial),len(initial[0])))
	for k in range (1,num_clusters+1):
		indices = [i for i, j in enumerate(clusters) if j == k]
		centroids[k-1]=np.divide((np.sum([data[i] for i in indices], axis=0)).astype(np.float),totcounter[k])

	centroid=comm.allreduce(centroids,MPI.SUM)
	comm.Barrier()
		
	
	if np.all(centroid==initial):
		flag=False
		print ("Execution time %s seconds" % (time.time() - start_time))
		
	else:
		initial= centroid 
	comm.Barrier()

#---- The Davies–Bouldin index are taken for CLuster comparison(Compared to sequential K-means) -----
if rank==0:
	print('adjusted_rand_score',adjusted_rand_score(kmeans,cluster))



			

		
