import pandas as pd
import streamlit as st
from google.oauth2 import service_account
from google.cloud import storage


#  Preparing streamlit app page.
st.sidebar.title('Main Page')
st.title('Hello world')
st.subheader('Step 1')
if st.button('Click'):
 st.write('Some content')
 st.title('Hello world')
 st.subheader('Step 1')

#  Preparing Uploader for datasets or files.
files = st.file_uploader('Upload Your Data',type=['csv', 'xlsx', 'png', 'jpeg', 'jpg' ,'gif', 'docx','pdf'],accept_multiple_files=True)
for file in files:
 if file.type=='text/csv':
     df = pd.read_csv(file)
     file.seek(0)
     st.write(df)
     file_details = {"FileName":file.name,"FileType":file.type}
     st.write(file_details)
 elif file.type=='image/png':
     file.seek(0)
     st.image(file)
     file_details = {"FileName": file.name, "FileType": file.type}
     st.write(file_details)
 elif file.type=='image/jpg':
     file.seek(0)
     st.image(file)
     file_details = {"FileName": file.name, "FileType": file.type}
     st.write(file_details)
 elif file.type=='image/jpeg':
     file.seek(0)
     st.image(file)
     file_details = {"FileName": file.name, "FileType": file.type}
     st.write(file_details)
 elif file.type=='image/gif':
     file.seek(0)
     st.image(file)
     file_details = {"FileName": file.name, "FileType": file.type}
     st.write(file_details)
 elif file.type == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
     df = pd.read_excel(file)
     file.seek(0)
     st.write(df)
     file_details = {"FileName": file.name, "FileType": file.type}
     st.write(file_details)
 else:
     file.seek(0)
     st.write(file)
     file_details = {"FileName": file.name, "FileType": file.type}
     st.write(file_details)
    #  Make a connection between client and GCP (Google Cloud Platform) to hosting datasets or files.
 if files:
     credentials = service_account.Credentials.from_service_account_info(
            st.secrets["gcp_service_account"]
        )
     client = storage.Client(credentials=credentials)
     bucket = client.get_bucket("dataset5320")
     blob = bucket.blob(file.name)
     blob.upload_from_string(file.getvalue(), content_type=file.type)
     st.success("Nice!! Your Dataset has been uploaded successfully to cloud")
