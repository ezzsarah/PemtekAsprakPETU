import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import json
import os

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

st.subheader("Kesan Pesannya Gusyy 💬")

with st.form("form_pesan"):
    pengirim_pesan = st.text_input("Nama (nama panggung):", "")
    pesan = st.text_area("Gaskkann Isi:", "", height=150)
    submitted = st.form_submit_button("Submit y")

if submitted:
   # Simpan ke file JSON
    data = {
        "pengirim": pengirim_pesan,
        "pesan": pesan
    }
    fn = "pesan.json"
    if os.path.exists(fn):
        with open(fn, "r", encoding="utf-8") as f:
            all_data = json.load(f)
    else:
        all_data = []
    all_data.append(data)
    with open(fn, "w", encoding="utf-8") as f:
        json.dump(all_data, f, ensure_ascii=False, indent=2)
    st.success("Terima kasih! P2 ❤️")

# st.write("---")
st.subheader("🔒 Asprak Archieve")

password = st.text_input("ssttt:", type="password")
if password == "PeDua":
    # tampilkan semua pesan
    if os.path.exists("pesan.json"):
        with open("pesan.json", "r", encoding="utf-8") as f:
            all_data = json.load(f)
        st.write("Submitted:", len(all_data))
        for idx, d in enumerate(all_data, 1):
            st.write(f"**KesanPesan {idx}**")
            st.write("Dari:", d.get("pengirim", "Anonim"))
            st.write("Isi:", d.get("pesan", ""))
            st.write("---")
    else:
        st.write("Not yet.")
elif password:
    st.error("Password salah.")












