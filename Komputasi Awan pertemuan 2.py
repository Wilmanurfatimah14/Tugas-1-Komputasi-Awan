import streamlit as st

x = st.number_input(
    "Insert a number", value=None, placeholder="Type a number..."
)
st.write("The current number is ", x)
st.latex(x'''
    a + ax + a x^2 + a x^3 + \cdots + a x^{n-1} =
    \sum_{k=0}^{n-1} ax^k =
    a \left(\frac{1-x^{n}}{1-x}\right)
    ''')
