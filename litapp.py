#______-Basic Layout-_______
# (headers, footers text)
import streamlit as st

item1 = "chicken"
item1points = 0
item2 = "phart"
item2points = 0
item3 = "Rahhh"
item3points = 0

foodselection = st.radio(
    "Today's Lunch",
    [f':rainbow[{item1}]', f"***{item2}***", f'{item3} :movie_camera:'],
    captions = ["Joke", "No.", "Test"])

if foodselection == f'{item1}':
    item1points += 1
elif foodselection == f'{item2}':
    item2points += 1
elif foodselection == f'{item3}':
    item3points += 1

col1, col2, col3 = st.columns(3)
col1.metric("Item One", f"{item1}", f"{item1points}")
col2.metric("Item Two", f"{item2}", f"{item2points}")
col3.metric("Item Three", f"{item3}", f"{item3points}")

#______-"Backend code"-_______
# (python code supporting the layout code)

