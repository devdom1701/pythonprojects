import streamlit as st
from datetime import datetime

if 'signincounter' not in st.session_state:
    st.session_state.signincounter = 0
if 'votedcounter' not in st.session_state:
    st.session_state.votedcounter = 0
if 'Voted' not in st.session_state:
    st.session_state.Voted = False
if 'signed_in' not in st.session_state:
    st.session_state.signed_in = False
if 'votes' not in st.session_state:
    st.session_state.votes = {food: 0 for food in ["fart", "chicken", "poopp", "bunger", "Fungus", "Mold", "Starvation"]}

st.title("Voting for Food App")

# Function to sign in
def sign_in(username, password):
    if len(username) > 3 and len(password) > 3:
        st.sidebar.success(f'Done, signed in as "{username}"')
        st.toast("Signed In")
        st.session_state.signed_in = True
        st.session_state.signincounter += 1
    else:
        st.sidebar.warning("Please enter a valid username and password.")

username = st.sidebar.text_input("Username")
password = st.sidebar.text_input("Password", type="password")

if st.sidebar.button("Sign In"):
    sign_in(username, password)

# Voting
if st.session_state.signed_in and not st.session_state.Voted:
    st.header('Voting')
    for food in ["fart", "chicken", "poopp", "bunger", "Fungus", "Mold", "Starvation"]:
        button = st.button(f'Vote for "{food}"')
        if button:
            st.toast(f'Press Again to vote for {food}')
            st.session_state.votedcounter += 1
            st.session_state.votes[food] += 1
            st.session_state.Voted = True

# Comments
if st.session_state.Voted and st.session_state.signed_in:
    st.header('Comments')
    prompt = st.text_input("Say something")
    if prompt:
        timestamp = datetime.now().strftime("%Y/%m/%d %H:%M")
        st.markdown(f'{username}, At [{timestamp}]: {prompt}', unsafe_allow_html=True)
elif not st.session_state.signed_in:
    st.sidebar.warning("Sign in to continue.")

if st.session_state.Voted and st.session_state.signed_in:
    st.header('Voting Results')
    st.bar_chart(st.session_state.votes)