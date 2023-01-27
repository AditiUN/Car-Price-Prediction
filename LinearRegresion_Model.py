import pickle
import streamlit as st
import pandas as pd
import numpy as np

cars = pd.read_csv('C:/Users/Ashwini/Desktop/All Aditi Material/LR_PROJECT/carsEDA.csv')
model = pickle.load(open('C:/Users/Ashwini/Desktop/All Aditi Material/LR_PROJECT/Regressor.pkl', 'rb'))

def main():
    st.title('Cars Price Prediction')
    st.image("Pages//predimage.jpeg")
    
    #input variables
    Company = st.selectbox("Company", cars['Company'].unique())
    Name = st.selectbox("Name", cars['Name'].unique())
    Transmission = st.selectbox("Transmission", cars['Transmission'].unique())
    Fuel_Type = st.selectbox("Fuel_Type", cars['Fuel_Type'].unique())
    City = st.selectbox("City", cars['City'].unique())
    Year = st.selectbox("Year", cars['Year'].unique())
    KM_Driven= st.selectbox("KM_Driven", cars['KM_Driven'].unique()) 


    #prediction code
    if st.button('Predict'):
        makeprediction = model.predict(pd.DataFrame(columns=['Name', 'Company', 'Transmission', 'Fuel_Type', 'City', 'Year', 'KM_Driven'],
                              data=np.array([Name, Company, Transmission, Fuel_Type, City, Year, KM_Driven]).reshape(1, 7)))
        output = round(makeprediction[0],2)
        st.success('Car Price is {}'.format(output))


if __name__=='__main__':
    main()
