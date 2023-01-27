import streamlit as st
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
import time
import plotly.express as px 

cars = pd.read_csv('C:/Users/Ashwini/Desktop/All Aditi Material/LR_PROJECT/data.csv')

st.set_page_config(
    page_title = 'Real-Time Dashboard and Price Prediction',
    page_icon = '✅',
    layout = 'wide'
)
# dashboard title
st.title("Live Dashboard")

# Dropdown list 
City_filter = st.sidebar.selectbox("Select the City", pd.unique(cars['City']))
Year_filter = st.sidebar.selectbox("Select the Year", pd.unique(cars['Year']))

#to get a particular catagories from column 
cars = cars[cars['City']==City_filter]
cars = cars[cars['Year']==Year_filter]

# creating box 
a1, a2 = st.columns(2)
avg_price = np.mean(cars['Price'])
a1.metric(label="Price", value=round(avg_price))

avg_km_driven = np.mean(cars['KM_Driven'])
a2.metric(label='KM_Driven', value=round(avg_km_driven))

#creating graphs
st.markdown("### First Chart")
fig2 = px.histogram(data_frame = cars, y = 'Year' , x = 'Price')
fig2.update_layout(bargap=0.2)
st.write(fig2)

st.markdown("### Second Chart")
fig3=plt.figure(figsize=(15,7))
sns.boxplot(x='Types',y='Price',data=cars)
st.pyplot(fig3)

st.markdown("### Third Chart")
fig4=plt.figure(figsize=(5,2))
cars['Owner'].value_counts().plot(kind='pie')
st.pyplot(fig4)

st.markdown("### Fourth Chart")
fig = px.density_heatmap(data_frame=cars, y = 'Price', x = 'City')
st.write(fig)

st.markdown("### Fifth Chart")
fig6=plt.figure(figsize=(15,7))
st.bar_chart(data= cars, x = "Types" , y = "KM_Driven")

st.markdown("### Detailed Data View")
st.dataframe(cars)
