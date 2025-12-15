import pandas as pd
import streamlit as st
import plotly.express as ps
import json # saving to json file the transactions
import os

# set up the config of thr app page
st.set_page_config(page_title = 'Automated Finance Tracker', page_icon = '💰', layout='wide')


def load_transactions(uploaded_file):
    try:
        df = pd.read_csv(uploaded_file)
        return df
    except Exception as e:
        # error component to show error using streamlit
        st.error(f'There was an error loading transactions {str(e)}')
        return None



def main():
    # set up a file upload
    st.title('Automated Finance Dashboard')
    uploaded_file = st.file_uploader('Upload your transaction CSV file', type=['csv'])
    # st.write(pd.read_csv('sample_bank_statements.csv'))
    if uploaded_file is not None:
        df = load_transactions(uploaded_file)
        st.write(df)
        



main()

# if __name__ == '__main__':
#     main()
