import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError
streamlit.title('The Healthy Diner')
streamlit.header('Breakfast Best Hits 🙏')
streamlit.text('MEXICAN OMELETTE (V) 🇲🇽')
streamlit.text('SWEET POTATO ROSTI (V/GF) 🍠')
streamlit.text('SALMON FISH CAKE 🍥')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
#add picklist for fruit
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
#add table with fruit options
streamlit.dataframe(fruits_to_show)

streamlit.header("Fruityvice Fruit Advice!")
try:
fruit_choice = streamlit.text_input("What fruit would you like information about?")
if not fruit_choice:
streamlit.error("Please select a fruit to get information.")
else:
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
fruityvice_normalized = pandas.json normalize(fruitvvice response.json())
streamlit.dataframe(fruityvice_normalized)

except URLError as e:
streamlit. error()

streamlit.stop()

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("insert into fruit_load_list values ('from streamlit')")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)
#select fruit of choice
add_my_fruit = streamlit.text_input('What fruit would you like to add?','Kiwi')
streamlit.write('Thanks for adding ', add_my_fruit)
