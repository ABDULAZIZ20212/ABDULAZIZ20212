import pandas as pd
import streamlit as st
from google.oauth2 import service_account
from google.cloud import storage

credentials = service_account.Credentials.from_service_account_info(
            st.secrets["gcp_service_account"]
        )
st.write('**Secret:**',st.secrets['secret'])
st.write('**Password:**',st.secrets['section']['password']) 
