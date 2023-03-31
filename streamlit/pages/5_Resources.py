# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
#import data

st.set_page_config(page_title='Resources', page_icon=':glass:', layout='wide')
st.title('We use data and information from:')
fec = '[Federal Electoral Commission](https://www.fec.gov/campaign-finance-data/congressional-candidate-data-summary-tables/?year=2022&segment=18)'
st.markdown(fec, unsafe_allow_html=True)
opensecrets = '[OpenSecrets](https://www.opensecrets.org/elections-overview)'
st.markdown(opensecrets, unsafe_allow_html=True)

