Filename = 'final_model.sav'
pickle.dump(clf, open(Filename, 'wb'))

scaler_Filename = 'final_scalar.sav'
pickle.dump(scaler, open(scaler_Filename, 'wb'))
# DURING TESTING
load_scaler = pickle.load(open(scaler_Filename,'rb'))
X_test = load_scaler.transform(X_test)

load_model = pickle.load(open(Filename,'rb'))
result = load_model.score(X_test,y_test)

print(result)
# ON NEW DATA-SET
Datatopredict = load_scaler.transform(Datatopredict)
prediction = load_model.predict(Datatopredict)
