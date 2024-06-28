import streamlit as st

st.markdown("# DNS 1.1.1.1? :thinking_face::question:")
st.sidebar.markdown("# DNS 1.1.1.1 :thinking_face::question:")

tab1, tab2, tab3 = st.tabs(['Apa itu DNS?', 'Kenapa DNS 1.1.1.1?', 'Amankah DNS 1.1.1.1?'])
with tab1:
     st.markdown('DNS Merupakan singkatan dari _**Domain Name System**_.')
     st.write('''DNS adalah sistem yang mengubah URL website ke dalam bentuk IP Address. 
               Tanpa DNS, Anda harus mengetikkan IP Address secara lengkap ketika ingin mengunjungi sebuah website. 
               ''')
     st.write('Jaringan DNS sendiri memiliki dua sisi: ')
     
     col1, col2 = st.columns(2)
     with col1:
          from PIL import Image
          image = Image.open('C:\Streamlit\yaya\gambar\ikon1.png')
          st.image(image)
          st.subheader('Authoritative')
          st.markdown('_(sisi konten)_')
          st.write('''Setiap domain perlu memiliki provider Authoritative DNS. 
               Cloudflare sudah menjalankan layanan Authoritative DNS yang cepat dan banyak digunakan. 
               Rilis 1.1.1.1 juga tidak akan mengubah layanan Authoritative DNS Cloudflare
          ''')
     with col2:
          image = Image.open('C:\Streamlit\yaya\gambar\ikon2.png')
          st.image(image)
          st.subheader('Resolver')
          st.markdown('_(sisi konsumen)_')
          st.write('''Setiap perangkat yang terhubung ke internet memerlukan DNS resolver. 
               Secara default resolver ini diatur otomatis oleh jaringan apapun yang terhubung dengan device.  
               Jadi kebanyakan pengguna internet ketika terhubung dengan ISP atau jaringan mobile,
               operator jaringan akan mengatur DNS resolver mana yang sebaiknya digunakan
          ''')         

with tab2: 
     st.markdown('''Salah satu alasan kenapa adanya DNS adalah karena IP biasanya susah untuk diingat.
     172.217.10.46 tentunya tidak lebih sulit diingat daripada Google.com.''')
     
     image = Image.open('C:\Streamlit\yaya\gambar\project5.jpg')
     st.image(image, caption="Jenis-jenis serangan cyber")
     st.caption("<p style='text-align: center;'>sumber: https://www.wallarm.com/what/what-is-a-cyber-attack</p>", unsafe_allow_html=True)
     
     st.header('Proses adanya DNS 1.1.1.1')
     col1, col2, col3 = st.columns(3)
     with col1:
          image = Image.open('C:\Streamlit\yaya\gambar\ikon3.png')
          st.image(image)
          st.subheader('STEP 1')
          st.write('''DNS resolvers secara inheren tidak dapat menggunakan domain yang mudah diingat
          karena mereka adalah apa yang harus di-kueri untuk mencari tahu alamat IP dari sebuah domain.
          ''')
     with col2:
          image = Image.open('C:\Streamlit\yaya\gambar\ikon4.png')
          st.image(image)
          st.subheader('STEP 2')
          st.write('''Cloudflare sendiri kemudian menghubungi APNIC. 
          APNIC adalah sebuah Regional Internet Registery (RIR) yang bertanggung jawab 
          untuk mengeluarkan IP di daerah Asia Pacific.
          ''')
     with col3:
          image = Image.open('C:\Streamlit\yaya\gambar\ikon5.png')
          st.image(image)
          st.subheader('STEP 3')
          st.write('''Kelompok riset APNIC memiliki alamat IP 1.1.1.1 dan 1.0.0.1. 
          Walaupun alamatnya valid, begitu banyak orang telah memasukkan mereka ke dalam berbagai sistem acak
          sehingga mereka terus kewalahan oleh banjir traffic yang tidak bagus. 
          APNIC ingin mempelajari traffic ini, tetapi setiap kali mereka mencoba mengumumkan IP,
          banjir akan membanjiri jaringan konvensional apa pun.
          ''')

with tab3:
     st.header('''Sejak tanggal 1 April 2018, Cloudflare mengumumkan bahwa mereka sudah merilis layanan DNS baru. 
     Diberi nama 1.1.1.1
     ''')
     st.subheader('Ini adalah layanan DNS tercepat dan paling aman untuk pengguna internet di dunia saat ini.')
     st.write('''Cloudflare membangun layanan DNS tercepat ini agar sesuai dengan misi mereka yaitu
     untuk membantu membangun Internet yang lebih baik. 
     Cloudflare memiliki komitmen untuk membuat Internet menjadi lebih baik, lebih aman, dan lebih efisien.''')
     from PIL import Image
     image = Image.open('C:\Streamlit\yaya\gambar\project4.jpg')
     st.image(image, caption='Performa DNS 1.1.1.1')
     st.caption("<p style='text-align: center;'>sumber: https://www.cloudflare.com/learning/dns/what-is-1.1.1.1/</p>", unsafe_allow_html=True)
