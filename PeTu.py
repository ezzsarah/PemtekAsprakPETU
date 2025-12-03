import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("Pemtek A💖")

# Isi salam — kamu bisa ganti langsung di sini
nama = "P2 Gacor"
AsprakPeTu = "Irpunk_Sartaq_Gipps"

# Gambar hati
t = np.linspace(0, 2 * np.pi, 1000)
x = 20 * np.sin(t)**3
y = (17 * np.cos(t) 
     - 7 * np.cos(2 * t) 
     - 4 * np.cos(3 * t) 
     - np.cos(4 * t))

fig, ax = plt.subplots(figsize=(7,7))
ax.fill(x, y, color='red', alpha=0.9)
ax.text(0, 0, f"Hi guyss, Selamat menamatkan \npraktikum pemtek iaa, \nTengkyu atas kerjasamanya, \nand cemungutss projeknyaa, \n{nama} ", fontsize=18, 
        color="white", ha='center', va='center')
ax.set_aspect('equal')
ax.axis('off')
st.pyplot(fig)

# Tampilkan salam hangat di luar hati
st.write("")
st.markdown(f"**Asprak PeDuaa,**  \n{AsprakPeTu}")

st.write("---")  # garis pembatas

st.subheader("Tinggalkan kesan / pesanmu 💬")

with st.form("form_pesan"):
    pengirim_pesan = st.text_input("Namamu (opsional):", "")
    pesan = st.text_area("Tulis pesannya di sini:", "", height=150)
    submitted = st.form_submit_button("Kirim pesan")

if submitted:
    st.success("Terima kasih! Pesanmu sudah dikirim.")
    # Tampilkan pesan yang dikirim
    st.write("**Pesan dari:**", pengirim_pesan if pengirim_pesan else "Anonim")
    st.write("**Isi pesan:**")
    st.write(pesan)






