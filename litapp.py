import streamlit as st

if 'signincounter' not in st.session_state:
    st.session_state.signincounter = 0
if 'votedcounter' not in st.session_state:
    st.session_state.votedcounter = 0
if 'Voted' not in st.session_state:
    st.session_state.Voted = False
if 'signed_in' not in st.session_state:
    st.session_state.signed_in = False

st.title("Voting Ahhh App")

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
if st.session_state.signed_in and st.session_state.votedcounter == 0:
    st.header('Voting')
    foodlist = ["fart", "chicken", "poopp", "bunger", "Fungus","Mold","Starvation"]
    for i in foodlist:
        button = st.button(f'Vote for {i}')
        if button:
            st.toast(f'Successfully Voted for {i}')
            st.session_state.votedcounter += 1
            st.session_state.Voted = True
            st.wirte(f'+1 Vote')

# Comments
if st.session_state.Voted and st.session_state.signed_in:
    st.header('Comments')
    prompt = st.text_input("Say something")
    if prompt:
        st.markdown(f'{username}: {prompt}', unsafe_allow_html=True)
else:
    st.sidebar.warning("Sign in to continue.")
