import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('german_credit_data.csv')

print(data.head())
print(data.info())
print(data.isnull().sum())

sns.countplot(x='Risk', data=data)
plt.title('Distribution of Risk')
plt.show()
