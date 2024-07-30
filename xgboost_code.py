
# Install XGBoost
!pip install xgboost

# Import XGBoost and other necessary libraries
from xgboost import XGBRegressor
from sklearn.model_selection import RandomizedSearchCV

# Create the parameter grid
param_grid = {
    'n_estimators': [100, 200, 300],
    'learning_rate': [0.01, 0.05, 0.1],
    'max_depth': [3, 5, 7],
    'min_child_weight': [1, 3, 5],
    'gamma': [0, 0.1, 0.3],
    'subsample': [0.8, 0.9, 1.0],
    'colsample_bytree': [0.8, 0.9, 1.0],
    'reg_alpha': [0, 0.01, 0.1],
    'reg_lambda': [1, 1.5, 2]
}

# Initialize the model
model_XGBR = XGBRegressor(objective='reg:squarederror', random_state=42)

# Perform Grid Search with Cross Validation
random_search = RandomizedSearchCV(estimator=model_XGBR, param_distributions=param_grid, n_iter=10, cv=3, n_jobs=-1, scoring='neg_mean_squared_error', verbose=1)
random_search.fit(x_train, y_train)

# Get the best parameters
best_params = random_search.best_params_
print(f'Best parameters found: {best_params}')

# Use the best parameters to create the final model
best_modelXGBR = random_search.best_estimator_

# Train the model
best_modelXGBR.fit(x_train, y_train)

#evaluate the model
# Compute RMSE from MSE
from sklearn.metrics import mean_squared_error
import numpy as np
y_pred = best_modelXGBR.predict(x_test)
mse = mean_squared_error(y_test, y_pred)
rmse_XGBR = np.sqrt(mse)
print(f'RMSE on test set: {rmse_XGBR:.3f}')

# saving the best model
import pickle
pickle_out = open("Model_XGBR.pkl", mode = "wb")
pickle.dump(best_modelXGBR, pickle_out)
pickle_out.close()
