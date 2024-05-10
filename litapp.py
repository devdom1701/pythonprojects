import streamlit as st

item1 = "chicken"
item1points = 0
item2 = "phart"
item2points = 0
item3 = "Rahhh"
item3points = 0
Voted = False

foodselection = st.radio(
    "Today's Lunch",
    [f':rainbow: {item1}', f"***{item2}***", f'{item3} :movie_camera:'],
    format_func=lambda x: f"{item1}" if x == f':rainbow: {item1}' else f"{item2}" if x == f"***{item2}***" else f"{item3}")
while not Voted:
    if foodselection == f':rainbow: {item1}':
        if st.button("Vote"):
            item1points += 1
            Voted = True
    elif foodselection == f"***{item2}***":
        if st.button("Vote"):
            item2points += 1
            Voted = True
    elif foodselection == f'{item3} :movie_camera:':
        if st.button("Vote"):
            item3points += 1
            Voted = True
if Voted:
    col1, col2, col3 = st.columns(3)
    col1.metric("Item One", f"{item1}", f"{item1points}")
    col2.metric("Item Two", f"{item2}", f"{item2points}")
    col3.metric("Item Three", f"{item3}", f"{item3points}")

with st.sidebar:
    messages = st.container(height=300)
    if prompt := st.chat_input("Say something"):
        messages.chat_message("user").write(prompt)




["Pizza", "Chicken Tenders", "Chicken Alfredo", "Bacon Cheeseburger", "Bosco Sticks", "Chicken Quesadilla", "Chicken Sandwich", "French Toast", "Pizza Crunchers", "General Tso's", "Walking Tacos", "Buffalo Chicken Pizza", "Chicken Fajita Bowl", "Popcorn Chicken Bowl", "Taco Tuesday", "Cheeseburger", "Pork Carnitas", "Pasta w/ Meat Sauce", "Loaded Potato Wedges", "Chicken Nuggets", "Grilled Cheese", "Brisket and Potato Bowl", "Chicken Strips", "Cheeseburger Waffle Fries", "Cheese Rippers", "BBQ Pork Sandwich", "Cheese Ravioli w/ Meat Sauce", "Chicken Carnita Bowl", "Philly Cheesesteak", "Ravioli", "Sweet and Sour Chicken", "Pepperoni Stuffed Breadstick", "Meatballs Subs", "Ceasar SSalad"]