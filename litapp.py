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
foodlist = ["fart","chicken","poopp","bunger","Fungus"]

def sign_in(username, password):
    if len(username) > 3 and len(password) > 3:
        st.sidebar.success(f'Done, signed in as "{username}"')
        return True
    else:
        st.sidebar.warning("Please enter a valid username and password.")
        return False

# Sign-in Sidebar
username = st.sidebar.text_input("Username")
password = st.sidebar.text_input("Password", type="password")

if st.sidebar.button("Sign In"):
    signed_in = sign_in(username, password)

# Voting
if signed_in:
    st.header('Voting')
    foodlist = ["fart", "chicken", "shart"]
    itempoints = [0] * len(foodlist)

    Voted = False

    for i, food in enumerate(foodlist):
        if not Voted:
            if st.button(f'Vote for {food}'):
                itempoints[i] += 1
                st.bar_chart({food: points for food, points in zip(foodlist, itempoints)})
                Voted = True
                st.info('Successfully Voted.')
        else:
            st.warning('Already Voted Bozo')
    if Voted:
        # Comments
        st.header('Comments')
        with st.container():
            prompt = st.text_input("Say something")
            if prompt:
                messages = st.container()
                messages.markdown(f'{username}: {prompt}', unsafe_allow_html=True)
else:
    st.warning("Sign in to continue..")