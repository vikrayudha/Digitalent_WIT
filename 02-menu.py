import streamlit as st
import streamlit_book as stb
import base64

st.set_page_config(page_title='Kelompok 5',
                   page_icon = '💡',)

stb.set_book_config(menu_title="Main Menu",
                    menu_icon="menu-button-wide-fill",
                    options=[
                            "Introduction",
                            "DNS 1.1.1.1",
                            "Tutorial DNS 1.1.1.1",
                            "Quiz",
                            "Terima Kasih"
                            ],
                    paths=[
                        "intro.py",
                        "DNS.py",
                        "Tutorial.py",
                        "Quiz.py",
                        "thx.py"
                          ],
                    icons=[
                          "house",
                          "lightbulb",
                          "gear",
                          "heart",
                          "people",
                          ],
                    #save_answers=True,
                    )

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('background4.jpg')

audio_file = open('C:\Streamlit\yaya\my_project\happy.wav', 'rb')
audio_bytes = audio_file.read()
st.sidebar.audio(audio_bytes, format='audio/mp3')

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
local_css("style2.css")

new_title = '<i style="font-family:monospace; color:White; font-size: 14px; ">Create by Kelompok 5 WIT 2022</i>'
st.sidebar.markdown(new_title, unsafe_allow_html=True)
