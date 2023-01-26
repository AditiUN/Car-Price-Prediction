import streamlit as st

st.set_page_config(
    page_title="LR Project"
)

st.title("DashBoard and Model")
st.sidebar.success("Select a page above.")
st.subheader('For The Car You Want You Can Get Prediction Of Price')

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://images.hdqwalls.com/wallpapers/dark-side-car-digital-art-4k-2z.jpg");
             background-attachment: fixed;
	     background-position:75%;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()
