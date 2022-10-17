#!/usr/bin/env python

# In[5]:


import pandas as pd
from category_encoders import OrdinalEncoder
from lightgbm import LGBMRegressor
from shapash.data.data_loader import data_loading
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.model_selection import train_test_split

# # Building Supervized Model

# In[10]:



house_df, house_dict = data_loading("house_prices")


# In[11]:


y_df = house_df["SalePrice"].to_frame()
X_df = house_df[house_df.columns.difference(["SalePrice"])]


# In[12]:


house_df.shape


# In[14]:


house_df.head()


# # Encoding Categorical Features

# In[15]:


from category_encoders import OrdinalEncoder

categorical_features = [col for col in X_df.columns if X_df[col].dtype == "object"]

encoder = OrdinalEncoder(
    cols=categorical_features, handle_unknown="ignore", return_df=True
).fit(X_df)

X_df = encoder.transform(X_df)


# # Train / Test Split

# In[16]:


Xtrain, Xtest, ytrain, ytest = train_test_split(
    X_df, y_df, train_size=0.75, random_state=1
)


# # Model Fitting

# In[17]:


regressor = LGBMRegressor(n_estimators=200).fit(Xtrain, ytrain)


# # Declare and Compile SmartExplainer

# In[18]:


from shapash import SmartExplainer

# In[19]:


xpl = SmartExplainer(
    model=regressor,
    preprocessing=encoder,  # Optional: compile step can use inverse_transform method
    features_dict=house_dict,  # optional parameter, specifies label for features name
)


# In[20]:


xpl.compile(x=Xtest)


# # Start WebApp

# In[21]:


app = xpl.run_app(title_story="House Prices")


# # Stop WebApp

# In[22]:


app.kill()


# # Export local explaination in DataFrame

# In[23]:


summary_df = xpl.to_pandas(
    max_contrib=3,  # Number Max of features to show in summary
    threshold=5000,
)


# In[24]:


summary_df.head()


# # In jupyter

# In[25]:


y_pred = pd.DataFrame(regressor.predict(Xtest), columns=["pred"], index=Xtest.index)


# In[26]:


xpl.compile(x=Xtest, y_pred=y_pred)


# # Display features importance

# In[27]:


xpl.plot.features_importance()


# In[28]:


xpl.plot.contribution_plot("OverallQual")


# In[29]:


xpl.plot.contribution_plot("Second floor square feet")


# In[30]:


xpl.filter(max_contrib=8, threshold=100)


# # Display local plot, applying your filter

# In[31]:


xpl.plot.local_plot(index=560)


# # Save your Explainer & Export resultssummary_df.head()

# In[32]:


summary_df = xpl.to_pandas(
    max_contrib=3,  # Number Max of features to show in summary
    threshold=5000,
)


# In[33]:


summary_df.head()


# In[ ]:
