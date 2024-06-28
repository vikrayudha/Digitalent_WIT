import streamlit as st

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

local_css("style2.css")

st.markdown("# Introduction :wave:")

st.sidebar.markdown("# KELOMPOK :five:")
st.header(":one: Fitri Susanti - Tangerang - Content")
st.header(":two: Husnul Khatimah - Makassar - Content")
st.header(":three: Maria Alberta - Surabaya - Coding")
st.header(":four: Vikra Yudha Yolanda Afza - Padang - Coding")


