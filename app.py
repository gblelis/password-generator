import streamlit as st
import random
import string

st.set_page_config(
    layout='centered',
    page_title='Lelis Password Generator'
)


st.title('Password Generator', False)
st.subheader('By Lelis', False)

password_length_options = [i for i in range(8, 51)]

password_length = st.select_slider('Password Length', password_length_options)

checkbox_row = st.columns(4)

with checkbox_row[0]: is_uppercase = st.checkbox('Uppercase', value=True)
with checkbox_row[1]: is_lowercase = st.checkbox('Lowercase', value=True)
with checkbox_row[2]: is_number = st.checkbox('Numbers', value=True)
with checkbox_row[3]: is_symbol = st.checkbox('Symbols', value=True)

st.divider()

password = ''
if(is_lowercase or is_uppercase or is_number or is_symbol):
    while len(password) <= password_length:
        aleatorio = random.randint(0, 3)
        if aleatorio == 0:
            if(is_lowercase):
                password += random.choice(string.ascii_lowercase)
        elif aleatorio == 1:
            if(is_uppercase):
                password += random.choice(string.ascii_uppercase)
        elif aleatorio == 2:
            if(is_number):
                password += random.choice(string.digits)
        else:
            if(is_symbol):
                password += random.choice(string.punctuation)
else:
    password = 'Choose at least one option'


st.code(password, 'http')