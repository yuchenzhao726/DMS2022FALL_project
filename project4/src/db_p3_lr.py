#!/usr/bin/env python
# coding: utf-8

# In[42]:

import pandas as pd
import pickle

# In[43]:


from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


# In[44]:


def age_map(x):
    if 0 <= x <= 10:
        return 1
    elif 11 <= x <= 20:
        return 2
    elif 21 <= x <= 30:
        return 3
    elif 31 <= x <= 40:
        return 4
    elif 41 <= x <= 50:
        return 5
    elif 51 <= x <= 60:
        return 6
    elif 61 <= x <= 70:
        return 7
    elif 71 <= x <= 80:
        return 8
    elif 81 <= x <= 90:
        return 9
    elif 91 <= x <= 100:
        return 10
    else:
        return 11


# In[50]:


def initialize():
    data = pd.read_csv('./diabetes.csv')
    train_data = data[0:691]
    test_data = data[691:]
    feature_Preg_orig_train_f = (train_data["Pregnancies"] - train_data["Pregnancies"].mean()) / train_data[
        "Pregnancies"].std()
    feature_Preg_orig_test_f = (test_data["Pregnancies"] - train_data["Pregnancies"].mean()) / train_data[
        "Pregnancies"].std()
    feature_Glucose_orig_train_f = (train_data["Glucose"] - train_data["Glucose"].mean()) / train_data["Glucose"].std()
    feature_Glucose_orig_test_f = (test_data["Glucose"] - train_data["Glucose"].mean()) / train_data["Glucose"].std()
    feature_Blood_orig_train_f = (train_data["BloodPressure"] - train_data["BloodPressure"].mean()) / train_data[
        "BloodPressure"].std()
    feature_Blood_orig_test_f = (test_data["BloodPressure"] - train_data["BloodPressure"].mean()) / train_data[
        "BloodPressure"].std()
    feature_Skin_orig_train_f = (train_data["SkinThickness"] - train_data["SkinThickness"].mean()) / train_data[
        "SkinThickness"].std()
    feature_Skin_orig_test_f = (test_data["SkinThickness"] - train_data["SkinThickness"].mean()) / train_data[
        "SkinThickness"].std()
    feature_Insulin_orig_train_f = (train_data["Insulin"] - train_data["Insulin"].mean()) / train_data["Insulin"].std()
    feature_Insulin_orig_test_f = (test_data["Insulin"] - train_data["Insulin"].mean()) / train_data["Insulin"].std()
    feature_BMI_orig_train_f = (train_data["BMI"] - train_data["BMI"].mean()) / train_data["BMI"].std()
    feature_BMI_orig_test_f = (test_data["BMI"] - train_data["BMI"].mean()) / train_data["BMI"].std()
    feature_Func_orig_train_f = train_data["DiabetesPedigreeFunction"]
    feature_Func_orig_test_f = test_data["DiabetesPedigreeFunction"]
    all_age_level = data["Age"].map(age_map)
    all_age = pd.get_dummies(all_age_level, prefix='age')
    train_data_age = all_age[0:691]
    test_data_age = all_age[691:]
    # statistical features
    age_prob = pd.concat([all_age_level[0:691], data["Outcome"][0:691]], axis=1).groupby(['Age']).sum(["Outcome"]) / 691
    train_age_frame = all_age_level[0:691].to_frame()
    train_age_prob = train_age_frame.join(age_prob, on="Age")
    test_age_frame = all_age_level[691:].to_frame()
    test_age_prob = test_age_frame.join(age_prob, on="Age").fillna(0)
    feature_train = pd.concat([feature_Preg_orig_train_f, feature_Glucose_orig_train_f, feature_Blood_orig_train_f,
                               feature_Skin_orig_train_f, feature_Insulin_orig_train_f, feature_BMI_orig_train_f,
                               feature_Func_orig_train_f, train_age_prob
                               ], axis=1)
    feature_test = pd.concat([feature_Preg_orig_test_f, feature_Glucose_orig_test_f, feature_Blood_orig_test_f,
                              feature_Skin_orig_test_f, feature_Insulin_orig_test_f, feature_BMI_orig_test_f,
                              feature_Func_orig_test_f, test_age_prob
                              ], axis=1)
    y_train = data["Outcome"][0:691]
    y_test = data["Outcome"][691:]
    model = LogisticRegression(random_state=0).fit(feature_train, y_train)
    y_pred_test = model.predict(feature_test)
    y_pred_train = model.predict(feature_train)
    print(accuracy_score(y_train, y_pred_train))
    print("\n")
    print(accuracy_score(y_test, y_pred_test))
    print("\n")
    print(model.coef_)
    print("\n")
    pkl_filename = "./pickle_model.pkl"
    with open(pkl_filename, 'wb') as file:
        pickle.dump(model, file)


# In[51]:


initialize()

# In[ ]:
