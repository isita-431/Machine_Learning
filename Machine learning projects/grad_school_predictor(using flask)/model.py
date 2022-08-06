# Importing the libraries
# import numpy as np
# import matplotlib.pyplot as plt
# import pandas as pd
# import pickle

# dataset = pd.read_csv('hiring.csv')

# dataset['experience'].fillna(0, inplace=True)

# dataset['test_score'].fillna(dataset['test_score'].mean(), inplace=True)

# X = dataset.iloc[:, :3]

# #Converting words to integer values
# def convert_to_int(word):
#     word_dict = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8,
#                 'nine':9, 'ten':10, 'eleven':11, 'twelve':12, 'zero':0, 0: 0}
#     return word_dict[word]

# X['experience'] = X['experience'].apply(lambda x : convert_to_int(x))

# y = dataset.iloc[:, -1]

# #Splitting Training and Test Set
# #Since we have a very small dataset, we will train our model with all availabe data.

# from sklearn.linear_model import LinearRegression
# regressor = LinearRegression()

# #Fitting model with trainig data
# regressor.fit(X, y)

# # Saving model to disk
# pickle.dump(regressor, open('model.pkl','wb'))

# # Loading model to compare the results
# model = pickle.load(open('model.pkl','rb'))
# print(model.predict([[2, 9, 6]]))
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import warnings
import pickle
warnings.filterwarnings("ignore")

data = pd.read_csv("Admission_Predict.csv")
print(data.head())
X=data.drop(columns=['Chance of Admit ','Serial No.'], axis=1)
y=data['Chance of Admit ']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
log_reg = LogisticRegression()
y_train_c = [1 if each > 0.8 else 0 for each in y_train]
y_test_c  = [1 if each > 0.8 else 0 for each in y_test]

log_reg.fit(X_train, y_train_c)
predictions = log_reg.predict(X_test)
print(predictions)
final=[[333,115,4,4.0,4.5,9.52,1]]
b = log_reg.predict_proba(final)
print(b)
pickle.dump(log_reg,open('model.pkl','wb'))
model=pickle.load(open('model.pkl','rb'))