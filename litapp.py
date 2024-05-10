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
if not Voted:
    if foodselection == f':rainbow: {item1}':
        if st.button("Vote"):
            item1points += 1
    elif foodselection == f"***{item2}***":
        if st.button("Vote"):
            item2points += 1
    elif foodselection == f'{item3} :movie_camera:':
        if st.button("Vote"):
            item3points += 1
if Voted:
    col1, col2, col3 = st.columns(3)
    col1.metric("Item One", f"{item1}", f"{item1points}")
    col2.metric("Item Two", f"{item2}", f"{item2points}")
    col3.metric("Item Three", f"{item3}", f"{item3points}")
