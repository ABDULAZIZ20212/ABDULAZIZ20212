import pandas as pd
import streamlit as st
import streamlit_option_menu
from google.oauth2 import service_account
from google.cloud import storage
from streamlit_option_menu import option_menu

with st.sidebar:
    # 1. as sidebar menu
    selected3 = option_menu(None, ["Home", "Uploads", "Contact Us", 'Settings'],
                            icons=['house', 'cloud-upload', "list-task", 'gear'],
                            menu_icon="cast", default_index=0, orientation="",
                            styles={
                                "container": {"": "", "background-color": "#fafafa"},
                                "icon": {"color": "orange", "font-size": ""},
                                "nav-link": {"font-size": "", "": "", "margin": "",
                                             "--hover-color": "#eee"},
                                "nav-link-selected": {"background-color": "green"},
                            })
st.write(
    # 1. as sidebasr menu
    selected3 = option_menu(None, ["Home", "Uploads"],
                            icons=['house', 'cloud-upload'],
                            menu_icon="cast", default_index=0, orientation="horizontal",
                            styles={
                                "container": {"": "", "background-color": "#fafafa"},
                                "icon": {"color": "orange", "font-size": ""},
                                "nav-link": {"font-size": "", "": "", "margin": "",
                                             "--hover-color": "#eee"},
                                "nav-link-selected": {"background-color": "black"},
                            }))
#  Preparing streamlit app page.
st.title('Dataset Collection')
st.subheader('Datasets are collected and stored and classified in Google Cloud Platform via this application for ML Training')
#  Preparing Uploader for datasets or files.
files = st.file_uploader('Upload Your Data',type=['csv', 'xlsx', 'png', 'jpeg', 'jpg' ,'gif', 'docx','pdf', 'zip', 'rar', 'folder'],accept_multiple_files=True)
for file in files:
 if file.type=='text/csv':
     df = pd.read_csv(file, encoding="utf8")
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
     st.success("Nice!! Your file(s)  has been uploaded successfully to cloud")
