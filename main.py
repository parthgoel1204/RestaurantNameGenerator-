import streamlit as st
import langchainHelper
st.title("Restaurant Name Generator")

cuisine = st.sidebar.selectbox(
  "Select a cuisine",
  ("American", "Italian", "Mexican", "Chinese", "Indian" , "Afghani", "French", "Greek", "Japanese", "Korean", "Mediterranean", "Spanish", "Thai", "Vietnamese")
)

if cuisine:
  response = langchainHelper.generate_restaurant_name_and_items(cuisine)
  st.header(response['restaurant_name'].strip())
  st.subheader("Menu Items")
  menu_items = response['menu_items'].strip().split(",")

  for item in menu_items:
    st.write("-", item)