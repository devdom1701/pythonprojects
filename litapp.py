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
    "Pizza": {"image": "https://i.imgur.com/4AiIiq3.gif", "Description": "Cheese or peppaoni pizza"},
    "Chicken Tenders": {"image": "https://i.imgur.com/4AiIiq3.gif", "Description": "Chicken tenders"},
    "Chicken Alfredo": {"image": "https://i.imgur.com/4AiIiq3.gif", "Description": "Pasta with alfredo sauce and chicken"},
    "Bacon Cheeseburger": {"image": "https://i.imgur.com/4AiIiq3.gif", "Description": "A cheeseburger with bacon on it"},
    "Bosco Sticks": {"image": "https://i.imgur.com/4AiIiq3.gif", "Description": "A breadstick with cheese inside"},
    "Chicken Quesadilla": {"image": "https://i.imgur.com/4AiIiq3.gif", "Description": "A quesadilla with chicken"},
    "Chicken Sandwich": {"image": "https://i.imgur.com/4AiIiq3.gif", "Description": "Checken inbtweem sum buns"},
    "French Toast": {"image": "https://i.imgur.com/4AiIiq3.gif", "Description": "French toast, a golden-brown, crispy yet fluffy slice of heaven that begins with thick slices of bread soaked in a rich, creamy mixture of beaten eggs, milk, vanilla extract, and a dash of cinnamon, which, when cooked to perfection on a hot griddle, transforms into a mouthwatering breakfast delicacy that’s both sweet and savory, with its crispy edges and soft, custard-like center, making it a favorite for breakfast or brunch, especially when generously topped with a pat of melting butter, a drizzle of warm maple syrup, fresh berries, or even a dusting of powdered sugar, creating a symphony of flavors and textures that dance on your taste buds and make every bite a delightful experience, reminiscent of cozy Sunday mornings, family gatherings, and the simple joys of comfort food, where each bite transports you to a place of warmth and satisfaction, blending the sweetness of the syrup with the subtle spice of the cinnamon, and the richness of the custard with the crispiness of the toasted bread, truly making French toast not just a meal, but a nostalgic, comforting experience that brings joy, contentment, and a little bit of magic to your morning routine, because let’s be real, who can resist the allure of a perfectly made French toast, with its irresistible aroma and heavenly taste that just makes you want to savor every single bite, and maybe even go back for seconds, because it’s just that good, and no cap, French toast is straight-up mogging every other breakfast out there, turning your average morning into something special, something unforgettable, something that makes you want to wake up early just to enjoy this delectable treat, knowing that every bite is worth it, and that French toast, with its blend of simplicity and indulgence, has earned its rightful place as a beloved breakfast staple, adored by many, and forever a classic in the culinary world, with each piece offering a unique texture from the crispy edges to the soft, pillowy middle, and when you add a bit of powdered sugar and some fresh fruit like strawberries or blueberries, it elevates the whole experience to a new level, and don’t even get me started on the variations, cuh, like stuffed French toast with cream cheese and berries or banana and Nutella, which just takes the whole thing to an entirely new realm of deliciousness, making it not just a breakfast but an event, something to look forward to and enjoy with family and friends, whether you’re at a fancy brunch spot or just chilling at home in your pajamas, and let's not forget the savory versions, like French toast with a bit of cheese and ham, or even avocado and smoked salmon, which might sound wild but trust me, it’s a game-changer, bringing that perfect balance of savory and sweet, and making sure that French toast stays in the breakfast hall of fame, mogging over waffles, pancakes, and whatever else is trying to compete, because at the end of the day, nothing can compare to the comfort and joy that a good piece of French toast brings, with its rich history dating back to ancient Rome, evolving through the centuries but always keeping that core appeal of turning simple ingredients into something extraordinary, and whether you’re eating it on a lazy Sunday morning or whipping it up for a special occasion, French toast is always there to remind you that sometimes the simplest things are the most extraordinary, and as you savor each bite, you’re not just enjoying a meal, but participating in a tradition that’s been loved and cherished by generations, adding your own little twist and making it part of your own culinary story, because French toast is more than just food, it’s an experience, a connection to the past, and a celebration of the present, and that, my friend, is why it will always mog any other breakfast out there, no cap. Pain perdu, une tranche de paradis dorée, croustillante mais moelleuse, qui commence par de grosses tranches de pain trempées dans un mélange riche et crémeux d'œufs battus, de lait, d'extrait de vanille et d'une pincée de cannelle, qui, une fois cuit à la perfection sur une poêle chaude, se transforme en une délicieuse gourmandise du petit-déjeuner à la fois sucrée et salée, avec ses bords croustillants et son centre doux et crémeux, en faisant un favori pour le petit-déjeuner ou le brunch, surtout lorsqu'il est généreusement garni d'une noix de beurre fondant, d'un filet de sirop d'érable chaud, de baies fraîches ou même d'une pincée de sucre glace, créant une symphonie de saveurs et de textures qui dansent sur vos papilles et font de chaque bouchée une expérience délicieuse, rappelant les matins douillets de dimanche, les réunions de famille et les simples plaisirs de la nourriture réconfortante, où chaque bouchée vous transporte dans un lieu de chaleur et de satisfaction, mélangeant la douceur du sirop avec la subtile épice de la cannelle, et la richesse de la crème avec le croustillant du pain grillé, faisant vraiment du pain perdu non seulement un repas, mais une expérience nostalgique et réconfortante qui apporte joie, contentement et un peu de magie à votre routine matinale, parce que soyons réalistes, qui peut résister à l'attrait d'un pain perdu parfaitement préparé, avec son arôme irrésistible et son goût divin qui vous donne envie de savourer chaque bouchée, et peut-être même d'en reprendre, parce que c'est tout simplement si bon, et sans mentir, le pain perdu dépasse tous les autres petits-déjeuners, transformant votre matinée moyenne en quelque chose de spécial, quelque chose d'inoubliable, quelque chose qui vous donne envie de vous lever tôt juste pour profiter de cette délicieuse gourmandise, sachant que chaque bouchée en vaut la peine, et que le pain perdu, avec son mélange de simplicité et d'indulgence, a gagné sa place de droit en tant que petit-déjeuner bien-aimé, adoré par beaucoup, et pour toujours un classique dans le monde culinaire. *** Also top it with sum slop instead of syrup *** "},
    "Pizza Crunchers": {"image": "https://i.imgur.com/4AiIiq3.gif", "Description": "Mozzarella and pizza sauce covered in breadcrumbs"},
    "General Tso's": {"image": "https://i.imgur.com/4AiIiq3.gif", "Description": "Orange chicken, with rice"},
    "Walking Tacos": {"image": "https://i.imgur.com/4AiIiq3.gif", "Description": "Ground beef and taco toppings in a bag of Doritos"},
    "Buffalo Chicken Pizza": {"image": "https://i.imgur.com/4AiIiq3.gif", "Description": "Chicken served on seasoned rice"},
    "Chicken Fajita Bowl": {"image": "https://i.imgur.com/4AiIiq3.gif", "Description": "Popcorn chicken on mashed potatoes covered in gravy"},
    "Popcorn Chicken Bowl": {"image": "https://i.imgur.com/4AiIiq3.gif", "Description": "Popcorn chicken on mashed potatoes covered in gravy"},
    "Cheeseburger": {"image": "https://i.imgur.com/4AiIiq3.gif", "Description": "CCheeseburger3"},
    "Pork Carnitas": {"image": "https://i.imgur.com/4AiIiq3.gif", "Description": "Pork Carnitas, thats just the Description you're good."},
    "Pasta w/ Meat Sauce": {"image": "https://i.imgur.com/4AiIiq3.gif", "Description": "Pasta with cool sauce on it."},
    "Loaded Potato Wedges": {"image": "https://i.imgur.com/4AiIiq3.gif", "Description": "Loaded Potato wedges, Thats it."},
    "Chicken Nuggets": {"image": "https://i.imgur.com/4AiIiq3.gif", "Description": "Chicken with nuggies."},
    "Grilled Cheese": {"image": "https://i.imgur.com/4AiIiq3.gif", "Description": "Cheese but on the grill"},
    "Brisket and Potato Bowl": {"image": "https://i.imgur.com/4AiIiq3.gif", "Description": "           "},
    "Chicken Strips": {"image": "https://i.imgur.com/4AiIiq3.gif", "Description": "Chicken but it strips."},
    "Cheeseburger Waffle Fries": {"image": "https://i.imgur.com/4AiIiq3.gif", "Description": "Burger but with waffles by it"},
    "Cheese Rippers": {"image": "https://i.imgur.com/4AiIiq3.gif", "Description": "Cheese but grim ripper"},
    "BBQ Pork Sandwich": {"image": "https://i.imgur.com/4AiIiq3.gif", "Description": "BB Pork with no Q also its a sandwitch"},
    "Cheese Ravioli w/ Meat Sauce": {"image": "https://i.imgur.com/4AiIiq3.gif", "Description": "Tasty meat."},
    "Philly Cheesesteak": {"image": "https://i.imgur.com/4AiIiq3.gif", "Description": "Cheesesteak but Philly(I dont care if it originated in Philly)"},
    "Ravioli": {"image": "https://i.imgur.com/4AiIiq3.gif", "Description": "An italian delecasy suited for only the finest in sociotey, those who taste it initally for the first time in their lives will explode and be in shock and awe at the sheer desnsity of the pasta inside this elegant, but simple dish; although to the untrained eye it may seem a contrevertial or irrelevant food, However the ravioli is just the dish for your sad saturday morning."},
    "Sweet and Sour Chicken": {"image": "https://i.imgur.com/4AiIiq3.gif", "Description": "Sour chicken with the beef"},
    "Pepperoni Stuffed Breadsticks": {"image": "https://i.imgur.com/4AiIiq3.gif", "Description": "Breadsticks with cheese and alittle bit a slop with peperoini also im seeing how long i can make the commit before it bugs out so just keep reading I swear this is a Real representation of how this food taste So just eat it because i think its very tastely"},
    "Meatball Subs": {"image": "https://i.imgur.com/4AiIiq3.gif", "Description": "Meatbull but subbed out."},
    "Slop": {"image": "https://i.imgur.com/4AiIiq3.gif", "Description": "It taste good just try it. Bi't minty but you'll get used to it. Also we got it from Shrek's swamp"},
}

food_list2 = ["Pizza", "Chicken Tenders", "Chicken Alfredo", "Bacon Cheeseburger", "Bosco Sticks", "Chicken Quesadilla", 
              "Chicken Sandwich", "French Toast", "Pizza Crunchers", "General Tso's", "Walking Tacos", "Buffalo Chicken Pizza", 
              "Chicken Fajita Bowl", "Popcorn Chicken Bowl", "Cheeseburger", "Pork Carnitas", "Pasta w/ Meat Sauce", 
              "Loaded Potato Wedges", "Chicken Nuggets", "Grilled Cheese", "Brisket and Potato Bowl", "Chicken Strips", 
              "Cheeseburger Waffle Fries", "Cheese Rippers", "BBQ Pork Sandwich", "Cheese Ravioli w/ Meat Sauce", 
             "Philly Cheesesteak", "Ravioli", "Sweet and Sour Chicken", "Pepperoni Stuffed Breadstick", 
              "Meatballs Subs", "Slop"]

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
        VotingOption(name, food_details[name]['image'], food_details[name]['Description']) 
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
