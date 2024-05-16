import streamlit as st
import random
from datetime import datetime

class VotingOption:
    def __init__(self, name):
        self.name = name
        self.votes = 0

    def vote(self):
        self.votes += 1

food_list2 = ["Pizza", "Chicken Tenders", "Chicken Alfredo", "Bacon Cheeseburger", "Bosco Sticks", "Chicken Quesadilla", "Chicken Sandwich", "French Toast", "Pizza Crunchers", "General Tso's", "Walking Tacos", "Buffalo Chicken Pizza", "Chicken Fajita Bowl", "Popcorn Chicken Bowl", "Taco Tuesday", "Cheeseburger", "Pork Carnitas", "Pasta w/ Meat Sauce", "Loaded Potato Wedges", "Chicken Nuggets", "Grilled Cheese", "Brisket and Potato Bowl", "Chicken Strips", "Cheeseburger Waffle Fries", "Cheese Rippers", "BBQ Pork Sandwich", "Cheese Ravioli w/ Meat Sauce", "Chicken Carnita Bowl", "Philly Cheesesteak", "Ravioli", "Sweet and Sour Chicken", "Pepperoni Stuffed Breadstick", "Meatballs Subs","slop","Crabby Paddi"]
pick = random.food_list2
if pick == True:
    st.session_state.voting_options.append(pick)
    
if 'signincounter' not in st.session_state:
    st.session_state.signincounter = 0
if 'votedcounter' not in st.session_state:
    st.session_state.votedcounter = 0
if 'Voted' not in st.session_state:
    st.session_state.Voted = False
if 'notcommented' not in st.session_state:
    st.session_state.notcommented = True
if 'signed_in' not in st.session_state:
    st.session_state.signed_in = False
if 'voting_options' not in st.session_state:
    st.session_state.voting_options = [VotingOption(name) for name in ["fart", "chicken", "poopp", "bunger", "Fungus", "Mold", "Starvation","Rat Burg","Air(Personal Favorite)","Ice and Milk"]]
if 'messages' not in st.session_state:
    st.session_state.messages = {}

if not st.session_state.Voted:
    st.title("Voting for Food App")

# Function to sign in
def sign_in(username, password):
    if len(username) > 3 and len(password) > 3:
        st.sidebar.success(f'Done, signed in as "{username}"')
        st.toast("Signed In")
        st.session_state.signed_in = True
        st.session_state.signincounter += 1
        if username not in st.session_state.messages:
            st.session_state.messages[username] = []
    else:
        st.sidebar.warning("Please enter a valid username and password.")

if not st.session_state.Voted:
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
            st.session_state.votedcounter += 1
            option.vote()
            st.session_state.Voted = True

# Comments
if st.session_state.Voted and st.session_state.signed_in:
    st.header('Comments')
    if st.session_state.notcommented:
        st.info("Comment something!")
    prompt = st.text_input("Say something")
    if prompt:
        timestamp = datetime.now().strftime("%H:%M")
        st.session_state.messages[username].append(f'{username} , at {timestamp}: {prompt}')

    for msg in st.session_state.messages[username]:
        st.markdown(msg, unsafe_allow_html=True)
        st.session_state.notcommented = False
elif not st.session_state.signed_in:
    st.sidebar.warning("Sign in to continue.")

if st.session_state.Voted and st.session_state.signed_in:
    st.header('Voting Results')
    votes_dict = {option.name: option.votes for option in st.session_state.voting_options}
    st.bar_chart(votes_dict)