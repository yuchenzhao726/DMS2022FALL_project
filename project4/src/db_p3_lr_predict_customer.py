#!/usr/bin/env python
# coding: utf-8

# In[132]:


import pandas as pd
import pickle


# In[133]:


from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from  sklearn.metrics import accuracy_score 


# In[134]:


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


# In[147]:


def predictCustomer(preg, glucose, bloodPres, skinThick, insulin, bmi, diaFunc, age):
    data = {'Pregnancies':[preg], 
            'Glucose':[glucose], 
            'BloodPressure':[bloodPres],
            'SkinThickness':[skinThick], 
            'Insulin':[insulin],
            'BMI':[bmi], 
            'DiabetesPedigreeFunction':[diaFunc], 
            'Age':[age]}
    user = pd.DataFrame(data)
    data = pd.read_csv('./diabetes.csv')
    train_len = int((data.shape[0])*0.9)
    train_data = data[0:train_len]
    test_data = data[train_len:]
    feature_Preg_orig_train_f = (user["Pregnancies"]-train_data["Pregnancies"].mean())/train_data["Pregnancies"].std()
    feature_Glucose_orig_train_f = (user["Glucose"]-train_data["Glucose"].mean())/train_data["Glucose"].std()
    feature_Blood_orig_train_f = (user["BloodPressure"]-train_data["BloodPressure"].mean())/train_data["BloodPressure"].std()
    feature_Skin_orig_train_f = (user["SkinThickness"]-train_data["SkinThickness"].mean())/train_data["SkinThickness"].std()
    feature_Insulin_orig_train_f = (user["Insulin"]-train_data["Insulin"].mean())/train_data["Insulin"].std()
    feature_BMI_orig_train_f = (user["BMI"]-train_data["BMI"].mean())/train_data["BMI"].std()
    feature_Func_orig_train_f = user["DiabetesPedigreeFunction"]
    data_all = pd.concat([data["Age"], user["Age"]], axis = 0)
    all_age_level = data_all.map(age_map)
    user_age_level = all_age_level[-1:] 
    age_prob = pd.concat([all_age_level[0:train_len], data["Outcome"][0:train_len]], axis = 1).groupby(['Age']).sum(["Outcome"])/train_len
    train_age_prob = (user_age_level.to_frame()).join(age_prob, on ="Age")
    feature_train = pd.concat([feature_Preg_orig_train_f, feature_Glucose_orig_train_f, feature_Blood_orig_train_f, 
                           feature_Skin_orig_train_f, feature_Insulin_orig_train_f, feature_BMI_orig_train_f,
                           feature_Func_orig_train_f, train_age_prob
                          ],  axis=1)
    with open('./pickle_model.pkl', 'rb') as file:
        model = pickle.load(file)
    y_pred_train = model.predict_proba(feature_train)
    return y_pred_train[0][1]




# In[148]:




