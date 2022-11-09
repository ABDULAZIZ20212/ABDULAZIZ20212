import pandas as pd
import streamlit as st
from google.oauth2 import service_account
from google.cloud import storage

import streamlit as st
st.write('**Secret:**',st.secrets['secret'])
st.write('**Password:**',st.secrets['section']['password']) 
