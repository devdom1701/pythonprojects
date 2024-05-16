import streamlit as st
import random
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Database configuration
DATABASE_URL = "mssql+pymssql://sa:dockerStrongPwd123@PhartSQL:1433/sa"
Base = declarative_base()

# Define the Comment model
class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False)
    timestamp = Column(String(50), nullable=False)
    message = Column(Text, nullable=False)

# Set up the database
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

# Create the comments table if it doesn't exist
Base.metadata.create_all(engine)

class VotingOption:
    def __init__(self, name):
        self.name = name
        self.votes = 0

    def vote(self):
        self.votes += 1

food_list2 = ["Pizza", "Chicken Tenders", "Chicken Alfredo", "Bacon Cheeseburger", "Bosco Sticks", "Chicken Quesadilla", "Chicken Sandwich", "French Toast", "Pizza Crunchers", "General Tso's", "Walking Tacos", "Buffalo Chicken Pizza", "Chicken Fajita Bowl", "Popcorn Chicken Bowl", "Taco Tuesday", "Cheeseburger", "Pork Carnitas", "Pasta w/ Meat Sauce", "Loaded Potato Wedges", "Chicken Nuggets", "Grilled Cheese", "Brisket and Potato Bowl", "Chicken Strips", "Cheeseburger Waffle Fries", "Cheese Rippers", "BBQ Pork Sandwich", "Cheese Ravioli w/ Meat Sauce", "Chicken Carnita Bowl", "Philly Cheesesteak", "Ravioli", "Sweet and Sour Chicken", "Pepperoni Stuffed Breadstick", "Meatballs Subs","slop","Crabby Paddi"]

# Randomly select choices from the food list
choice = food_list2[random.randint(0, len(food_list2) - 1)]
choice2 = food_list2[random.randint(0, len(food_list2) - 1)]
choice3 = food_list2[random.randint(0, len(food_list2) - 1)]

randomchoicelist = [choice, choice2, choice3]

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
    st.session_state.voting_options = [VotingOption(name) for name in randomchoicelist]

if not st.session_state.Voted:
    st.title("Voting for Food App")

# Function to sign in
def sign_in(username, password):
    if len(username) > 3 and len(password) > 3:
        st.sidebar.success(f'Done, signed in as "{username}"')
        st.toast("Signed In")
        st.session_state.signed_in = True
        st.session_state.signincounter += 1
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
        new_comment = Comment(username=username, timestamp=timestamp, message=prompt)
        session.add(new_comment)
        session.commit()
        st.session_state.notcommented = False

    comments = session.query(Comment).filter_by(username=username).all()
    for comment in comments:
        st.markdown(f'{comment.username}, at {comment.timestamp}: {comment.message}', unsafe_allow_html=True)
elif not st.session_state.signed_in:
    st.sidebar.warning("Sign in to continue.")

if st.session_state.Voted and st.session_state.signed_in:
    st.header('Voting Results')
    votes_dict = {option.name: option.votes for option in st.session_state.voting_options}
    st.bar_chart(votes_dict)