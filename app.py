# Core packages
import streamlit as st

# EDA packages
import pandas as pd
import numpy as np
import seaborn as sns

# Viz packages
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Agg")

# ML packages

def main():
    """Project with Streamlit"""

    st.title("Finance ML Project")
    st.text("Using streamlit")

    activites = ["EDA", "Plot", "Model Building", "About"]

    choice = st.sidebar.selectbox("Select activity", activites)

    if choice == "EDA":
        st.subheader("Exploratory Data Analysis")

        data = st.file_uploader("Upload file", type=["csv", "txt"])
        if data is not None:
            df = pd.read_csv(data)
            st.dataframe(df.head())


    elif choice == "Plot":
        st.subheader("Data Visualization")

    elif choice == "Model Building":
        st.subheader("Building ML Model")

    elif choice == "About":
        st.subheader("About")

if __name__ == '__main__':
    main()

