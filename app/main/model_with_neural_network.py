# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 10:57:21 2024

@author: akash
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import tensorflow as tf
from tensorflow import keras

def covid_prediction_with_neural_network(data_path, test_size=0.2, epochs=50):
    """
    Predicts COVID-19 infection likelihood using a neural network.

    Args:
        data_path (str): Path to the Excel data file.
        test_size (float, optional): Proportion of data for testing. Defaults to 0.2.
        epochs (int, optional): Number of training epochs. Defaults to 50.

    Returns:
        tuple: A tuple containing the trained model, the accuracy score, and the history object (or None if an error occurs).
    """
    try:
        data = pd.read_excel(data_path)
        data = data.drop(["Government Id"], axis=1)
        data["Body_temp"].fillna(data["Body_temp"].median(), inplace=True)
        data["Age"].fillna(data["Age"].median(), inplace=True)

        le = LabelEncoder()
        for col in ['Gender', 'Infection_propb']:
            data[col] = le.fit_transform(data[col])

        Y = data["Infection_propb"]
        X = data.drop(["Infection_propb"], axis=1)

        # Feature scaling (important for neural networks)
        scaler = StandardScaler()
        X = scaler.fit_transform(X)

        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=test_size, random_state=42)

        model = keras.Sequential([
            keras.layers.Input(shape=(X_train.shape[1],)), # Input layer
            keras.layers.Dense(128, activation='relu'),  # Hidden layer 1
            keras.layers.Dropout(0.2), # Dropout for regularization
            keras.layers.Dense(64, activation='relu'),   # Hidden layer 2
            keras.layers.Dropout(0.2), # Dropout for regularization
            keras.layers.Dense(1, activation='sigmoid')  # Output layer (sigmoid for binary classification)
        ])

        model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
        history = model.fit(X_train, Y_train, epochs=epochs, validation_data=(X_test, Y_test))
        _, accuracy = model.evaluate(X_test, Y_test)

        return model, accuracy, history

    except Exception as e:
        print(f"An error occurred: {e}")
        return None


# Example usage:
data_file_path = r"C:\Akash\Github\ML-Project\app\data\data_corna_new.xlsx"
results = covid_prediction_with_neural_network(data_file_path)


if results:
    model, accuracy, history = results
    print(f"Neural Network Accuracy: {accuracy}")

    # You can access the training history (e.g., loss, validation accuracy) through the 'history' object.
    # Example:
    # print(history.history['loss'])
    # print(history.history['val_accuracy'])