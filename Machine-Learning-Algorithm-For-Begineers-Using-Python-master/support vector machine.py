import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
sc_x=StandardScaler()
sc_y=StandardScaler()
x=sc_x.fit_transform(x)
y=sc_y.fit_transform(y)

dataset=pd.read_csv("Position_Salaries.csv")
x=dataset.iloc[:,1:2].values
y=dataset.iloc[:,2].values


y_pred=sc_y.inverse_transform(regressor.predict(sc_x.transform(np.array([6.5]))))

plt.scatter(x,y,color='red')
plt.plot(x,regressor.predict(x),color='blue')
plt.title("truth or bluff")
plt.xlabel("positionlevel")
plt.ylabel("salaries")
plt.show