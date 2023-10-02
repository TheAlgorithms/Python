# https://en.wikipedia.org/wiki/Hierarchical_clustering


from sklearn.datasets import load_wine
import pandas as pd
import numpy as np
import string

wine = load_wine()
data1 = pd.DataFrame(data=np.c_[wine['data'], wine['target']], columns=wine['feature_names']+['target'])
data = data1.iloc[:26]
data = data.drop('target', axis = 1)



#autoscailing data

mean_df = data.mean(axis=0)
std_df = data.std(axis=0)

df1 = []
i = 0

for dot in data.columns:
    ascaled = (data[dot]-mean_df[i])/std_df[i]
    i+=1
    df1.append(ascaled)

df2 = pd.concat(df1, axis=1)

#Adding Letter Indexes [optional]

# kal = list(string.ascii_uppercase)
# ind=[]

# for i in range(len(data)):
#     s = kal[i]
#     ind+=s    

# df2.index = ind
df = df2



#Euclidean Distance Matrix

def df_odl_eukl(df):
    
    n_df=(df.values)
    n_df
    
    (df.values).shape
    
    matrix=np.zeros(((df.values).shape[0],(df.values).shape[0]))
    matrix
    
    
    for i in range((df.values).shape[0]):
        for j in range((df.values).shape[0]):
            matrix[i,j]=np.sqrt(np.sum((n_df[i]-n_df[j])**2))



    df_odl = pd.DataFrame(matrix)
    # df_odl.index = ind  #uncomment if letter index needed
    df_odl_eukl = df_odl
    return df_odl_eukl

df_oe = df_odl_eukl(df)


df_odl = np.tril(df_oe)
X = df_oe.copy()





Z = X.copy()

X = df_oe.copy()
nazwy = iter(range(len(X),200))

full_dict = {}

lista_tych_coordow = []
min_value_lits = []
list_coord_name = []

while X.size >= 2:

    triangle = pd.DataFrame(np.tril(X), columns = X.columns, index = X.index)
    triangle_flat = np.array(triangle).flatten()
    
    
    
    min1 = min(i for i in triangle_flat if i > 0)
    coord = tuple(np.where(triangle == min1))
    lista_tych_coordow.append(list(coord))
    
    min_value_lits.append(min1)
    
    coord1 = max(coord)[0]
    coord2 = min(coord)[0]
    
    
    lista_cor = X.iloc[coord1].name, X.iloc[coord2].name
    list_coord_name.append(lista_cor)
    
    new_name = next(nazwy)
    
    #Couting number of object in cluster

    nazwy_col = []

   
        

    for i in range(0, len(Z)): 
        nazwy_col.append(Z.columns[i])

    if X.iloc[coord1].name in nazwy_col and X.iloc[coord2].name in nazwy_col:
        full_dict[new_name] = 2
        
    elif (X.iloc[coord1].name in nazwy_col and X.iloc[coord2].name not in nazwy_col):
        full_dict[new_name] =  1 + full_dict.get(X.iloc[coord2].name)
        
    elif (X.iloc[coord1].name not in nazwy_col and X.iloc[coord2].name in nazwy_col):
        full_dict[new_name] = 1 + full_dict.get(X.iloc[coord1].name)
        
    else:
        full_dict[new_name] = full_dict.get(X.iloc[coord1].name) + full_dict.get(X.iloc[coord2].name)
                    
                    

    
    wektor = []
    
    
    for i in range(len(X)):
        if X.iloc[coord1,i] == 0:
            wektor.append(X.iloc[coord1,i])
        
        elif X.iloc[coord2,i] == 0:
            wektor.append(X.iloc[coord2,i])
        
        elif X.iloc[coord1,i] > X.iloc[coord2,i]:
            wektor.append(X.iloc[coord1, i])

        else:
            wektor.append(X.iloc[coord2, i])

          
    X.iloc[coord2] = wektor
    X.iloc[:, coord2] = wektor
    
    
    X.drop(X.columns[coord1], axis=1, inplace = True)
    X.drop(X.index[coord1], axis=0, inplace = True)


   
    
    X.rename(columns={X.columns[coord2]: new_name}, inplace=True)
    X.rename(index={X.index[coord2]: new_name}, inplace=True)
    

    


last = []

k =  list(full_dict.values())

for i in range(len(min_value_lits)):
    last.append([list_coord_name[i][0], list_coord_name[i][1], 
                  min_value_lits[i], k[i]])




import scipy.cluster.hierarchy as sch
from scipy.cluster.hierarchy import ward, fcluster, single, complete
from scipy.spatial.distance import pdist
import matplotlib.pyplot as plt


# =============================================================================
# Takes final matrix from HCA, and generate dendrogram by use of libraries
# 
# =============================================================================

fig = plt.figure(figsize=(12, 7))
dendrogram = sch.dendrogram(last) #put the name of variable which contains 
                                    #objects, min_values and number of obj in cluster
plt.title('Dendrogram')
plt.xlabel('Obiekty')
plt.ylabel('Euclidean distance')
plt.show()

test_mat = complete(pdist(df)) #if this is the same as matrix last
#then you do a good job!

print(last)
print(test_mat)


