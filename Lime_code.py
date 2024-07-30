
# Interprete the model using LIME to understand how it works
!pip install lime
# import Explainer function from lime_tabular module of lime library
from lime.lime_tabular import LimeTabularExplainer

# Create an explainer object
explainer = LimeTabularExplainer(x_train.values, feature_names=x_train.columns, mode='regression')

# storing a new observation
i = 6
X_observation = x_test.iloc[[i], :]
X_observation

exp = explainer.explain_instance(X_observation.values[0], best_modelXGBR.predict, num_features=5)
exp.show_in_notebook(show_table=True, show_all=False)
print(exp.score)
