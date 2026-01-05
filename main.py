import pandas as pd
import streamlit as st
import plotly.express as ps
import json # saving to json file the transactions
import os


# setup the app page using streamlit
st.set_page_config(page_title='Automated Finance Tracker', page_icon='💰', layout='wide')

# method to create a data frame (table) from the uploaded csv file.
# we will be adding additional functionalities to clean up the csv file that will allow us to modify it.
# NOTE df.columns = selects all columns from the data frame (not each columns)
# NOTE df['Amount'] is used to select specific column from all columns. We selected all amounts, converted it to string then removed all ',' 
# then finally converting it to a float
# NOTE df['Date'] = selects all entries in the Date column. Converted the date in the csv file to datetime that can be parsed by panda

def load_transactions(file):
    try:
        df = pd.read_csv(file)
        df.columns = [cols.strip() for cols in df.columns]
        df['Amount'] = df['Amount'].str.replace(',','').astype(float)
        df['Date']  = pd.to_datetime(df['Date'], format='%d %b %Y')
        return df
    except Exception as e:
        st.error(f'There was a problem loading transaction from upload:\n{e}')
        return None

    


def main():
    st.title('Automated Personal Finance Tracker')
    uploaded_file = st.file_uploader('Upload CSV file', type='csv')

    if uploaded_file is not None:
        # df (data frame will be the returned value of the load_transaction method (cleaned up csv file))
        df = load_transactions(uploaded_file)
        # st.write(df) # displays the table

        if df is not None:
            debit_df = df['Debit/Credit'] == 'Debit'
            st.write(debit_df)

        


if __name__ == '__main__':
    main()