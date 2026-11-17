# python3 -m venv .venv
# pip install Streamlit
# pip install streamlit_option_menu
# pip install streamlit.components.v1
# python -m streamlit hello
# python -m streamlit run PC4_duo.py

import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components

### Opción 1: Menú vertical
# with st.sidebar:
    # opciones = option_menu("Selecciona una sección: ",['Presentación', 'Experiencia', 'Gráficos'] , 
        # icons=['0-circle','1-circle', '2-circle'], menu_icon="filetype-py", default_index=0)

### Opción 2: Menú horizontal
opciones_2 = option_menu(
    menu_title="Menú: ", 
    options=['Presentación', 'Experiencia', 'Gráficos'], 
    icons=['people','emoji-laughing-fill', 'easel'], 
    menu_icon="cast", default_index=0, orientation="horizontal") # none

if opciones_2 == 'Presentación':
    st.markdown("<h1 style='text-align: center; font-size: 50 px; color: black'>¿Qué hicimos en Pensamiento Computacional?</h1>", unsafe_allow_html=True) #editar aspecto del texto / título del blog

    # Alumno a
    col1, col2 = st.columns(2)
    
    col1.image("DSC_0126.HEC", caption='Sofia', width=300)

    texto = """
    ¡Bienvenidos al blog! Soy Sofía, comunicadora para el Desarrollo en formación, cat-lover y swiftie. 
    A veces pinto con acuarelas, a veces me dedico al tejido y a veces toco piano. Con Yasuri hicimos este blog como proyecto del curso de Pensamiento Computacional en la PUCP.  Aquí recopilamos lo realizado y aprendido en este curso a lo largo del ciclo 2026-II. 
    """
    col2.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto}</div>", unsafe_allow_html=True)

    # Alumno b
    col1, col2 = st.columns(2)
    
    texto_2 = """
    ¡Hola! Soy Yasuri, estudiante de Comunicación Audiovisual. Soy fan del K-pop (especialmente BTS) y no me gustan las fiestas porque me da sueño muy temprano, mis amigos dicen que soy un viejita en el cuerpo de una persona de 20 años. Esperamos les guste el blog que hicimos con tanta dedicación. ¡Esperamos aportar un granito de arena a este curso con nuestro proyecto!
    """
    col1.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto_2}</div>", unsafe_allow_html=True)
    
    col2.image("DSC_0135.HEC", caption='Yas', width=300)
    
elif  opciones_2 == 'Experiencia':

    st.markdown("<h1 style='text-align: center; font-size: 50 px; color: black'>Nuestra experiencia y videos 💻</h1>", unsafe_allow_html=True)

    # Alumno a
    texto_3 = """
    Aquí escribe tu experiencia aprendiendo a programar. 
    ¿Cómo te sentiste al principio? 
    ¿Qué te ha enseñado la programación? 
    ¿Qué te gusta de programar? 
    ¿Qué te gustaría hacer con la programación en el futuro?
    """
    st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_3}</div>", unsafe_allow_html=True)
    
    # Formato YouTube
    # st.subheader("🎥 Título apropiado video 1")
    # st.video("https://www.youtube.com/watch?v=X_Z7d04x9-E")
    
    # Formato Google Drive
    # Video 1 - Sofia
    st.subheader("🎥 Estructuras condicionales")

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:  
        st.link_button("🎥 Mira el video aquí >>",
                       "https://drive.google.com/file/d/1h_DUh-bDni-EzudxrKC5yopkWndQZh6t/view?usp=sharing",
                       use_container_width=True
            )

    # Alumno b
    texto_4 = """
    Cuando supe que iba a "programar" me asusté y pensé que sería muy dificil. Sin embargo, con la práctica me di cuenta de que no es muy complicado. La programación me ha enseñado a que es posible para cualquier persona usar esta herramiento y no solo las personas de ingeniería. Lo que me gusta de programar es que a través de solo códigos podamos hacer grandes cosas -Yasuri. 
    """
    st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_4}</div>", unsafe_allow_html=True)
        
    # Formato YouTube
    # st.subheader("🎥 Título apropiado video 1")
    # st.video("https://www.youtube.com/watch?v=X_Z7d04x9-E")
        
    # Formato Google Drive
    # VIDEO 2 - Yasuri
    st.subheader("🎥 Strings y listas")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:  
        st.link_button("🎥 Mira el video aquí",
                       "https://drive.google.com/file/d/1npm1POLdNr69TrULSe5PzwM0DLpymoUB/view?usp=drive_link",
                       use_container_width=True
             )
        
    # Formato Google Drive
    # VIDEO 3 - Yasuri y Sofia
    st.subheader("🎥 Estructuras condicionales")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:  
        st.link_button("🎥 Mira el video aquí >>",
                       "https://drive.google.com/file/d/1lRspHKXyLSrD7RtK3kzYDyh2mEbonQYP/view?usp=sharing",
                       use_container_width=True
             )
    
            
else:

    st.markdown("<h1 style='text-align: center;font-size: 50 px; color: black'>Nombre a la sección</h1>", unsafe_allow_html=True)
    
    # Aquí todos los integrantes deben poner sus 3 gráficos y su mapa en la lista 
    # y aumentar la estructura condicional como sea necesaria
    graficos = ['Gráfico_1', 'Gráfico_2', 'Mapa_1'] 
    grafico_seleccionado = st.selectbox('Selecciona un gráfico', graficos)
    
    if grafico_seleccionado == 'Gráfico_1':
        st.subheader("📊 Gráfico 1: Wordcloud - Yasuri")
        texto_5 = """
        Este Wordcloud muestra la primera parte del libro La vegetariana (Hang Kang), las palabras mas grandes son las palabras que se repiten constantemente y las palabras mas pequeñas las que menos se repiten. Para crear este Wordcloud, primero se depuró el texto quitándole los stopwords, signos de puntuación y convirtiendo el texto a minúsculas.
        """
        st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_5}</div>", unsafe_allow_html=True)

        col1, col2, col3 = st.columns([1, 7, 1])
        with col2:
                st.image("wordcloud.png", width=1000)

    elif grafico_seleccionado == 'Gráfico_2':
        st.subheader("📊 Gráfico 2: Histograma - Yasuri")
        texto_6 = """
        El hsitograma muestra la distribución de los goles anotados como Local y  goles recibidos como Visitante del equipo Athlético Madrid. Anotaron más goles de los que recibieron. 
        """
        st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_6}</div>", unsafe_allow_html=True)
    
        col1, col2, col3 = st.columns([1, 7, 1])
        with col2:
            st.image("histograma.png", width=800)
    
    else:
        st.subheader("🗺️ Mapa 1: Distribución geográfica - Yasuri")
        texto_7 = """
        El mapa muestra el lugar de nacimiento de los pilotos L. Hamilton (Inglaterra) y L. Perez (México), con algunos datos como el nombre del piloto, el nombre de la escudería, el puntaje total que iobtuvieron en el F1-2016 y una imagen de de ellos. 
        """
        st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_7}</div>", unsafe_allow_html=True)
            
        with open("mapa.html", "r", encoding="utf-8") as mapa:
                html_content = mapa.read()
    
        components.html(html_content,height=600)
    