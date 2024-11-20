import streamlit as st
import datetime

st.write("""  # Application Form """)

with st.form("user form"):

    username = st.text_input("User Name:")
    #User age slider

    age=st.slider("Age",0,100,18)

    #Date of Birth
    dob=st.date_input("Date of Birth",datetime.date(1998,12,30))

    #User Gender
    gender = st.radio(
        "What's your gender ?",
        ["Male","Female"],
        index=None,
        )

  

    #toggle button
    enableuser = st.toggle("Activate User")
    profile_picture =st.file_uploader("Upload a datafile")
    #form submit button
    submitted = st.form_submit_button("Submit")

    if submitted:
        st.write("Username ",username,"age ",age,"dob",dob,"gender",gender,"activate user",enableuser)

      
