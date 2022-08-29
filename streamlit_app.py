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

#select fruit you want more info on
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")

# take JSON and normalise to data
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# put the normalised data into a table
streamlit.dataframe(fruityvice_normalized)

import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * FROM FRUIT_LOAD_LIST")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)

#select fruit of choice
add_my_fruit = streamlit.text_input('What fruit would you like to add?','Kiwi')
streamlit.write('Thanks for adding ', add_my_fruit)
                  
