import streamlit as st
import random
from datetime import datetime

class VotingOption:
    def __init__(self, name, image, description):
        self.name = name
        self.image = image
        self.description = description
        self.votes = 0

    def vote(self):
        self.votes += 1

# Dictionary for images and descriptions
food_details = {
    "Pizza": {"image": "https://i.imgur.com/4AiIiq3.gif", "description": "Cheese or peppaoni pizza"},
    "Chicken Tenders": {"image": "https://i.imgur.com/4AiIiq3.gif", "description": "Chicken tenders"},
    "Chicken Alfredo": {"image": "https://i.imgur.com/4AiIiq3.gif", "description": "Pasta with alfredo sauce and chicken"},
    "Bacon Cheeseburger": {"image": "https://i.imgur.com/4AiIiq3.gif", "description": "A cheeseburger with bacon on it"},
    "Bosco Sticks": {"image": "https://i.imgur.com/4AiIiq3.gif", "description": "Sticks with cheese"},
    "Chicken Quesadilla": {"image": "https://i.imgur.com/4AiIiq3.gif", "description": "Quesadilla but chicken"},
    "Chicken Sandwich": {"image": "https://i.imgur.com/4AiIiq3.gif", "description": "Checken inbtweem sum buns"},
    "French Toast": {"image": "https://i.imgur.com/4AiIiq3.gif", "description": "French but toast flavored"},
    "Pizza Crunchers": {"image": "https://i.imgur.com/4AiIiq3.gif", "description": "Pizza but crunchy"},
    "General Tso's": {"image": "https://i.imgur.com/4AiIiq3.gif", "description": "Chicken or something"},
    "Walking Tacos": {"image": "https://i.imgur.com/4AiIiq3.gif", "description": "Taco but it walks"},
    "Buffalo Chicken Pizza": {"image": "https://i.imgur.com/4AiIiq3.gif", "description": "Pizza but with buffalos on it"},
    "Chicken Fajita Bowl": {"image": "https://i.imgur.com/4AiIiq3.gif", "description": "Chicken in a bowl"},
    "Popcorn Chicken Bowl": {"image": "https://i.imgur.com/4AiIiq3.gif", "description": "Popcorn version of chicken in a bowl"},
    "Cheeseburger": {"image": "https://i.imgur.com/4AiIiq3.gif", "description": "ChesBurger"},
    "Pork Carnitas": {"image": "https://i.imgur.com/4AiIiq3.gif", "description": "Pork Carnitas, thats just the description you're good."},
    "Pasta w/ Meat Sauce": {"image": "https://i.imgur.com/4AiIiq3.gif", "description": "Pasta with cool sauce on it."},
    "Loaded Potato Wedges": {"image": "https://i.imgur.com/4AiIiq3.gif", "description": "Loaded Potato wedges, Thats it."},
    "Chicken Nuggets": {"image": "https://i.imgur.com/4AiIiq3.gif", "description": "Chicken with nuggies."},
    "Grilled Cheese": {"image": "https://i.imgur.com/4AiIiq3.gif", "description": "Cheese but on the grill"},
    "Brisket and Potato Bowl": {"image": "https://i.imgur.com/4AiIiq3.gif", "description": "Caleb"},
    "Chicken Strips": {"image": "https://i.imgur.com/4AiIiq3.gif", "description": "Caleb"},
    "Cheeseburger Waffle Fries": {"image": "https://i.imgur.com/4AiIiq3.gif", "description": "Caleb"},
    "Cheese Rippers": {"image": "https://i.imgur.com/4AiIiq3.gif", "description": "Caleb"},
    "BBQ Pork Sandwich": {"image": "https://i.imgur.com/4AiIiq3.gif", "description": "Caleb"},
    "Cheese Ravioli w/ Meat Sauce": {"image": "https://i.imgur.com/4AiIiq3.gif", "description": "Caleb"},
    "Philly Cheesesteak": {"image": "https://i.imgur.com/4AiIiq3.gif", "description": "Caleb"},
    "Ravioli": {"image": "https://i.imgur.com/4AiIiq3.gif", "description": "Caleb"},
    "Sweet and Sour Chicken": {"image": "https://i.imgur.com/4AiIiq3.gif", "description": "Caleb"},
    "Pepperoni Stuffed Breadsticks": {"image": "https://i.imgur.com/4AiIiq3.gif", "description": "Caleb"},
    "Meatball Subs": {"image": "https://i.imgur.com/4AiIiq3.gif", "description": "Caleb"},
    "Slop": {"image": "https://i.imgur.com/4AiIiq3.gif", "description": "Caleb"},
}

food_list2 = ["Pizza", "Chicken Tenders", "Chicken Alfredo", "Bacon Cheeseburger", "Bosco Sticks", "Chicken Quesadilla", 
              "Chicken Sandwich", "French Toast", "Pizza Crunchers", "General Tso's", "Walking Tacos", "Buffalo Chicken Pizza", 
              "Chicken Fajita Bowl", "Popcorn Chicken Bowl", "Cheeseburger", "Pork Carnitas", "Pasta w/ Meat Sauce", 
              "Loaded Potato Wedges", "Chicken Nuggets", "Grilled Cheese", "Brisket and Potato Bowl", "Chicken Strips", 
              "Cheeseburger Waffle Fries", "Cheese Rippers", "BBQ Pork Sandwich", "Cheese Ravioli w/ Meat Sauce", 
             "Philly Cheesesteak", "Ravioli", "Sweet and Sour Chicken", "Pepperoni Stuffed Breadstick", 
              "Meatballs Subs"]

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
    st.session_state.voting_options = [
        VotingOption(name, food_details[name]['image'], food_details[name]['description']) 
        for name in food_list2 if name in food_details
    ]
if 'messages' not in st.session_state:
    st.session_state.messages = {}
if 'random_options' not in st.session_state:
    st.session_state.random_options = random.sample(st.session_state.voting_options, 3)

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

username = st.sidebar.text_input("Username")
password = st.sidebar.text_input("Password", type="password")

if st.sidebar.button("Sign In"):
    sign_in(username, password)

# Voting
if st.session_state.signed_in and not st.session_state.Voted:
    st.header('Voting')
    for option in st.session_state.random_options:
        with st.expander(f"{option.name}"):
            st.image(option.image, caption=option.name)
            st.write(option.description)
            if st.button(f'Vote for "{option.name}"'):
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
