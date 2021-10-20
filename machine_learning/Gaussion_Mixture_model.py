import numpy as np
import pandas as pd
import sklearn.mixture
import sklearn.metrics
import math



#classifier function
def classifier(q):

    file1 = pd.read_csv("fileto-train.csv") #file should have class attribute
    file2 = pd.read_csv("fileto-test.csv")
    df1 = pd.DataFrame(file1)
    df2 = pd.DataFrame(file2)

    df_0 = df1.where(df1["Class"] == 0, inplace=False)  #imp: exclude class attribute from df1 while declaring df_0 and df_1
    df_0.dropna(inplace=True)
    df_0.reset_index(inplace=True)
    df_1 = df1.where(df1["Class"] == 1, inplace=False)
    df_1.dropna(inplace=True)
    df_1.reset_index(inplace=True)

    #create gmm model and fit training values
    gmm_0 = sklearn.mixture.GaussianMixture(n_components=q, covariance_type='full')
    gmm_0.fit(df_0)
    gmm_1 = sklearn.mixture.GaussianMixture(n_components=q, covariance_type='full')
    gmm_1.fit(df_1)

    #calculate log likelihood
    ll_0 = (gmm_0.score_samples(df2))
    ll_1 = (gmm_1.score_samples(df2))

    #predict values for test data
    pred = []

    for i in range(len(ll_0)):
        if(ll_0[i] > ll_1[i]):
            pred.append(0)
        else:
            pred.append(1)

    return pred

