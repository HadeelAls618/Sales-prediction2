
# Code for comparing the results of three models
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

models = ['XGBoost Model', 'LightBm Model', 'Nueral network Model']
rmse_scores = [rmse_XGBR, rmse_LGBMR, rmse_NN] 

# Create a DataFrame for better visualization
import pandas as pd
data = pd.DataFrame({'Model': models, 'RMSE': rmse_scores})

# Plotting
sns.set(style="whitegrid")
plt.figure(figsize=(10, 5))
barplot = sns.barplot(x='Model', y='RMSE', data=data, palette='viridis')
#plt.title('Comparison of RMSE Scores')
plt.xlabel('Model')
plt.ylabel('RMSE')

 #Adding the RMSE score above each bar
for index, row in data.iterrows():
    barplot.text(index, row.RMSE, round(row.RMSE, 2), color='black', ha="center")
plt.ylim(0, max(rmse_scores) + 0.1)  # Adjust the y-limit for better visualization

# Save the figure
plt.savefig('model_comparison_figure.png')

plt.show()
