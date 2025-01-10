import streamlit as st
import numpy as np

# Fungsi untuk metode Trapezoidal Rule
def trapezoidal_rule(x, y):
    n = len(x)  # jumlah titik (jumlah subinterval + 1)
    integral = (x[-1] - x[0]) * (y[0] + 2 * np.sum(y[1:n-1]) + y[n-1]) / (2 * (n - 1))
    return integral

# Fungsi untuk metode Simpson's Rule
def simpsons_rule(x, y):
    n = len(x)
    if n % 2 == 0:
        raise ValueError("Metode Simpson memerlukan jumlah titik ganjil.")
    h = (x[-1] - x[0]) / (n - 1)
    integral = y[0] + y[-1]
    for i in range(1, n-1):
        weight = 4 if i % 2 != 0 else 2
        integral += weight * y[i]
    return integral * h / 3

# Judul aplikasi
st.title("Kalkulator Numerik: Trapezoidal dan Simpson's Rule")

# Sidebar untuk input data
st.sidebar.header("Input Data")

# Input jumlah titik pembagi
num_points = st.sidebar.number_input("Jumlah titik pembagi", min_value=2, max_value=100, value=3, step=1)

# Input titik-titik pembagi
x_input = st.sidebar.text_input("Masukkan titik-titik pembagi (pisahkan dengan koma)", "0.6, 1.0, 1.4")
y_input = st.sidebar.text_input("Masukkan nilai fungsi (pisahkan dengan koma)", "3, 2.8, 2.5")

# Dropdown menu untuk memilih metode numerik
method = st.sidebar.selectbox("Pilih Metode:", ["Trapezoidal Rule", "Simpson's Rule"])

# Validasi dan perhitungan
try:
    # Parsing input string menjadi array
    x = np.array([float(i) for i in x_input.split(",")])
    y = np.array([float(i) for i in y_input.split(",")])

    # Validasi ukuran array
    if len(x) != num_points or len(y) != num_points:
        st.error("Jumlah titik-titik pembagi dan nilai fungsi harus sesuai dengan jumlah titik yang ditentukan.")
    else:
        # Pilihan metode
        if method == "Trapezoidal Rule":
            result = trapezoidal_rule(x, y)
            st.success(f"Hasil integral menggunakan Trapezoidal Rule adalah: {result}")
        elif method == "Simpson's Rule":
            if len(x) % 2 == 0:
                st.error("Metode Simpson memerlukan jumlah titik ganjil.")
            else:
                result = simpsons_rule(x, y)
                st.success(f"Hasil integral menggunakan Simpson's Rule adalah: {result}")

        # Menampilkan tabel data untuk referensi
        st.subheader("Tabel Data")
        st.write("Titik-titik pembagi (x):", x)
        st.write("Nilai fungsi (y):", y)
except Exception as e:
    st.error(f"Error: {e}")
