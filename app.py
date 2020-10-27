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
            data.seek(0)
            df = pd.read_csv(data, delimiter=",")
            st.dataframe(df.head())

            if st.checkbox("Show shape"):
                st.write(df.shape)

            if st.checkbox("Show columns"):
                all_columns = df.columns.to_list()
                st.write(all_columns)

            if st.checkbox("Choose column"):
                selected_columns = st.multiselect("Select Columns", all_columns)
                new_df = df[selected_columns]
                st.dataframe(new_df)

            if st.checkbox("Show Summary"):
                st.write(df.describe())

            if st.checkbox("Show Null Values"):
                st.write(df.isna().sum())


    elif choice == "Plot":
        st.subheader("Data Visualization")
        st.set_option('deprecation.showPyplotGlobalUse', False)

        data = st.file_uploader("Upload file", type=["csv", "txt"])
        if data is not None:
            data.seek(0)
            df = pd.read_csv(data, delimiter=",")
            st.dataframe(df.head())

        if st.checkbox("Correlation with Seaborn"):
            st.write(sns.heatmap(df.corr(), annot = True))
            st.pyplot()

        if st.checkbox("Pie Chart"):
            all_columns = df.columns.to_list()
            columns_to_plot = st.selectbox("Select 1 column", all_columns)
            pie_plot = df[columns_to_plot].value_counts().plot.pie(autopct = "%1.1f%%")
            st.write(pie_plot)
            st.pyplot()

        type_of_plot = st.selectbox("Select type of Plot", ['area', 'bar', 'line', 'hist', 'box', 'kde'])
        all_columns = df.columns.to_list()
        selected_columns_names = st.multiselect("Select Columns to plot", all_columns)

        if st.button("Generate Plot"):
            st.success("Generating Customizable Plot of {} for {}".format(type_of_plot, selected_columns_names))

        # Plot by streamlit
        if type_of_plot == 'area':
            cust_data = df[selected_columns_names]
            st.area_chart(cust_data)

        elif type_of_plot == 'bar':
            cust_data = df[selected_columns_names]
            st.area_chart(cust_data)

        elif type_of_plot == 'line':
            cust_data = df[selected_columns_names]
            st.area_chart(cust_data)

        elif type_of_plot:
            cust_plot = df[selected_columns_names].plot(kind = type_of_plot)
            st.write(cust_plot)
            st.pyplot()

        


    elif choice == "Model Building":
        st.subheader("Building ML Model")

    elif choice == "About":
        st.subheader("About")

if __name__ == '__main__':
    main()

