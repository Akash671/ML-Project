# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 10:56:13 2024

@author: PCAT
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB

def covid_prediction_with_multiple_algorithms(data_path, test_size=0.2):
    """
    Predicts COVID-19 infection likelihood using multiple algorithms and evaluates their accuracy.

    Args:
        data_path (str): Path to the Excel data file.
        test_size (float, optional): Proportion of data for testing. Defaults to 0.2.

    Returns:
        dict: A dictionary containing accuracy scores for each algorithm or None if an error occurs.
    """
    try:
        data = pd.read_excel(data_path)
        data = data.drop(["Government Id"], axis=1)
        data["Body_temp"].fillna(data["Body_temp"].median(), inplace=True)
        data["Age"].fillna(data["Age"].median(), inplace=True)

        le = LabelEncoder()
        for col in ['Gender', 'Infection_propb']: # Encode all string columns
            data[col] = le.fit_transform(data[col])


        Y = data["Infection_propb"]
        X = data.drop(["Infection_propb"], axis=1)
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=test_size, random_state=42)

        models = {
            "Logistic Regression": LogisticRegression(),
            "Decision Tree": DecisionTreeClassifier(),
            "Random Forest": RandomForestClassifier(),
            "Gradient Boosting": GradientBoostingClassifier(),
            "Support Vector Machine": SVC(),
            "Naive Bayes": GaussianNB(),
        }

        results = {}
        for name, model in models.items():
            model.fit(X_train, Y_train)
            Y_pred = model.predict(X_test)
            accuracy = accuracy_score(Y_test, Y_pred)
            results[name] = accuracy

        return results

    except Exception as e:
        print(f"An error occurred: {e}")
        return None



# Example usage:
data_file_path = r"C:\Akash\Github\ML-Project\app\data\data_corna_new.xlsx"
results = covid_prediction_with_multiple_algorithms(data_file_path)

if results:
    for name, accuracy in results.items():
        print(f"{name}: {accuracy}")