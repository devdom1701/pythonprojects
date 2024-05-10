#______-Basic Layout-_______
# (headers, footers text)
import streamlit as st

st.button("Reset", type="primary")
if st.button("Say hello"):
    st.write("Why hello there")
else:
    st.write("Goodbye")


#______-"Backend code"-_______
# (python code supporting the layout code)

