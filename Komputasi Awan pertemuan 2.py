import streamlit as st

# Input angka dan satuan awal
x = st.number_input("Masukan Angka")
sx = st.text_input("Satuan", "C")
st.write("Anda memasukan", x, sx)

# Input satuan yang dikonversi ke
sy = st.text_input("Dikonversi ke", "C")
y = 0

# Logika konversi suhu
if sx == 'C':
    if sy == 'F':  # Celcius ke Fahrenheit
        y = (x * 9/5) + 32
    elif sy == 'K':  # Celcius ke Kelvin
        y = x + 273.15
    elif sy == 'C':  # Jika tidak ada konversi
        y = x
elif sx == 'F':
    if sy == 'C':  # Fahrenheit ke Celcius
        y = (x - 32) * 5/9
    elif sy == 'K':  # Fahrenheit ke Kelvin
        y = (x - 32) * 5/9 + 273.15
    elif sy == 'F':
        y = x
elif sx == 'K':
    if sy == 'C':  # Kelvin ke Celcius
        y = x - 273.15
    elif sy == 'F':  # Kelvin ke Fahrenheit
        y = (x - 273.15) * 9/5 + 32
    elif sy == 'K':
        y = x

# Output hasil konversi
st.write(x, sx, "=", y, sy)
