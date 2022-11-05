# streamlit_app.py
import datetime,time
import os
import streamlit as st
from google.oauth2 import service_account
from google.cloud import storage

# Create API client.
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"]
)
client = storage.Client(credentials=credentials)

# Retrieve file contents.
# Uses st.experimental_memo to only rerun when the query changes or after 10 min.
# @st.experimental_memo(ttl=600)
# def read_file(bucket_name, file_path):
bucket = client.get_bucket("dataset5320")
#     content = bucket.blob(file_path).download_as_string().decode("utf-8")
#     return content
#
# bucket_name = "dataset5320"
file_path = ("exams10.csv")
# blob = bucket.blob(file_path)
# with open('C:\\Users\\MY PC\\Desktop\\exams.csv')as f:
#     blob.upload_from_file(f)

blob = bucket.blob(file_path)
blob.upload_from_filename('ABDULAZIZ20212/Vs.csv',content_type='text/csv')
st.write("upload complete")

# print("upload complete")
# content = read_file(bucket_name, file_path)
# df.to_csv()
# bucket.blob ( 'tsla( 0 ).csv'.format(datetime.datetime.now( ).strftime('%Y-%m-%d %H_%M_%s'))).upload_from_string('text/csv')
# Print results.
# st.write(content)
