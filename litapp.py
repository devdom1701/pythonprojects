#______-Basic Layout-_______
# (headers, footers text)
import streamlit as st

item1 = "chicken"
item2 = "phart"
item3 = "Rahhh"


st.button("Reset", type="primary")
if st.button("Say hello"):
    st.write("Why hello there")
else:
    st.write("Goodbye")

genre = st.radio(
    "Today's Lunch",
    [f':rainbow[{item1}]', f"***{item2}***", f'{item3} :movie_camera:'],
    captions = ["Joke", "No.", "Test"])

if genre == ":rainbow[{item1}}]":
    st.write("thats gay.")
else:
    st.write("based.")

#______-"Backend code"-_______
# (python code supporting the layout code)

