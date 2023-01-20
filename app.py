from helper import curls, squats, pushups, crunches

import streamlit as st 


st.title("    Gym Assist")

st.header("Welcome to the Virtual Gym")
st.text("")
st.text("")
st.text("Currently we offer help with pushups, curls, squats and crunches.")
st.text("")
st.text("")
' **We advise you to use it in a well lit setting** '

# '_This_ is some **Markdown***'

st.text("")
st.text("")
st.text("")
option = st.selectbox("Which Excercise do you wish to practice? ", ['None','Curls', 'Pushups', 'Squats', 'Crunches'])
st.text("")
st.text("")
st.text("")




'How many reps do you aim for ?'

aim  = st.slider('x')


if(aim>0):
    if option == 'Curls' :
        curls(aim)
        st.balloons()
        st.success('Congrats on finishing your workout')


    if option == 'Pushups':
        pushups(aim)
        st.balloons()
        st.success('Congrats on finishing your workout')


    if option  == 'Squats':
        squats(aim)
        st.balloons()
        st.success('Congrats on finishing your workout')

    if option == 'Crunches':
        crunches(aim)
        st.balloons()
        st.success('Congrats on finishing your workout')


