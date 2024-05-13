import streamlit as st
import time

st.title("Voting Rahhh App")

itemnumba = 0

item1points = 0
item2points = 0
item3points = 0

Voted = False
signed_in = False
notsignedin = True

messagelog = []
passwordlist = []
usernamelist = []
usernamelistcounter = 0

foodlist = ["fart", "chicken", "poopp", "bunger", "Fungus"]

# Sign-in Sidebar
if notsignedin and not Voted:
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")

def sign_in(username, password):
    global usernamelistcounter, notsignedin
    if len(username) > 3 and len(password) > 3:
        st.sidebar.success(f'Done, signed in as "{username}"')
        usernamelist.append(f"{username}")
        passwordlist.append(f"{password}")
        usernamelistcounter += 1
        notsignedin = False
    else:
        st.sidebar.warning("Please enter a valid username and password.")

if st.sidebar.button("Sign In") and notsignedin and not Voted:
    signed_in = sign_in(username, password)

# Voting
if signed_in and not Voted:
    st.header('Voting')
    itempoints = [0] * len(foodlist)

    for i, food in enumerate(foodlist):
        if st.button(f'Vote for {food}'):
            itempoints[i] += 1
            st.toast('Successfully Voted.')
            Voted = True
            break

# Comments Section
if Voted:
    st.sidebar.header('Comments')
    with st.sidebar.container():
        prompt = st.sidebar.text_input("Say something")
        if prompt:
            messages = st.sidebar.container()
            messages.markdown(f'{usernamelist[usernamelistcounter - 1]}: {prompt}', unsafe_allow_html=True)
else:
    if signed_in:
        st.sidebar.warning("Vote to unlock the comment section..")
