import streamlit as st

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

local_css("style3.css")

st.markdown ("# TERIMA KASIH 🤩🙇‍♀️")
st.markdown('# 🎉 👏👏👏 🎉')


st.sidebar.markdown("# Penutup")

with st.sidebar.form(key='Form1'):
    judul = st.text_input('Kritik dan Saran')
    nilai = st.slider('Penilaian',min_value=0,max_value=10)
    masuk = st.form_submit_button(label='Submit')
if masuk:
    st.sidebar.success("Terimakasih Masukannya 😄")
    st.snow()