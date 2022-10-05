# The algorithm's most common use is to make purchase recommendations based on the goods the customer already has in their shopping basket.


# Importing necessary modules
import numpy as np  
import pandas as pd  
from mlxtend.frequent_patterns import apriori, association_rules

# Loading the data, here We have took an example of cart_data.xlsx
data1 = pnd.read_excel('Cart_Data.xlsx')  
data1.head()  

# Exploring more about the column data and transaction countries
data1.columns
data1.Country.unique() 

# Cleaning the Data
data1['Description'] = data1['Description'].str.strip()
data1.dropna(axis = 0, subset = ['InvoiceNo'], inplace = True)  
data1['InvoiceNo'] = data1['InvoiceNo'].astype('str')
data1 = data1[~data1['InvoiceNo'].str.contains('C')]

# Splitting the data according to region
basket1_Region1 = (data1[data1['Country'] == "Region1"]  
        .groupby(['InvoiceNo', 'Description'])['Quantity']  
        .sum().unstack().reset_index().fillna(0)  
        .set_index('InvoiceNo'))  
    
basket1_Region2 = (data1[data1['Country'] == "Region2"]  
        .groupby(['InvoiceNo', 'Description'])['Quantity']  
        .sum().unstack().reset_index().fillna(0)  
        .set_index('InvoiceNo'))  
   
basket1_Region3 = (data1[data1['Country'] == "Region3"]  
        .groupby(['InvoiceNo', 'Description'])['Quantity']  
        .sum().unstack().reset_index().fillna(0)  
        .set_index('InvoiceNo'))  
  
basket1_Region4 = (data1[data1['Country'] == "Region4"]  
        .groupby(['InvoiceNo', 'Description'])['Quantity']  
        .sum().unstack().reset_index().fillna(0)  
        .set_index('InvoiceNo'))

# Here, we will define the hot encoding function    
def hot_encode1(P):  
    if(P<= 0):  
        return 0  
    if(P>= 1):  
        return 1  
  
# Here, we will encode the datasets  
basket1_encoded = basket1_Region1.applymap(hot_encode1)  
basket1_Region1 = basket1_encoded  
  
basket1_encoded = basket1_Region2.applymap(hot_encode1)  
basket1_Region2 = basket1_encoded  
  
basket1_encoded = basket1_Region3.applymap(hot_encode1)  
basket1_Region3 = basket1_encoded  
  
basket1_encoded = basket1_Region4.applymap(hot_encode1)  
basket1_Region4 = basket1_encoded

# Build the model  
frq_items1 = AP(basket1_Region1, min_support = 0.05, use_colnames = True)  
# Collect the inferred rules in a dataframe  
rules1 = AR(frq_items1, metric = "lift", min_threshold = 1)  
rules1 = rules1.sort_values(['confidence', 'lift'], ascending = [False, False])  
print(rules1.head())  

frq_items2 = apriori(basket1_Region2, min_support = 0.01, use_colnames = True)  
rules2 = association_rules(frq_items2, metric ="lift", min_threshold = 1)  
rules2 = rules2.sort_values(['confidence', 'lift'], ascending =[False, False])  
print(rules2.head())  
 
frq_items3 = AP(basket1_Region3, min_support = 0.05, use_colnames = True)  
rules3 = AR(frq_items3, metric ="lift", min_threshold = 1)  
rules3 = rules3.sort_values(['confidence', 'lift'], ascending =[False, False])  
print(rules1.head())

frq_items4 = AP(basket1_Region4, min_support = 0.05, use_colnames = True)  
rules4 = AR(frq_items4, metric ="lift", min_threshold = 1)  
rules4 = rules4.sort_values(['confidence', 'lift'], ascending =[False, False])  
print(rules1.head())

# After Implementing this you will get the trends of data you required