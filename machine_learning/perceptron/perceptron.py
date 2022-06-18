import pandas as pd
data = pd.read_csv("./AND.csv")

output_column = ['Output']

features = list(set(list(data.columns))-set(output_column))

x = data[features].values
y = data[output_column].values

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.25,random_state = 1)

from sklearn.neural_network import MLPClassifier
classifier = MLPClassifier(learning_rate_init = 0.1,random_state = 1)
classifier.fit(x_train,y_train.ravel())

ydash = classifier.predict(x_test)

from sklearn.metrics import confusion_matrix
conf_matr = confusion_matrix(y_test,ydash)

print(conf_matr)
