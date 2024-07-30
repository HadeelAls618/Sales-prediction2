
# Install LightGBM
!pip install lightgbm

# Import LightGBM and other necessary libraries
from lightgbm import LGBMRegressor
from sklearn.model_selection import RandomizedSearchCV

# Create the parameter grid
param_grid = {
    'n_estimators': [100, 200, 300],
    'learning_rate': [0.01, 0.05, 0.1],
}

# Initialize the model
model_LGBM = LGBMRegressor(random_state=42)

# Perform Grid Search with Cross Validation
random_search = RandomizedSearchCV(estimator=model_LGBM, param_distributions=param_grid, n_iter=10, cv=3, n_jobs=-1, scoring='neg_mean_squared_error', verbose=1)
random_search.fit(x_train, y_train)

# Get the best parameters
best_params = random_search.best_params_
print(f'Best parameters found: {best_params}')

# Use the best parameters to create the final model
best_modelLGBM = random_search.best_estimator_

# Train the model
best_modelLGBM.fit(x_train, y_train)

# Compute RMSE from MSE
from sklearn.metrics import mean_squared_error
import numpy as np
y_pred = best_modelLGBM.predict(x_test)
mse = mean_squared_error(y_test, y_pred)
rmse_LGBMR = np.sqrt(mse)
print(f'RMSE on test set: {rmse_LGBMR:.3f}')
