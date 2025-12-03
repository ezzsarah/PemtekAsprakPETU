import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("Pemtek A💖")

# Isi salam — kamu bisa ganti langsung di sini
nama = "P2 Gacor"
AsprakPeTu = "Irpunk_Sartaq_Gipps"

# Gambar hati
t = np.linspace(0, 2 * np.pi, 1000)
x = 16 * np.sin(t)**3
y = (13 * np.cos(t) 
     - 5 * np.cos(2 * t) 
     - 2 * np.cos(3 * t) 
     - np.cos(4 * t))

fig, ax = plt.subplots(figsize=(5,5))
ax.fill(x, y, color='red', alpha=0.8)
ax.text(0, 0, f"Selamat menamatkan pemtek P2, \nTengkyu atas kerjasamanya, \ncemungutss projeknyaa, {nama} 💖", fontsize=18, 
        color="white", ha='center', va='center')
ax.set_aspect('equal')
ax.axis('off')
st.pyplot(fig)

# Tampilkan salam hangat di luar hati
st.write("")
st.markdown(f"**Pemtek A,**  \n{AsprakPeTu}")
