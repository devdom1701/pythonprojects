import streamlit as st
import time

st.title("Voting Rahhh App")

itemnumba = 0

item1points = 0
item2points = 0
item3points = 0

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

def sign_in(username, password):
    global usernamelistcounter
    if len(username) > 3 and len(password) > 3:
        st.sidebar.success(f'Done, signed in as "{username}"')
        usernamelist.append(f"{username}")
        passwordlist.append(f"{password}")
        usernamelistcounter += 1
        return True
    else:
        st.sidebar.warning("Please enter a valid username and password.")
        return False

if st.sidebar.button("Sign In"):
    signed_in = sign_in(username, password)

# Voting
if signed_in:
    st.header('Voting')
    itempoints = [0] * len(foodlist)
    st.warning("Vote to unlock the comment section..")

    if not Voted:
        for i, food in enumerate(foodlist):
            if st.button(f'Vote for {food}'):
                itempoints[i] += 1
                st.bar_chart({food: itempoints[i] for i, food in enumerate(foodlist)})
                st.toast('Successfully Voted.')
                Voted = True
                break
    
if Voted:
    # Comments
    st.title('Comments')
    with st.container():
        prompt = st.text_input("Say something")
        if prompt:
            messages = st.container()
            messages.markdown(f'{usernamelist[usernamelistcounter - 1]}: {prompt}', unsafe_allow_html=True)
else:
    st.sidebar.warning("Sign in to continue..")
