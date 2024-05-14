import streamlit as st

if 'signincounter' not in st.session_state:
    st.session_state.signincounter = 0
if 'votedcounter' not in st.session_state:
    st.session_state.votedcounter = 0
if 'Voted' not in st.session_state:
    st.session_state.Voted = False
if 'signed_in' not in st.session_state:
    st.session_state.signed_in = False

st.title("Voting App")
if not st.session_state.signed_in:
    st.write("##### --- sign in to continue --- ")

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
    foodlist = ["fart", "chicken", "poopp", "bunger", "Fungus","Mold","Starvation"]
    for i in foodlist:
        button = st.button(f'Vote for "{i}"')
        if button:
            st.toast(f'Press Again to vote for {i}')
            st.session_state.votedcounter += 1
            if votedcounter == 1:
                st.session_state.Voted = True

# Comments
if st.session_state.Voted and st.session_state.signed_in:
    st.toast(f'Voted for {i}')
    st.header('Comments')
    prompt = st.text_input("Say something")
    if prompt:
        st.markdown(f'{username}: {prompt}', unsafe_allow_html=True)
else:
    st.sidebar.warning("Sign in to continue.")
