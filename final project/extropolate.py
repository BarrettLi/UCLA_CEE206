import numpy as np
import pandas as pd

# Part 1 - data preprocessing
dataset = pd.read_csv("data/thermo.csv")
y = dataset.iloc[:, 0].values
X = dataset.iloc[:, 1:].values
# print(X)
# print(y)
# Splitting the dataset into the Training set and Testing set
SIZE = int(len(X) * 0.2)
def split(X, y, index):
    start = SIZE * index
    end = SIZE * (index + 1)
    X_test, y_test = X[start: end], y[start: end]
    X_train, y_train = np.delete(X, [_ for _ in range(start, end)], 0), np.delete(y, [_ for _ in range(start, end)], 0)
    return X_train, X_test, y_train, y_test

y_pred = []
y_true = []
for i in range(5):
    X_train, X_test, y_train, y_test = split(X, y, i) 
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

    y_pred.append(reg.predict(X_test))
    y_true.append(y_test)

# part 3 - evaluate results
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error

for i in range(len(y_true)):
    print(r2_score(y_pred=y_pred[i], y_true=y_true[i]))
    print(mean_squared_error(y_true[i], y_pred[i]))
# print(mean_absolute_error(y_test, y_pred))
import matplotlib.pyplot as plt

for i in range(5):
    plt.plot(y_true[i], y_pred[i])
    plt.title("Extrapolation in [{}, {}]".format(i * SIZE, (i + 1) * SIZE))
    plt.xlabel("damping parameter")
    plt.ylabel("predicted damping parameter")
    plt.show()
