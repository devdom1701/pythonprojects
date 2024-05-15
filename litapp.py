import streamlit as st
from datetime import datetime

class VotingOption:
    def __init__(self, name):
        self.name = name
        self.votes = 0

    def vote(self):
        self.votes += 1

if 'signincounter' not in st.session_state:
    st.session_state.signincounter = 0
if 'votedcounter' not in st.session_state:
    st.session_state.votedcounter = 0
if 'Voted' not in st.session_state:
    st.session_state.Voted = False
if 'signed_in' not in st.session_state:
    st.session_state.signed_in = False
if 'voting_options' not in st.session_state:
    st.session_state.voting_options = [VotingOption(name) for name in ["fart", "chicken", "poopp", "bunger", "Fungus", "Mold", "Starvation"]]

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
    for option in st.session_state.voting_options:
        button = st.button(f'Vote for "{option.name}"')
        if button:
            st.toast(f'Press Again to vote for {option.name}')
            st.session_state.votedcounter += 1
            option.vote()
            st.session_state.Voted = True
            votes_dict = {option.name: option.votes for option in st.session_state.voting_options}
            comments = st.text_input("Say something")
            popup_content = f"""
                # Voting Results
                {votes_dict}
                # Comments
                {username} , at {datetime.now().strftime("%H:%M")}: {comments}
            """
            st.popup(popup_content, title="Vote Summary")

# Comments
if st.session_state.Voted and st.session_state.signed_in:
    st.header('Comments')
    prompt = st.text_input("Say something")
    if prompt:
        timestamp = datetime.now().strftime("%H:%M")
        st.markdown(f'{username} , at {timestamp}: {prompt}', unsafe_allow_html=True)
elif not st.session_state.signed_in:
    st.sidebar.warning("Sign in to continue.")