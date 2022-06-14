#!/usr/bin/env python
# coding: utf-8

# In[139]:


#required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm



# In[140]:


#1(i)
mean=0
std_dev=1
exps=[]
for N in range(100, 10**5, 1000):
    rand_no=np.random.normal(loc=mean, scale=std_dev, size=(N,))
    exp=np.sum(np.logical_and(rand_no<=1, rand_no>=-1))/N
    exps.append(exp)
_, bins,_ = plt.hist(rand_no, 100, density = True)
plt.plot(bins, norm.pdf(bins, loc=mean, scale=std_dev), linewidth=2, color='#1bdc14')
plt.show()


# In[141]:



e_x = 68.2
mean_e_x=np.mean(exps) * 100

mean_e_x=int(mean_e_x * 10)/10

if e_x == mean_e_x:
    print('Result Verified')
    print(f'mean(XN)=E(X)={e_x}%')
else:
    print('Your results are wrong. Check again!')
    print(f'mean(XN) != E(X) = {e_x}%')
          




# In[164]:


#2(i)Profit for each month
revenue = [14574.49, 7606.46, 8611.41, 9175.41, 8058.65, 8105.44, 11496.28, 9766.09, 10305.32, 14379.96, 10713.97, 15433.50]
expenses = [12051.82, 5695.07, 12319.20, 12089.72, 8658.57, 840.20, 3285.73, 5821.12, 6976.93, 16618.61, 10054.37, 3803.96]
month = {0:'Janauary',1:'February',2:'March',3:'April',4:'May',5:'June',6:'July',7:'August',8:'September',9:'October',10:'November',11:'December'}
revenue=np.array(revenue)
expenses=np.array(expenses)
profit=revenue-expenses
print("Profit Per Month:\n",profit)



# In[165]:


#2(ii)Profit after tax for each month (the tax rate is 30% to revenue) 
tax=0.3*revenue
profit_after_tax = profit-tax
print("Profit After Tax:\n",profit_after_tax)


# In[166]:


#2(iii)Profit Margin for each month - equals to profit after tax dividend 
profit_margin = profit_after_tax/revenue*100

print("Profit Margin:\n",np.round(profit_margin,0))


# In[171]:


#2(iv)Good Months – Where the profit after tax was greater than the mean of the year 
mean_of_year = profit_after_tax.mean()
print('Mean of year = ',np.round(mean_of_year,2))
print("Good Months of Year ^_^")
good_months = []
for i in range(0,12):
    if profit_after_tax[i] > mean_of_year:
        good_months.append(month[i])
print(good_months)


# In[172]:


#2(v)Bad Months – Where the profit after tax was less than mean of the year
print('Mean of year = ',np.round(mean_of_year,2))
print("Bad Months of Year -_-")
bad_months = []
for i in range(0,12):
    if profit_after_tax[i] < mean_of_year:
        bad_months.append(month[i])
print(bad_months)
        


# In[173]:


#2(vi)The Worst Month – Where the profit after tax was minimum for the year 
worst_month=profit_after_tax.min()
print("Worst Month of Year -_-")
for i in range(0,12):
    if worst_month==profit_after_tax[i]:
     print(month[i])


# In[174]:


#2(vii)The Best Month – Where the profit after tax was maximum for the year 
best_month=profit_after_tax.max()
print("Best Month of year ^_^")
for i in range(0,12):
    if best_month==profit_after_tax[i]:
        print(month[i])




#Required data set
#Seasons
Seasons = ["2005","2006","2007","2008","2009","2010","2011","2012","2013","2014"]
Sdict = {"2005":0,"2006":1,"2007":2,"2008":3,"2009":4,"2010":5,"2011":6,"2012":7,"2013":8,"2014":9}

#Players
Players = ["KobeBryant","JoeJohnson","LeBronJames","CarmeloAnthony","DwightHoward","ChrisBosh","ChrisPaul","KevinDurant","DerrickRose","DwayneWade"]
Pdict = {"KobeBryant":0,"JoeJohnson":1,"LeBronJames":2,"CarmeloAnthony":3,"DwightHoward":4,"ChrisBosh":5,"ChrisPaul":6,"KevinDurant":7,"DerrickRose":8,"DwayneWade":9}

#Free Throws
KobeBryant_FT = [696,667,623,483,439,483,381,525,18,196]
JoeJohnson_FT = [261,235,316,299,220,195,158,132,159,141]
LeBronJames_FT = [601,489,549,594,593,503,387,403,439,375]
CarmeloAnthony_FT = [573,459,464,371,508,507,295,425,459,189]
DwightHoward_FT = [356,390,529,504,483,546,281,355,349,143]
ChrisBosh_FT = [474,463,472,504,470,384,229,241,223,179]
ChrisPaul_FT = [394,292,332,455,161,337,260,286,295,289]
KevinDurant_FT = [209,209,391,452,756,594,431,679,703,146]
DerrickRose_FT = [146,146,146,197,259,476,194,0,27,152]
DwayneWade_FT = [629,432,354,590,534,494,235,308,189,284]

#Matrix for free throws
Free_Throws = np.array(["KobeBryant_FT","JoeJohnson_FT","LeBronJames_FT","CarmeloAnthony_FT","DwightHoward_FT","ChrisBosh_FT","ChrisPaul_FT","KevinDurant_FT","DerrickRose_FT","DwayneWade_FT"])

#Free Throw Attempts
KobeBryant_FTA = [819,768,742,564,541,583,451,626,21,241]
JoeJohnson_FTA = [330,314,379,362,269,243,186,161,195,176]
LeBronJames_FTA = [814,701,771,762,773,663,502,535,585,528]
CarmeloAnthony_FTA = [709,568,590,468,612,605,367,512,541,237]
DwightHoward_FTA = [598,666,897,849,816,916,572,721,638,271]
ChrisBosh_FTA = [581,590,559,617,590,471,279,302,272,232]
ChrisPaul_FTA = [465,357,390,524,190,384,302,323,345,321]
KevinDurant_FTA = [256,256,448,524,840,675,501,750,805,171]
DerrickRose_FTA = [205,205,205,250,338,555,239,0,32,187]
DwayneWade_FTA = [803,535,467,771,702,652,297,425,258,370]

#Matrix for free throw attempts
Free_Throws_Attempts=np.array(["KobeBryant_FTA","JoeJohnson_FTA","LeBronJames_FTA","CarmeloAnthony_FTA","DwightHoward_FTA","ChrisBosh_FTA","ChrisPaul_FTA","KevinDurant_FTA","DerrickRose_FTA","DwayneWade_FTA"])
#Salaries
KobeBryant_Salary = [15946875,17718750,19490625,21262500,23034375,24806250,25244493,27849149,30453805,23500000]
JoeJohnson_Salary = [12000000,12744189,13488377,14232567,14976754,16324500,18038573,19752645,21466718,23180790]
LeBronJames_Salary = [4621800,5828090,13041250,14410581,15779912,14500000,16022500,17545000,19067500,20644400]
CarmeloAnthony_Salary = [3713640,4694041,13041250,14410581,15779912,17149243,18518574,19450000,22407474,22458000]
DwightHoward_Salary = [4493160,4806720,6061274,13758000,15202590,16647180,18091770,19536360,20513178,21436271]
ChrisBosh_Salary = [3348000,4235220,12455000,14410581,15779912,14500000,16022500,17545000,19067500,20644400]
ChrisPaul_Salary = [3144240,3380160,3615960,4574189,13520500,14940153,16359805,17779458,18668431,20068563]
KevinDurant_Salary = [0,0,4171200,4484040,4796880,6053663,15506632,16669630,17832627,18995624]
DerrickRose_Salary = [0,0,0,4822800,5184480,5546160,6993708,16402500,17632688,18862875]
DwayneWade_Salary = [3031920,3841443,13041250,14410581,15779912,14200000,15691000,17182000,18673000,15000000]
#Matrix for salary
Salary = np.array([KobeBryant_Salary, JoeJohnson_Salary, LeBronJames_Salary, CarmeloAnthony_Salary, DwightHoward_Salary, ChrisBosh_Salary, ChrisPaul_Salary, KevinDurant_Salary, DerrickRose_Salary, DwayneWade_Salary])

#Games 
KobeBryant_G = [80,77,82,82,73,82,58,78,6,35]
JoeJohnson_G = [82,57,82,79,76,72,60,72,79,80]
LeBronJames_G = [79,78,75,81,76,79,62,76,77,69]
CarmeloAnthony_G = [80,65,77,66,69,77,55,67,77,40]
DwightHoward_G = [82,82,82,79,82,78,54,76,71,41]
ChrisBosh_G = [70,69,67,77,70,77,57,74,79,44]
ChrisPaul_G = [78,64,80,78,45,80,60,70,62,82]
KevinDurant_G = [35,35,80,74,82,78,66,81,81,27]
DerrickRose_G = [40,40,40,81,78,81,39,0,10,51]
DwayneWade_G = [75,51,51,79,77,76,49,69,54,62]
#Matrix fr games
Games = np.array([KobeBryant_G, JoeJohnson_G, LeBronJames_G, CarmeloAnthony_G, DwightHoward_G, ChrisBosh_G, ChrisPaul_G, KevinDurant_G, DerrickRose_G, DwayneWade_G])

#Minutes Played
KobeBryant_MP = [3277,3140,3192,2960,2835,2779,2232,3013,177,1207]
JoeJohnson_MP = [3340,2359,3343,3124,2886,2554,2127,2642,2575,2791]
LeBronJames_MP = [3361,3190,3027,3054,2966,3063,2326,2877,2902,2493]
CarmeloAnthony_MP = [2941,2486,2806,2277,2634,2751,1876,2482,2982,1428]
DwightHoward_MP = [3021,3023,3088,2821,2843,2935,2070,2722,2396,1223]
ChrisBosh_MP = [2751,2658,2425,2928,2526,2795,2007,2454,2531,1556]
ChrisPaul_MP = [2808,2353,3006,3002,1712,2880,2181,2335,2171,2857]
KevinDurant_MP = [1255,1255,2768,2885,3239,3038,2546,3119,3122,913]
DerrickRose_MP = [1168,1168,1168,3000,2871,3026,1375,0,311,1530]
DwayneWade_MP = [2892,1931,1954,3048,2792,2823,1625,2391,1775,1971]
#Matrix for min played
Min_Played = np.array([KobeBryant_MP, JoeJohnson_MP, LeBronJames_MP, CarmeloAnthony_MP, DwightHoward_MP, ChrisBosh_MP, ChrisPaul_MP, KevinDurant_MP, DerrickRose_MP, DwayneWade_MP])

#Field Goals
KobeBryant_FG = [978,813,775,800,716,740,574,738,31,266]
JoeJohnson_FG = [632,536,647,620,635,514,423,445,462,446]
LeBronJames_FG = [875,772,794,789,768,758,621,765,767,624]
CarmeloAnthony_FG = [756,691,728,535,688,684,441,669,743,358]
DwightHoward_FG = [468,526,583,560,510,619,416,470,473,251]
ChrisBosh_FG = [549,543,507,615,600,524,393,485,492,343]
ChrisPaul_FG = [407,381,630,631,314,430,425,412,406,568]
KevinDurant_FG = [306,306,587,661,794,711,643,731,849,238]
DerrickRose_FG = [208,208,208,574,672,711,302,0,58,338]
DwayneWade_FG = [699,472,439,854,719,692,416,569,415,509]
#Matrix for field goals
Field_Goals = np.array([KobeBryant_FG, JoeJohnson_FG, LeBronJames_FG, CarmeloAnthony_FG, DwightHoward_FG, ChrisBosh_FG, ChrisPaul_FG, KevinDurant_FG, DerrickRose_FG, DwayneWade_FG])

#Field Goal Attempts
KobeBryant_FGA = [2173,1757,1690,1712,1569,1639,1336,1595,73,713]
JoeJohnson_FGA = [1395,1139,1497,1420,1386,1161,931,1052,1018,1025]
LeBronJames_FGA = [1823,1621,1642,1613,1528,1485,1169,1354,1353,1279]
CarmeloAnthony_FGA = [1572,1453,1481,1207,1502,1503,1025,1489,1643,806]
DwightHoward_FGA = [881,873,974,979,834,1044,726,813,800,423]
ChrisBosh_FGA = [1087,1094,1027,1263,1158,1056,807,907,953,745]
ChrisPaul_FGA = [947,871,1291,1255,637,928,890,856,870,1170]
KevinDurant_FGA = [647,647,1366,1390,1668,1538,1297,1433,1688,467]
DerrickRose_FGA = [436,436,436,1208,1373,1597,695,0,164,835]
DwayneWade_FGA = [1413,962,937,1739,1511,1384,837,1093,761,1084]
#Matrix for field goal attempts
Field_G_Attempts = np.array([KobeBryant_FGA, JoeJohnson_FGA, LeBronJames_FGA, CarmeloAnthony_FGA, DwightHoward_FGA, ChrisBosh_FGA, ChrisPaul_FGA, KevinDurant_FGA, DerrickRose_FGA, DwayneWade_FGA])

#Points
KobeBryant_P = [2832,2430,2323,2201,1970,2078,1616,2133,83,782]
JoeJohnson_P = [1653,1426,1779,1688,1619,1312,1129,1170,1245,1154]
LeBronJames_P = [2478,2132,2250,2304,2258,2111,1683,2036,2089,1743]
CarmeloAnthony_P = [2122,1881,1978,1504,1943,1970,1245,1920,2112,966]
DwightHoward_P = [1292,1443,1695,1624,1503,1784,1113,1296,1297,646]
ChrisBosh_P = [1572,1561,1496,1746,1678,1438,1025,1232,1281,928]
ChrisPaul_P = [1258,1104,1684,1781,841,1268,1189,1186,1185,1564]
KevinDurant_P = [903,903,1624,1871,2472,2161,1850,2280,2593,686]
DerrickRose_P = [597,597,597,1361,1619,2026,852,0,159,904]
DwayneWade_P = [2040,1397,1254,2386,2045,1941,1082,1463,1028,1331]
#Matrix for points
Points = np.array([KobeBryant_P, JoeJohnson_P, LeBronJames_P, CarmeloAnthony_P, DwightHoward_P, ChrisBosh_P, ChrisPaul_P, KevinDurant_P, DerrickRose_P, DwayneWade_P])


# In[150]:


c_dict = {"KobeBryant":'red',"JoeJohnson":'brown',"LeBronJames":'blue',"CarmeloAnthony":'green',"DwightHoward":'black',"ChrisBosh":'pink',"ChrisPaul":'orange',"KevinDurant":'red',"DerrickRose":'yellow',"DwayneWade":'magenta'}
m_dict = {"KobeBryant":'o',"JoeJohnson":'s',"LeBronJames":'^',"CarmeloAnthony":'d',"DwightHoward":'o',"ChrisBosh":'s',"ChrisPaul":'^',"KevinDurant":'d',"DerrickRose":'o',"DwayneWade":'s'}


# In[151]:


#3(i) myplot(Salary) ---- How much each player get paid annually irrespective of the number of games?
def myplot1(playerlist):
    for name in playerlist:
        plt.plot(Salary[Pdict[name]], c=c_dict[name], ls='--', marker=m_dict[name], ms=7, label=name)
    plt.legend(loc='upper left', bbox_to_anchor = (1,1))
    plt.xticks(list(range(0,10)), Seasons, rotation='vertical')
    plt.show()
myplot1(["KobeBryant","JoeJohnson","LeBronJames","CarmeloAnthony","DwightHoward","ChrisBosh","ChrisPaul","KevinDurant","DerrickRose","DwayneWade"])
    


# In[152]:


#3(ii) myplot(Salary/Games) ---- How much each player get paid per game on average? 
Avg_Salary = Salary/Games
def myplot1(playerlist):
    for name in playerlist:
        plt.plot(Avg_Salary[Pdict[name]], c=c_dict[name], ls='--', marker=m_dict[name], ms=7, label=name)
    plt.legend(loc='upper left', bbox_to_anchor = (1,1))
    plt.xticks(list(range(0,10)), Seasons, rotation='vertical')
    plt.show()
myplot1(["KobeBryant","JoeJohnson","LeBronJames","CarmeloAnthony","DwightHoward","ChrisBosh","ChrisPaul","KevinDurant","DerrickRose","DwayneWade"])
    


# In[153]:


#3(iii) myplot(Salary/FieldGoals) ---- How the salary varies with the number of goals scored? 
Salary_Goal_Scored = Salary/Field_Goals
def myplot1(playerlist):
    for name in playerlist:
        plt.plot(Salary_Goal_Scored[Pdict[name]], c=c_dict[name], ls='--', marker=m_dict[name], ms=7, label=name)
    plt.legend(loc='upper left', bbox_to_anchor = (1,1))
    plt.xticks(list(range(0,10)), Seasons, rotation='vertical')
    plt.show()
myplot1(["KobeBryant","JoeJohnson","LeBronJames","CarmeloAnthony","DwightHoward","ChrisBosh","ChrisPaul","KevinDurant","DerrickRose","DwayneWade"])
    


# In[154]:


#3(iv) myplot(Points/MinutesPlayed) 
Points_per_min = Points/Min_Played
def myplot1(playerlist):
    for name in playerlist:
        plt.plot(Points_per_min[Pdict[name]], c=c_dict[name], ls='--', marker=m_dict[name], ms=7, label=name)
    plt.legend(loc='upper left', bbox_to_anchor = (1,1))
    plt.xticks(list(range(0,10)), Seasons, rotation='vertical')
    plt.show()
myplot1(["KobeBryant","JoeJohnson","LeBronJames","CarmeloAnthony","DwightHoward","ChrisBosh","ChrisPaul","KevinDurant","DerrickRose","DwayneWade"])
    


# In[155]:


#3(v) myplot(FieldGoals/Games) 
Goals_per_game = Field_Goals/Games
def myplot1(playerlist):
    for name in playerlist:
        plt.plot(Goals_per_game[Pdict[name]], c=c_dict[name], ls='--', marker=m_dict[name], ms=7, label=name)
    plt.legend(loc='upper left', bbox_to_anchor = (1,1))
    plt.xticks(list(range(0,10)), Seasons, rotation='vertical')
    plt.show()
myplot1(["KobeBryant","JoeJohnson","LeBronJames","CarmeloAnthony","DwightHoward","ChrisBosh","ChrisPaul","KevinDurant","DerrickRose","DwayneWade"])
    


# In[156]:


#3(vi) myplot(FieldGoals/FieldGoalAttempts) 
Goals_per_attemps = Field_Goals/Field_G_Attempts
def myplot1(playerlist):
    for name in playerlist:
        plt.plot(Field_G_Attempts[Pdict[name]], c=c_dict[name], ls='--', marker=m_dict[name], ms=7, label=name)
    plt.legend(loc='upper left', bbox_to_anchor = (1,1))
    plt.xticks(list(range(0,10)), Seasons, rotation='vertical')
    plt.show()
myplot1(["KobeBryant","JoeJohnson","LeBronJames","CarmeloAnthony","DwightHoward","ChrisBosh","ChrisPaul","KevinDurant","DerrickRose","DwayneWade"])
    


# In[157]:


#3(vii) myplot(Points/Games) 
Points_per_game = Points/Games
def myplot1(playerlist):
    for name in playerlist:
        plt.plot(Points_per_game[Pdict[name]], c=c_dict[name], ls='--', marker=m_dict[name], ms=7, label=name)
    plt.legend(loc='upper left', bbox_to_anchor = (1,1))
    plt.xticks(list(range(0,10)), Seasons, rotation='vertical')
    plt.show()
myplot1(["KobeBryant","JoeJohnson","LeBronJames","CarmeloAnthony","DwightHoward","ChrisBosh","ChrisPaul","KevinDurant","DerrickRose","DwayneWade"])
    


# In[158]:


#3(viii) myplot(MinutesPlayed/Games) 
minPlayed_per_game = Min_Played/Games
def myplot1(playerlist):
    for name in playerlist:
        plt.plot(minPlayed_per_game[Pdict[name]], c=c_dict[name], ls='--', marker=m_dict[name], ms=7, label=name)
    plt.legend(loc='upper left', bbox_to_anchor = (1,1))
    plt.xticks(list(range(0,10)), Seasons, rotation='vertical')
    plt.show()
myplot1(["KobeBryant","JoeJohnson","LeBronJames","CarmeloAnthony","DwightHoward","ChrisBosh","ChrisPaul","KevinDurant","DerrickRose","DwayneWade"])
    


# In[159]:


#3(ix) myplot(FieldGoals/MinutesPlayed) 
goals_per_minPlayed = Field_Goals/Min_Played
def myplot1(playerlist):
    for name in playerlist:
        plt.plot(goals_per_minPlayed[Pdict[name]], c=c_dict[name], ls='--', marker=m_dict[name], ms=7, label=name)
    plt.legend(loc='upper left', bbox_to_anchor = (1,1))
    plt.xticks(list(range(0,10)), Seasons, rotation='vertical')
    plt.show()
myplot1(["KobeBryant","JoeJohnson","LeBronJames","CarmeloAnthony","DwightHoward","ChrisBosh","ChrisPaul","KevinDurant","DerrickRose","DwayneWade"])
    


# In[160]:


#3(x) myplot(Points/FieldGoals)--- Player style that whether he likes to score 3 pointer or otherwise. 
points_per_goal = Points/Field_Goals
def myplot1(playerlist):
    for name in playerlist:
        plt.plot(points_per_goal[Pdict[name]], c=c_dict[name], ls='--', marker=m_dict[name], ms=7, label=name)
    plt.legend(loc='upper left', bbox_to_anchor = (1,1))
    plt.xticks(list(range(0,10)), Seasons, rotation='vertical')
    plt.show()
myplot1(["KobeBryant","JoeJohnson","LeBronJames","CarmeloAnthony","DwightHoward","ChrisBosh","ChrisPaul","KevinDurant","DerrickRose","DwayneWade"])
    


# In[ ]:




