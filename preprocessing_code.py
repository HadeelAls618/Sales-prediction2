
import pandas as pd
data=pd.read_csv('big_mart_data.zip')
data.head()
# Check the missing values
data.isna().sum()

# Map the categorical variables to numerical
data['Item_Fat_Content'] = data['Item_Fat_Content'].map({'Low Fat': 0, 'Regular': 1})
data['Item_Type'] = data['Item_Type'].map({'Dairy': 0, 'Drinks': 1, 'Fruits': 2, 'Others': 3})
data['Outlet_Size'] = data['Outlet_Size'].map({'Small': 0, 'Medium': 1, 'High': 2})
data.head()
