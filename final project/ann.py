import numpy as np
import pandas as pd

# Part 1 - data preprocessing
dataset = pd.read_csv("data/thermo.csv")
y = dataset.iloc[:, 0].values
X = dataset.iloc[:, 1:].values
# print(X)
# print(y)
# Splitting the dataset into the Training set and Testing set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Part 2 - making ANN
import keras
from keras.models import Sequential
from keras.layers import Dense

reg = Sequential()
# input layer and first hidden layer
reg.add(Dense(units=51, kernel_initializer="uniform", activation="relu", input_dim=X_train.shape[1]))
# second hidden layer
reg.add(Dense(units=51, kernel_initializer="uniform", activation="relu"))
# output layer
reg.add(Dense(units=1, kernel_initializer="uniform", activation="linear"))

# compile ANN
reg.compile(optimizer="Nadam", loss="mean_squared_error", metrics=["mean_squared_error"])

reg.fit(X_train, y_train, batch_size=10, epochs=240)

y_pred = reg.predict(X_test)

# part 3 - evaluate results
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error

# print(mean_absolute_error(y_test, y_pred))
import matplotlib.pyplot as plt

plt.scatter(y_test, y_pred)
plt.xlabel("damping parameter")
plt.ylabel("predicted damping parameter")
plt.title("y_true vs. y_pred")
plt.show()

# print(r2_score(y_test, y_pred))
with open("log/result.txt", "w") as fd:
    fd.write("RMSE: {}\n".format(np.sqrt(mean_squared_error(y_test, y_pred))))
    fd.write("R2: {}\n".format(r2_score(y_test, y_pred)))