import streamlit as st

st.markdown("# Tutorial Menggunakan DNS 1.1.1.1. :computer: pada Windows")
st.sidebar.markdown("# TUTORIAL WINDOWS")

st.markdown(':one: Klik **_Start Menu_** kemudian masuk ke **_Control Panel_**')
if st.button('Gambar1'):
    from PIL import Image
    image = Image.open('C:\Streamlit\yaya\gambar\Tuto1.jpg')
    st.image(image, caption="Star Menu dan Control Panel")

st.markdown(':two: Klik **_Network and Internet_**')
if st.button('Gambar2'):
    from PIL import Image
    image = Image.open('C:\Streamlit\yaya\gambar\Tuto2.jpg')
    st.image(image, caption="Network and Internet")

st.markdown(':three: Klik **_Change Adapter Settings_**')
if st.button('Gambar3'):
    from PIL import Image
    image = Image.open('C:\Streamlit\yaya\gambar\Tuto3.jpg')
    st.image(image, caption="Change Adapter Settings")

st.markdown(':four: Klik **kanan pada jaringan Wi-FI** yang tersambung kemudian klik **_Properties_**')
if st.button('Gambar4'):
    from PIL import Image
    image = Image.open('C:\Streamlit\yaya\gambar\Tuto4.jpg')
    st.image(image, caption="Properties pada jaringan Wi-Fi")

st.markdown(':five: Pilih **_Internet Protocol Version 4 atau Version 6_**')
if st.button('Gambar5'):
    from PIL import Image
    image = Image.open('C:\Streamlit\yaya\gambar\Tuto6.jpg')
    st.image(image, caption="IPv4 atau IPv6")

st.markdown(':six: Klik **_Use The Following DNS Server Addresses_**')
if st.button('Gambar6'):
    from PIL import Image
    image = Image.open('C:\Streamlit\yaya\gambar\Tuto7.jpg')
    st.image(image, caption="Use The Following DNS")

st.markdown(':seven: Cari **_entri server DNS_** yang ada untuk referensi masa mendatang')
if st.button('Gambar7'):
    from PIL import Image
    image = Image.open('C:\Streamlit\yaya\gambar\Tuto8.jpg')
    st.image(image, caption="add IP")

st.markdown(''':eight: Ganti alamat DNS untuk **_IPv4: 1.1.1.1_** dan **_1.0.0.1_** atau 
    untuk **_IPv6:2606:4700:4700::1111_** dan **_2606:4700:4700::1001_**''')
if st.button('Gambar8'):
    from PIL import Image
    image = Image.open('C:\Streamlit\yaya\gambar\Tuto9.jpg')
    st.image(image, caption="DNS 1.1.1.1 dan 1.0.0.1")

st.markdown(':nine: Klik :ok: kemudian _Close_ :x:')
if st.button('Gambar9'):
    from PIL import Image
    image = Image.open('C:\Streamlit\yaya\gambar\Tuto11.jpg')
    st.image(image)

st.markdown(':one::zero: Restart browser')


