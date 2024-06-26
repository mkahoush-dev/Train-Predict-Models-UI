
import train_streamlit as app1
import predict_streamlit as app2
import streamlit as st

# Define pages based on apps imported.
PAGES = {
    "Train": app1,
    "Predict": app2
}

st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()