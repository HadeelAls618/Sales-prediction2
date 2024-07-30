
# Split the data
from sklearn.model_selection import train_test_split
x = data.drop('Item_Outlet_Sales', axis=1)
y = data['Item_Outlet_Sales']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
