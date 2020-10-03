'''
Upper Confidence Bound is a simple reinforcement algorithm. In reinforcement learning, the agent generates its training data by interacting with the world. The agent learns the consequences of its actions through trial and error, instead of being fed explicity.

A very popular use of the UCB algorithm is determining the advertisement that produces the maximum reward.

Imagine an online advertising trial where an advertiser wants to measure the click-through rate of three different ads for the same product. Whenever a user visits the website, the advertiser displays an ad at random. The advertiser then monitors whether the user clicks on the ad or not. After a while, the advertiser notices that one ad seems to be working better than the others. The advertiser must now decide between sticking with the best-performing ad or continuing with the randomized study. If the advertiser only displays one ad, then he can no longer collect data on the other two ads. Perhaps one of the other ads is better, it only appears worse due to chance. If the other two ads are worse, then continuing the study can affect the click-through rate adversely. This advertising trial exemplifies decision-making under uncertainty. In the above example, the role of the agent is played by an advertiser. The advertiser has to choose between three different actions, to display the first, second, or third ad. Each ad is an action. Choosing that ad yields some unknown reward. Finally, the profit of the advertiser after the ad is the reward that the advertiser receives.

The basic algorithm is:

Step 1: At each round n, we consider two numbers for each ad i,
  i. the number of times i was selected upto round n<br/>
  ii. the sum of rewards of the ad i upto round n
Step 2: From these two numbers we compute:
  i. the average reward of i upto round n<br/>
  ii. the confidence level at round n
Step 3: We select the i with maximum upper confidence bound
'''


# Importing the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math


# Importing the dataset
dataset=pd.read_csv('Ads.csv')

# Implementing UCB
N=10000 #Total number of times we advertise
d=10 #Total number of ads
ads_selected=[]
number_of_selections=[0]*d
sums_of_rewards=[0]*d
total_reward=0

def ucb():
    for n in range(0,N):
        ad=0
        max_upperbound=0
        for i in range(0,d):
            if(number_of_selections[i]>0):
                average_reward=sums_of_rewards[i]/number_of_selections[i]
                delta_i=math.sqrt(3/2*math.log(n+1)/number_of_selections[i])
                upper_bound=average_reward+delta_i
            else:
                upper_bound=1e400 #We do this to select each ad atleast once the first time
            if(upper_bound > max_upperbound):
                max_upperbound=upper_bound #Select the ad with the maximum upper confidence bound
                ad=i
        ads_selected.append(ad) 
        number_of_selections[ad]+=1 #Increase the number of selections for the selected ad
        reward=dataset.values[n,ad] #Receive rewards as per simulated dataset
        sums_of_rewards[ad]+=reward #Calculate the total rewards for the selected ad
        total_reward=total_reward+reward
            
def view():
    # Visualising the UCB results
    plt.hist(ads_selected)
    plt.title('Histogram of Ads seletions')
    plt.xlabel('Ads selected')
    plt.ylabel('Number of times each ad was seected')
    plt.show()

if __name__ == "__main__":
    ucb()
    view()