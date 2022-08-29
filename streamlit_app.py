import streamlit

streamlit.title('The Healthy Diner')
streamlit.header('Breakfast Best Hits 🙏')
streamlit.text('MEXICAN OMELETTE (V) 🇲🇽')
streamlit.text('SWEET POTATO ROSTI (V/GF) 🍠')
streamlit.text('SALMON FISH CAKE 🍥')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

#add picklist for fruit
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

#add table with fruit options
streamlit.dataframe(fruits_to_show)

streamlit.header("Fruityvice Fruit Advice!")

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")

# take JSON and normalise to data
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# put the normalised data into a table
streamlit.dataframe(fruityvice_normalized)
                  
