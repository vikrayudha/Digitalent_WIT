import streamlit as st

st.markdown("# Ayo kita coba jawab pertanyaan di bawah :woman-raising-hand::fire:")
st.sidebar.markdown("# QUIZ :broken_heart:")

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

local_css("style.css")

col1, col2 = st.columns(2)
with col1:
    st.write('Pertanyaan 1')
    st.subheader('''Apa kepanjangan dari DNS?''')
    if st.button('a. Damage Name Sensor'):
        st.markdown(':x: Yah kamu salah :cry:')
    if st.button('b. Domain Name System'):
        st.markdown(':heavy_check_mark: Kamu pinter banget :thumbsup::heart_eyes:')
    if st.button('c. Domain Nine Shine'):
        st.markdown(':x: Ayo coba lagi! :muscle:')

with col2:
    st.write('Pertanyaan 2')
    st.subheader('''Jenis IPv berapa aja yang kamu bisa ganti?
    ''')
    if st.button('a. IPv4 dan IPv6'):
        st.markdown(':heavy_check_mark: Keren! :sunglasses:')
    if st.button('b. IPv3 dan IPv4'):
        st.markdown(':x: Masih berani coba? :smirk:')
    if st.button('c. IPv5 dan IPv6'):
        st.markdown(':x: Kamu masih punya kesempatan :wink:')
