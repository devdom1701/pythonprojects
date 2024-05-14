import streamlit as st
import time

st.title("Voting ahhh App")

itemnumba = 0
itempoints = 0

Voted = False
signed_in = False
tab1, tab2 = st.columns(2)

messagelog = []
passwordlist = []
usernamelist = []
usernamelistcounter = 0

foodlist = ["fart", "chicken", "poopp", "bunger", "Fungus"]

# Sign-in Sidebar
username = st.sidebar.text_input("Username")
password = st.sidebar.text_input("Password", type="password")

# Data storage
users = {}

# Function to sign in
def sign_in(username, password):
    if len(username) > 3 and len(password) > 3:
        st.sidebar.success(f'Done, signed in as "{username}"')
        users[username] = {'password': password, 'Voted': False}
        return True
    else:
        st.sidebar.warning("Please enter a valid username and password.")
        return False

# Sign in
if st.sidebar.button("Sign In"):
    signed_in = sign_in(username, password)

# Voting
if signed_in:
    st.header('Voting')
    foodlist = ["fart", "chicken", "poopp", "bunger", "Fungus"]
    votes = [0] * len(foodlist)
    for i, food in enumerate(foodlist):
        if st.button(f'Vote for {food}'):
            votes[i] += 1
            st.bar_chart({food: votes[i] for i, food in enumerate(foodlist)})
            st.success('Successfully Voted.')
            users[username]['Voted'] = True
            break
    if not any(user['Voted'] for user in users.values()):
        st.warning("Vote to unlock the comment section.")
else:
    st.sidebar.warning("Sign in to continue.")

# Comments
if not signed_in and users[username]['Voted']:
    st.header('Comments')
    prompt = st.text_input("Say something")
    if prompt:
        st.markdown(f'{username}: {prompt}', unsafe_allow_html=True)
    else:
        st.warning("Type something to leave a comment.")