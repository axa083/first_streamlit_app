import streamlit

streamlit.title('The Healthy Diner')
streamlit.header('Breakfast Best Hits 🙏')
streamlit.text('MEXICAN OMELETTE (V) 🇲🇽')
streamlit.text('SWEET POTATO ROSTI (V/GF) 🍠')
streamlit.text('SALMON FISH CAKE 🍥')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
                  
