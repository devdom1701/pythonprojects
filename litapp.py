import streamlit as st
import time

st.title("Voting ahhh App")

itemnumba = 0
itempoints = 0
signincounter = 0

Voted = False
if signincounter == 0:
    signed_in = False
else:
    signed_in = True

tab1, tab2 = st.columns(2)

messagelog = []
passwordlist = []
usernamelist = []
usernamelistcounter = 0

foodlist = ["fart", "chicken", "poopp", "bunger", "Fungus", "Monkey(Because why not)"]

# Sign-in Sidebar
username = st.sidebar.text_input("Username")
password = st.sidebar.text_input("Password", type="password")

# Data storage
users = {}

# Function to sign in
def sign_in(username, password):
    global signed_in, signincounter
    if len(username) > 3 and len(password) > 3:
        st.sidebar.success(f'Done, signed in as "{username}"')
        signed_in = True
        signincounter += 1
        users[username] = {'password': password}
    else:
        st.sidebar.warning("Please enter a valid username and password.")

# Sign in
if st.sidebar.button("Sign In"):
    signinfield = sign_in(username, password)

# Voting
if signed_in:
    st.header('Voting')
    votes = [0] * len(foodlist)
    for i, food in enumerate(foodlist):

        while st.button(f'Vote for {food}'):
            votes[i] += 1
            st.toast('Successfully Voted.')
            Voted = True
            st.title("Voted!!!")

    while Voted:
        st.title("Voted!!!")
        st.header('Comments')
        prompt = st.text_input("Say something")
        if prompt:
            st.markdown(f'{username}: {prompt}', unsafe_allow_html=True)
#else:
    #st.sidebar.warning("Sign in to continue.")
