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
foodlist = ["fart","chicken","shart"]

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
                Voted = True
                st.info('Successfully Voted.')
        else:
            st.warning('Already Voted Bozo')

    st.bar_chart({food: points for food, points in zip(foodlist, itempoints)})

# Comments
st.header('Comments')
with st.container():
    prompt = st.text_input("Say something")
    if prompt:
        messages = st.container()
        messages.markdown(f'{username}: {prompt}', unsafe_allow_html=True)
    else:
        st.warning("Type something to leave a comment.")





































# import streamlit as st
# import time

# st.title("Voting Rahhh App")

# itemnumba = 0

# item1points = 0
# item2points = 0
# item3points = 0

# Voted = False
# signed_in = False
# notsignedin = False

# messagelog = []
# passwordlist = []
# usernamelist = []
# usernamelistcounter = 0

# foodlist = ["fart", "chicken", "poopp", "bunger", "Fungus"]

# # Sign-in Sidebar
# if not notsignedin:
#     username = st.sidebar.text_input("Username")
#     password = st.sidebar.text_input("Password", type="password")

# def sign_in(username, password):
#     global usernamelistcounter, notsignedin
#     if len(username) > 3 and len(password) > 3:
#         st.sidebar.success(f'Done, signed in as "{username}"')
#         usernamelist.append(f"{username}")
#         passwordlist.append(f"{password}")
#         usernamelistcounter += 1
#         notsignedin = True
#         return True
#     else:
#         st.sidebar.warning("Please enter a valid username and password.")
#         return False

# if st.sidebar.button("Sign In") and not notsignedin:
#     signed_in = sign_in(username, password)

# # Voting
# if signed_in:
#     st.header('Voting')
#     itempoints = [0] * len(foodlist)

#     if not Voted:
#         for i, food in enumerate(foodlist):
#             if st.button(f'Vote for {food}'):
#                 itempoints[i] += 1
#                 st.toast('Successfully Voted.')
#                 Voted = True
#                 break
#     else:
#         st.warning('Already Voted Bozo')

# st.sidebar.header('Comments')
# with st.sidebar:
#     message_history = []
#     prompt = st.text_input("Say something")
#     if prompt:
#         message_history.append((username, prompt))
#     for username, message in message_history:
#         st.chat_message(f"{username}: {message}")