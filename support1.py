import streamlit as st
from PIL import Image
import requests
import json

url = "https://paperclips.atlassian.net/rest/api/2/issue"

username = "alisaboundji2003@gmail.com"
api_token = "ATATT3xFfGF0nbbrUOhCsrl5eIuELJHtlXLMW5UaEGdzzg83e7i6qKQTIvIB62Yt8VmUDbupVAhcnYClxJxkYeFFIoELLi_oqIBWp0yJNzvCLWix_lBJ4wwVqnkMDEn3Dr1efwIBU-LnneSopD7CS2inaeuIrGdh45_PpEmFlBipyt_shO3NpLY=0F77ABC0"

# Set up the request headers
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

# Issue data in JSON format





image=Image.open("Original on Transparent.png")
#image=image.resize((180,100))
st.image(image)

first_name=st.text_input("First name:")
last_name=st.text_input("Last Name:")
email=st.text_input("Email address:")
issue=st.text_input("Issue:")
desc = st.text_area("Type your issue here:", height=200)
col0,col1,col2,col3,col4,col5,col6=st.columns(7)
sending=col3.button("Send")
if sending :
  issue_data = {
    "fields": {
       "project":
       {
          "key": "AL"
       },
       "summary": issue,
       "description": f"First name:{first_name}\nLast name:{last_name}\nEmail:{email}\ndescription:{desc}",
       "issuetype": {
          "id": "10003"
       }
      }
    }
# Make the POST request
  response = requests.post(
      url,
      headers=headers,
      auth=(username, api_token),
      data=json.dumps(issue_data)
  )
  st.success("Report sent to the developers,you will be contacted soon")
