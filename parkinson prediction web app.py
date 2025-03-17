# -*- coding: utf-8 -*-
"""
Created on Sun Mar 16 23:50:30 2025

@author: user
"""

import numpy as np
import pickle
import streamlit as st

loaded_model= pickle.load(open('E:/Parkin/trained_model.sav','rb'))
#creating a function for real time prediction

def parkinson_prediction(input_data):
  
    #convert tuple into numpy array
    input_data_as_numpy_array=np.asarray(input_data)
    #reshape the array because eta na hole model main dataset er row column ke dhore boshe thakbe. tai 1 ta data point er jonno reshape kora lage

    input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)

    #difference is here at loaded_model keyword here we store all value of traning
    prediction=loaded_model.predict(input_data_reshaped)
    print(prediction)
    if prediction[0]==0:
      return 'Healthy'
    else:
      return 'Parkinsons affected'
  
def main():
    #title
    st.title ('Parkinson Prediction Web App')
    
    #getting input data from user
    
    
    Fo=st.text_input("Average vocal fundamental frequency")
    Fhi=st.text_input("Maximum vocal fundamental frequency")
    Flo=st.text_input("Minimum vocal fundamental frequency") 
    Jitter=st.text_input(" Several measures of variation in fundamental frequency0")
    Jitterabs=st.text_input(" Several measures of variation in fundamental frequency1")
    
    RAP=st.text_input("Several measures of variation in fundamental frequency2")
    MDVP=st.text_input("Several measures of variation in fundamental frequency3")
    DDP=st.text_input("Several measures of variation in fundamental frequency4")
    Shimmer1=st.text_input(" Several measures of variation in amplitude1")
    Shimmer2=st.text_input(" Several measures of variation in amplitude2")
    APQ3=st.text_input(" Several measures of variation in amplitude3")
    APQ5=st.text_input(" Several measures of variation in amplitude4")
    APQ=st.text_input(" Several measures of variation in amplitude5")
    DDA=st.text_input(" Several measures of variation in amplitude6")
    NHR=st.text_input("Two measures of ratio of noise to tonal components in the voice1")
    HNR=st.text_input("Two measures of ratio of noise to tonal components in the voice2")
    RPDE=st.text_input("Two nonlinear dynamical complexity measures1") 
    DFA=st.text_input(" Signal fractal scaling exponen")
    spread1=st.text_input("Three nonlinear measures of fundamental frequency variation1")
    spread2=st.text_input("Three nonlinear measures of fundamental frequency variation2")
    D2=st.text_input("Two nonlinear dynamical complexity measures2")
    PPE=st.text_input("Three nonlinear measures of fundamental frequency variation3")
    
    #for diagnosis
    status= ''
    
    #creating enter for prediction
    if st.button('Parkinson TEST Result'):
        status=parkinson_prediction([Fo, Fhi, Flo,Jitter,Jitterabs,RAP,MDVP,DDP,Shimmer1,Shimmer2,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE])
    
    st.success(status)
    
    
    
if __name__=='__main__':
    main()
     
    
    
    
    
    