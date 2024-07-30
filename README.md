# Sales Prediction Application

**Overview**
Welcome to our Sales Prediction Application! 🎉 In this project, we embarked on a journey to accurately forecast sales across various stores using advanced machine learning techniques. Our goal was to develop a robust predictive model capable of estimating sales with high precision, ensuring that businesses can make informed decisions and optimize their operations effectively.

**Problem Statement**
In the retail world, predicting sales with accuracy can make a significant difference in inventory management, marketing strategies, and overall business performance. We aimed to solve this problem by leveraging state-of-the-art machine learning models to predict store sales based on various features.

**Solution Approach**
We employed a variety of machine learning techniques to achieve our goal:

* Data Preprocessing:

Dataset: We used the Big Mart dataset, which includes various features related to store and item characteristics. This dataset was cleaned and preprocessed to make it more manageable and effective for our models.
Feature Engineering: Categorical variables were mapped to numerical values, and missing values were addressed to ensure data quality.
Model Selection and Training:

XGBoost: An efficient and scalable gradient boosting model. We optimized it using Randomized Search to find the best hyperparameters.
LightGBM: A powerful gradient boosting framework that handles large datasets efficiently. We also applied Randomized Search for parameter tuning.
Neural Network: We built a custom neural network from scratch to explore deep learning capabilities in predicting sales.
For each model, we evaluated performance using Root Mean Squared Error (RMSE) to determine which model provided the most accurate predictions.

* Model Evaluation:

RMSE Comparison: We compared the RMSE scores of the XGBoost, LightGBM, and Neural Network models. The XGBoost model outperformed the others, making it our choice for deployment.
Model Interpretation: To understand how our chosen model works, we used LIME (Local Interpretable Model-agnostic Explanations) to gain insights into the model’s predictions and ensure transparency.
Deployment:

We developed a web application using Streamlit to provide an intuitive user interface for making predictions.
Ngrok was used to make the locally-hosted web application publicly accessible.
Application Features
Our web application allows users to input the following information to predict sales for a store:

* Item Fat Content
* Outlet Size
* Item Type
* Item Weight
* Item MRP
The application processes this input and provides a sales prediction using the trained XGBoost model, which has been evaluated and selected as the best performing model.
