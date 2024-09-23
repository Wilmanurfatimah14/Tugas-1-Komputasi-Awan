import streamlit as st

x = st.number_input("Masukan Angka")
sx = st.text_input("Satuan", "C")
st.write("Anda memasukan", x,'',sx)
sy = st.text_input("Dikonversi ke", "C")
st.write (x, ' ',sx, '=', y,sy)

