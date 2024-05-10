#______-Basic Layout-_______
# (headers, footers text)
import streamlit as st

st.button("Reset", type="primary")
if st.button("Say hello"):
    st.write("Why hello there")
else:
    st.write("Goodbye")

genre = st.radio(
    "What's your favorite movie genre",
    [":rainbow[gay]", "***testing***", "Documentary :movie_camera:"],
    captions = ["Joke", "No.", "Test"])

if genre == ":rainbow[gay]":
    st.write("You selected gay.")
else:
    st.write("You didn't select gay.")

#______-"Backend code"-_______
# (python code supporting the layout code)

