# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 21:38:41 2024

@author: Deepak Raj.M
"""

import numpy as np
import pickle
import streamlit as st

# loading the saved model
loaded_model = pickle.load(open('C:/Users/Deepak Raj.M/Desktop/Mini Project/trained_model.sav', 'rb'))

# creating a function for prediction
def heartdisease_prediction(input_data):

    # change the input data to a numpy array
    input_data_as_numpy_array= np.asarray(input_data)

    # reshape the numpy array as we are predicting for only one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0]== 0):
      return 'The person does not have a heart disease'
    else:
      return 'The person has heart disease'
  
def main():
    
    # giving a title
    st.title('Heart Disease Prediction Web App')
    
    # getting the input data from the user
    age = st.text_input('Age of the Person')
    sex = st.text_input('Gender of the Person (0 or 1)')
    cp = st.text_input('Chest Pain Type')
    trestbps = st.text_input('Resting Blood Pressure (in mm/hg)')
    chol = st.text_input('Cholesterol (in mg/dl)')
    fbs = st.text_input('Fasting Blood Sugar (in mg/dl)')
    restecg = st.text_input('Resting ECG Results')
    thalach = st.text_input('Max Heart Rate Achieved')
    exang = st.text_input('Exercise Induced Angina')
    oldpeak = st.text_input('ST Depression induced by exercise relative to rest')
    slope = st.text_input('Slope of the Peak Exercise ST Segment')
    ca = st.text_input('Number of Major Vessels')
    thal = st.text_input('Thalassemia')
    
    # code for prediction
    diagnosis = ''
    
    # creating a button for prediction
    if st.button('Heart Disease Test Result'):
        diagnosis = heartdisease_prediction([age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal])
        
    st.success(diagnosis)
    
    if __name__ == '__main__':
        main()