import streamlit as st
import pandas as pd
import os

def save_uploadedfile(uploadedfile):
     with open(os.path.join("C:\\Users\\MY PC\\Downloads\\images", uploadedfile.name), "wb") as f:
         f.write(uploadedfile.getbuffer())

     return st.success("Saved File".format(uploadedfile.name))
st.subheader('Page 1')
uploaded_file = st.file_uploader("Add dataset (csv) ",type=['csv'])
if uploaded_file is not None:
    # file_details = {"FileName":uploaded_file.name,"FileType":uploaded_file.type}
    # st.write(file_details)
    # df = st.image(uploaded_file,  width= 250)
    df = pd.read_csv(uploaded_file)
    st.write(df)
    save_uploadedfile(uploaded_file)































#      with open(os.path("C:\\Users\\MY PC\\Downloads\\images", uploadedfile.name), "wb") as f:
#       f.write(uploadedfile.getbuffer())
#      return st.success("Saved File".format(uploadedfile.name))
#
#
# st.subheader('Page 1')
# uploaded_file = st.file_uploader("Add dataset",type=['png','jpg','gif'])
# if uploaded_file is not None:
#     file_details = {"FileName":uploaded_file.name,"FileType":uploaded_file.type}
#     st.write(file_details)
#     df = st.image(uploaded_file, width= 250)
# save_uploadedfile(uploaded_file)


# file_details = {"FileName":uploaded_file.name,"FileType":uploaded_file.type}
    # st.write(file_details)

# def save_uploadedfile(uploadedfile):
#     with open(os.path.join("Data", uploadedfile.name), "wb") as f:
#         f.write(uploadedfile.getbuffer())
#     return st.success("Saved File:{}to Data".format(uploadedfile.name))
#     st.title("PDF File upload")
#     st.text("Asimple way directory")
#     uploadedfiles = st.file_uploader("Upload PDF", type = ['pdf'], accept_multiple_files = True)
#     for file in uploadedfiles:
#         if uploadedfiles is not None:
#             save_uploadedfile(file)
