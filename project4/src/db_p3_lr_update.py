#!/usr/bin/env python
# coding: utf-8

# In[126]:

import pandas as pd
import pickle


# In[127]:


from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from  sklearn.metrics import accuracy_score 


# In[128]:


# In[129]:


def age_map(x):
    if x >= 0 and x <= 10:
        return 1
    elif x >= 11 and x <= 20:
        return 2
    elif x >= 21 and x <= 30:
        return 3
    elif x >= 31 and x <= 40:
        return 4
    elif x >= 41 and x <= 50:
        return 5
    elif x >= 51 and x <= 60:
        return 6
    elif x >= 61 and x <= 70:
        return 7
    elif x >= 71 and x <= 80:
        return 8
    elif x >= 81 and x <= 90:
        return 9
    elif x >= 91 and x <= 100:
        return 10
    else :
        return 11


# In[130]:


def update(file):
    data = pd.read_csv(file)
    train_len = int((data.shape[0])*0.8)
    train_data = data[0:train_len]
    test_data = data[train_len:]
    feature_Preg_orig_train_f = (train_data["Pregnancies"]-train_data["Pregnancies"].mean())/train_data["Pregnancies"].std()
    feature_Glucose_orig_train_f = (train_data["Glucose"]-train_data["Glucose"].mean())/train_data["Glucose"].std()
    feature_Blood_orig_train_f = (train_data["BloodPressure"]-train_data["BloodPressure"].mean())/train_data["BloodPressure"].std()
    feature_Skin_orig_train_f = (train_data["SkinThickness"]-train_data["SkinThickness"].mean())/train_data["SkinThickness"].std()
    feature_Insulin_orig_train_f = (train_data["Insulin"]-train_data["Insulin"].mean())/train_data["Insulin"].std()
    feature_BMI_orig_train_f = (train_data["BMI"]-train_data["BMI"].mean())/train_data["BMI"].std()
    feature_Func_orig_train_f = train_data["DiabetesPedigreeFunction"]
    all_age_level = data["Age"].map(age_map)
    age_prob = pd.concat([all_age_level[0:train_len], data["Outcome"][0:train_len]], axis = 1).groupby(['Age']).sum(["Outcome"])/train_len
    train_age_frame = all_age_level[0:train_len].to_frame()
    train_age_prob = train_age_frame.join(age_prob, on ="Age")
    feature_train = pd.concat([feature_Preg_orig_train_f, feature_Glucose_orig_train_f, feature_Blood_orig_train_f, 
                           feature_Skin_orig_train_f, feature_Insulin_orig_train_f, feature_BMI_orig_train_f,
                           feature_Func_orig_train_f, train_age_prob
                          ],  axis=1)
    y_train = data["Outcome"][0:train_len]
    pkl_filename = "./pickle_model.pkl"
    with open(pkl_filename, 'rb') as file:
        model = pickle.load(file)
    model = model.fit(feature_train, y_train)
    y_pred_train = model.predict(feature_train)
    print(accuracy_score(y_train, y_pred_train))
    print("\n")
    pkl_filename = "./pickle_model.pkl"
    with open(pkl_filename, 'wb') as file:
        pickle.dump(model, file)


