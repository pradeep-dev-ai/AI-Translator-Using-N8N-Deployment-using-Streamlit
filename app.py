import streamlit as st
import requests
st.title("AI Translator App")
text=st.text_area("Enter the Sentence")
if st.button("Telugu"):
    if text:
        response=requests.post(url="https://prade1-23.app.n8n.cloud/webhook-test/7f63aead-efde-42f8-b5a9-9cdc3bc4eb11",json={"input":text,"language":"Telugu"})
        if response.status_code==200:
            st.write(response.json()['output'])
elif st.button("Hindi"):
    if text:
        response=requests.post(url="https://prade1-23.app.n8n.cloud/webhook-test/7f63aead-efde-42f8-b5a9-9cdc3bc4eb11",json={"input":text,"language":"Hindi"})
        if response.status_code==200:
            st.write(response.json()['output'])


else:
    pass