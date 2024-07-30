
# Define and train the Neural Network model
from keras.models import Sequential
from keras.layers import Dense, BatchNormalization
from keras.optimizers import Adam

# Define the model
model_NN = Sequential()
model_NN.add(Dense(64, input_dim=5, activation='relu'))
model_NN.add(BatchNormalization())
model_NN.add(Dense(128, activation='relu'))
model_NN.add(BatchNormalization())
model_NN.add(Dense(64, activation='relu'))
model_NN.add(BatchNormalization())
model_NN.add(Dense(32, activation='relu'))
model_NN.add(BatchNormalization())
model_NN.add(Dense(1, activation='linear'))

# Compile the model
optimizer = Adam(learning_rate=0.001)
model_NN.compile(loss='mse', optimizer=optimizer, metrics=['mse', 'mae'])

# Train the model
model_NN.fit(x_train, y_train, epochs=100, batch_size=64)


# Compute RMSE from MSE
from sklearn.metrics import mean_squared_error
import numpy as np
y_pred = model_NN.predict(x_test)
mse = mean_squared_error(y_test, y_pred)
rmse_NN = np.sqrt(mse)
print(f'RMSE on test set: {rmse_NN:.3f}')
