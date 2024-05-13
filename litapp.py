import streamlit as st
import time
st.title("Voting Rahhh App")

username = "Fart"
item1 = 'Chicken'
item1points = 0
item2 = 'Phart'
item2points = 0
item3 = 'Rahhh'
item3points = 0
Voted = False
signed_in = False

tab1, tab2 = st.columns(2)
messagelog = []
#_____ Sign-in Sidebar _____
username = st.sidebar.text_input("Username")
password = st.sidebar.text_input("Password", type="password")

if st.sidebar.button("Sign In"):
    if len(username and password) > 3:
        signed_in = True
    else:
        st.sidebar.text("")
    if not signed_in:
        st.sidebar.title("Not signed in Brotha")
    elif signed_in:
        with st.sidebar:
            with st.spinner('Loading...'):
                time.sleep(1)
                st.sidebar.success(f'Done, signed in as "{username}"')
                st.balloons

#_____Voting____
with tab1:
    st.header('Voting')
    foodselection = st.radio(
        "Today's Lunch",
        [f'{item1}', f'{item2}', f'{item3}'],
        format_func=lambda x: f'{item1}' if x == f'{item1}' else f'{item2}' if x == f'{item2}' else f'{item3}'
    )
    if not Voted:
        if foodselection == f'{item1}':
            if st.button('Vote'):
                item1points += 1
                Voted = True
        elif foodselection == f'{item2}':
            if st.button('Vote'):
                item2points += 1
                Voted = True
        elif foodselection == f'{item3}':
            if st.button('Vote'):
                item3points += 1
                Voted = True

    if Voted:
        st.bar_chart({f'{item1}': item1points, f'{item2}': item2points, f'{item3}': item3points})

with tab2:
    st.header('Comments')
    with st.container():
        prompt = st.text_input("Say something")
        if prompt:
            messages = st.container()
            messages.markdown(f'{username}: {prompt}', unsafe_allow_html=True)
        else:
            for message in messagelog:
                st.container().markdown(f'{message}', unsafe_allow_html=True)
