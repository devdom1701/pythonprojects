import streamlit as st
username = "Fart"
#--------- variables ----------
item1 = 'Chicken'
item1points = 0
item2 = 'Phart'
item2points = 0
item3 = 'Rahhh'
item3points = 0
Voted = False

messagelog = []

tab1, tab2 = st.tabs(["Voting","Comment"])
#--------- main code ----------
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
        col1, col2, col3 = st.columns(3)
        col1.metric('Item One', f'{item1}', f'{item1points}')
        col2.metric('Item Two', f'{item2}', f'{item2points}')
        col3.metric('Item Three', f'{item3}', f'{item3points}')

with tab2:
    st.header('Comments')
    with st.container():
        messages = st.container(height=300)
        prompt = st.text_input("Say something")
        if prompt:
            if messagelog: 
                combined_messages = "<br>".join(messagelog) + "<br>" + f'{username}: {prompt}'
            else:
                combined_messages = f'{username}: {prompt}'
            messages.markdown(combined_messages, unsafe_allow_html=True)
            messagelog.append(f'{username}: {prompt}')
        else:
            combined_messages = "<br>".join(messagelog)
            messages.markdown(combined_messages, unsafe_allow_html=True)