import streamlit as st
import time

st.title("Voting Rahhh App")

itemnumba = 0

item1points = 0
item2points = 0
item3points = 0

Voted = False
signed_in = False
notsignedin = False

messagelog = []
passwordlist = []
usernamelist = []
usernamelistcounter = 0

foodlist = ["fart", "chicken", "poopp", "bunger", "Fungus"]

# Sign-in Sidebar
if not notsignedin:
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")

def sign_in(username, password):
    global usernamelistcounter, notsignedin
    if len(username) > 3 and len(password) > 3:
        st.sidebar.success(f'Done, signed in as "{username}"')
        usernamelist.append(f"{username}")
        passwordlist.append(f"{password}")
        usernamelistcounter += 1
        notsignedin = True
        return True
    else:
        st.sidebar.warning("Please enter a valid username and password.")
        return False

if st.sidebar.button("Sign In") and not notsignedin:
    signed_in = sign_in(username, password)

# Voting
if signed_in:
    st.header('Voting')
    itempoints = [0] * len(foodlist)

    if not Voted:
        for i, food in enumerate(foodlist):
            if st.button(f'Vote for {food}'):
                itempoints[i] += 1
                st.bar_chart({food: itempoints[i] for i, food in enumerate(foodlist)})
                st.toast('Successfully Voted.')
                Voted = True
                break
    else:
        st.warning('Already Voted Bozo')

if not Voted:
    if signed_in:
        st.warning("Vote to unlock the comment section..")
    elif Voted:
        st.header('Comments')
        with st.container():
            prompt = st.text_input("Say something")
            if prompt:
                messages = st.container()
                messages.markdown(f'{usernamelist[usernamelistcounter - 1]}: {prompt}', unsafe_allow_html=True)