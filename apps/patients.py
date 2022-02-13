import streamlit as st
from . import login,db

def app():
    logged_in_as_doctor,logged_in_as_patient,username = login.app()
    pending=False
    if logged_in_as_doctor:
        patientname = db.get_patientname(username)
        if patientname=="***":
            st.header("You have no appointments yet")
        else:
            pending=True
            st.header("You have an appointment with {}".format(patientname))
            
    elif logged_in_as_doctor:
        st.warning("You are not logged in as a doctor!")
    else:
        st.warning("Please login as a doctor to access this page!")

    if pending:
        # ----------------------------------------------
        st.subheader("Schedule a meeting here..")
        date = st.text_input("Date:")
        time = st.text_input("Time:")
        if st.button("Schedule"):
            db.create_appointmenttable()
            db.add_appointment(username,patientname,date,time)
            st.subheader("Appointment scheduled with {} at date: {} ,time: {}".format(patientname,date,time))
        # -----------------------------------------------