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
    st.markdown("<h1 style='text-align: center; font-size: 50 px; color: black'>Diario de código</h1>", unsafe_allow_html=True) #editar aspecto del texto / título del blog

    # Alumno a
    col1, col2 = st.columns(2)
    
    col1.image("ft_sofia.png", caption='Sof', width=300)

    texto = """
    ¡Bienvenidos al blog! Soy Sofía, comunicadora para el desarrollo en formación, cat-lover y swiftie. 
    Soy de la ciudad de Lima y me encanta pasear por el centro histórico. 
    A veces pinto con acuarelas, a veces hago crochet o toco piano. En este blog recopilamos lo 
    aprendido en el curso Pensamiento Computacional 2026-2 en la PUCP.  ¡Exploren la página para descubrir más!
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
    texto_3 = """ Antes de llevar este curso no conocía mucho del lenguaje de programación, lo asociaba
    más a los hackers o ingenieros de software. Me parecía difícil de aprender y le tenía cierto rechazo. 
    Ahora, cuando programo me siento hacker. He aprendido a usar condicionales, hacer gráficos y mapas. 
    Lo que me gusta de programar es que te permite procesar y sintetizar una gran cantidad de información
    de modo automatizado, y presentarla con herramientas visuales fáciles de comprender.  
    Pienso que aplicaré la programación en futuros proyectos donde sea necesario trabajar con grandes cuerpos de datos. 
    - Sofia
    """
    st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_3}</div>", unsafe_allow_html=True)
    
    # Formato YouTube
    # st.subheader("🎥 Título apropiado video 1")
    # st.video("https://www.youtube.com/watch?v=X_Z7d04x9-E")
    
    # Formato Google Drive
    # Video 1 - Sofia
    st.subheader("🎥 String y listas - S")

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:  
        st.link_button("🎥 Mira el video aquí",
                       "https://drive.google.com/file/d/1h_DUh-bDni-EzudxrKC5yopkWndQZh6t/view?usp=sharing",
                       use_container_width=True
            )

    # Alumno b
    texto_4 = """
    Cuando supe que iba a "programar" me asusté y pensé que sería muy difícil. Sin embargo, con la práctica me di cuenta de que no es muy complicado. La programación me ha enseñado a que es posible para cualquier persona usar esta herramienta y no solo las personas de ingeniería. Lo que me gusta de programar es que a través de solo códigos podamos hacer grandes cosas -Yasuri. 
    """
    st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_4}</div>", unsafe_allow_html=True)
        
    # Formato YouTube
    # st.subheader("🎥 Título apropiado video 1")
    # st.video("https://www.youtube.com/watch?v=X_Z7d04x9-E")
        
    # Formato Google Drive
    # VIDEO 2 - Yasuri
    st.subheader("🎥 Strings y listas - Y")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:  
        st.link_button("🎥 Mira el video aquí",
                       "https://drive.google.com/file/d/1npm1POLdNr69TrULSe5PzwM0DLpymoUB/view?usp=drive_link",
                       use_container_width=True
             )
        
    # Formato Google Drive
    # VIDEO 3 - Yasuri y Sofia
    st.subheader("🎥 Estructuras condicionales - Y y S")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:  
        st.link_button("🎥 Mira el video aquí",
                       "https://drive.google.com/file/d/1lRspHKXyLSrD7RtK3kzYDyh2mEbonQYP/view?usp=sharing",
                       use_container_width=True
             )
    
            
else:

    st.markdown("<h1 style='text-align: center;font-size: 50 px; color: black'>Nombre a la sección</h1>", unsafe_allow_html=True)
    
    # Aquí todos los integrantes deben poner sus 3 gráficos y su mapa en la lista 
    # y aumentar la estructura condicional como sea necesaria
    graficos = ['Nube de palabras', 'Histograma', 'Pastel', 'Gráfico de barras', 'Mapas'] 
    grafico_seleccionado = st.selectbox('Selecciona un gráfico', graficos)

    if grafico_seleccionado == 'Nube de palabras':
        st.subheader("☁️ Wordcloud - Los juegos del hambre")
        texto_5 = """
        En este gráfico vemos las palabras más repetidas del primer capítulo del libro 'Los juegos del hambre' de Suzzane Collins. Esto
        se logró mediante la depuración de signos de puntuación y stopwords del texto original en inglés. 
        Las palabras más grandes refieren a lugares, personajes y elementos importantes de la historia. Así, la nube
        de palabras nos da un primer vistazo general a las temáticas de la obra.
        """
        st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_5}</div>", unsafe_allow_html=True)
            
        col1, col2, col3 = st.columns([1, 7, 1])
        with col2:
            st.image("wordcloud_s.png", width=1500)
            
    
    elif grafico_seleccionado == 'Histograma':
        st.subheader("📊 Histograma - Barcelona")
        texto_6 = """
        Los histogramas muestran los goles de Barcelona anotados como local y los goles recibidos como visitante. 
        En el primer gráfico se observa que Barcelona como local anotó 3 goles como moda, 1 gol como mínimo y 6 como máximo por partido. 
        Además, la cantidad de goles anotados se concentra dentro del rango de 2 a 4 goles. 
        El segundo gráfico muestra que los goles recibidos como visitante se concentran de modo casi parejo dentro del rango de 0-2, 
        con el raro caso de 3 o 4 goles como máximo (esto ocurrió solo en 3 ocasiones en total). 
        En general, Barcelona demuestra un buen desempeño constante como local, manteniendo una racha alta de goles (3 como tendencia), 
        mientras que como visitante ha limitado los goles recibidos al mínimo (solo de 0 a 2). 
        En comparación, el equipo como local ha anotado más goles que los que ha recibido como visitante por partido. 
        """
        st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_6}</div>", unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1, 7, 1])
        with col2:
                st.image("histograma_Barcelona.png", width=1000)
    
    elif grafico_seleccionado == 'Pastel':
        st.subheader("📊 Gráfico de pastel - Barcelona")
        texto_7 = """
        El gráfico muestra la distribución de resultados de Barcelona como visitante durante la Liga 2025-2026.
        Barcelona ha ganado la gran mayoría de los partidos que jugó como visitante, con más del 60% de victorias. 
        Por el contrario, los partidos perdidos representan poco más de un tercio del total. 
        Los partidos empatados constituyen un mínimo de aproximadamente el 5%, lo que muestra una marcada diferencia en los resultados bien como Victoria o Derrota. 
        En general, se observan resultados muy favorables obtenidos por Barcelona como visitante a lo largo de la Liga, obteniendo predominantemente la Victoria.             """
        st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_7}</div>", unsafe_allow_html=True)
            
        col1, col2, col3 = st.columns([1, 7, 1])
        with col2:
                st.image("pastel_Barcelona.png", width=1000)

    elif grafico_seleccionado == 'Gráfico de barras':
        st.subheader("📊 Gráfico de barras 1")
        texto_8 = """
        El gráfico muestra el promedio de tarjetas amarillas recibidas por los equipos de la Liga Española 2025-2026
        cuando jugaron como visitantes. Se observa que todos los equipos, cuando jugaron como visitantes, recibieron tarjetas amarillas. 
        En promedio, el rango de tarjetas amarillas recibidas es desde 2 hasta 3 tarjetas como máximo. Asimismo, la mayoría de equipos (13) recibió 
        en promedio solo 2 tarjetas amarillas, mientras que los demás recibieron 3. En general, la cantidad de tarjetas amarillas que los equipos 
        visitantes recibieron por partido se mantuvo dentro de un rango constante y limitado.        
        """
        st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_8}</div>", unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1, 7, 1])
        with col2:
                st.image("grafico_barras_s.png", width=1000)
        
    else:
        st.subheader("🗺️ Mapa 1: Pilotos Hamilton y Bottas de la Fórmula 1")
        texto_9 = """
        El mapa muestra los lugares de nacimiento de los pilotos Hamilton y Bottas de la Fórmula 1. 
        La presentación de la ventana popup muestra el nombre del piloto en el encabezado 1 en negrita, luego la escudería y el puntaje total. 
        Elegí presentar los datos en este orden porque me pareció adecuado según prioridad de los datos y porque facilita la visualización el poder ver 
        la foto y nombre primero para ubicar rápidamente al personaje. Además, elegí presentar el dato de la escudería y el puntaje dentro de una frase 
        string cada una para especificar qué información era (es decir, que no solo se muestre el número del puntaje sino precisar "Puntaje total: ##"), 
        y los separé para que cada uno ocupe una línea para mayor diferenciación (que no salga todo el texto en la misma línea). 
        También amplíe el ancho del marco de la imagen para ajustarlo a las fotos elegidas (que se vea el premio de Bottas, por ejemplo).
        En cuanto al mapa, utilicé unas coordenadas centrales ubicadas en Estocolmo porque era un lugar aproximadamente a media distancia 
        entre las ciudades de nacimiento de cada piloto (entre los marcadores). También usé el signo de una estrella en los marcadores, 
        ya que se asocia a los piltos famosos. Así se puede ubicar los marcadores más fácilmente y de cerca.            
        """
        st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_9}</div>", unsafe_allow_html=True)
                
        with open("mapa_S.html", "r", encoding="utf-8") as mapa_S:
                    html_content = mapa_S.read()
        
        components.html(html_content,height=600)

    #gráficos Yasuri
    
    if grafico_seleccionado == 'Nube de palabras':
        st.subheader("☁️ Wordcloud La vegetariana")
        texto_10 = """
        Este Wordcloud muestra la primera parte del libro La vegetariana (Hang Kang), las palabras mas grandes son las palabras que se repiten constantemente y las palabras mas pequeñas las que menos se repiten. Para crear este Wordcloud, primero se depuró el texto quitándole los stopwords, signos de puntuación y convirtiendo el texto a minúsculas.
        """
        st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_10}</div>", unsafe_allow_html=True)

        col1, col2, col3 = st.columns([1, 7, 1])
        with col2:
                st.image("wordcloud.png", width=1000)

        

    elif grafico_seleccionado == 'Histograma':
        st.subheader("📊 Histograma ATHM")
        texto_11 = """
        El histograma muestra la distribución de los goles anotados como Local y  goles recibidos como Visitante del equipo Athlético Madrid. Anotaron más goles de los que recibieron. 
        """
        st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_11}</div>", unsafe_allow_html=True)
    
        col1, col2, col3 = st.columns([1, 7, 1])
        with col2:
            st.image("histograma.png", width=800)

    elif grafico_seleccionado == 'Pastel':
        st.subheader("📊 Gráfico de pastel ATHM")
        texto_7 = """
        El gráfico de pastel muestra en procentajes el rendimiento del Athlético Madrid durante la temporada 2025-2026. Los resultados muestran que el equipo ganó mas del 50% de los partidos de la temporada, tuvo algunos partidos pérdidos y un porcentaje bajo de partidos empatados. 
        """
        st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_7}</div>", unsafe_allow_html=True)
                
        col1, col2, col3 = st.columns([1, 7, 1])
        with col2:
             st.image("pastel_Barcelona.png", width=1000)

    elif grafico_seleccionado == 'Gráfico de barras':
        st.subheader("📊 Gráfico de barras ATHM")
        texto_8 = """
       El gráfico de barras muestra el promedio de tarjetas amarrillas que el Athlético Madrid obtuvo durante la temporada 2025-26 como equipo visitante. Los resultados solo varían entre 2 y 3 tarjetas amarillas en promedio. 
        """
        st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_8}</div>", unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1, 7, 1])
        with col2:
                st.image("grafico_barras_s.png", width=1000)
        
    
    else:
        st.subheader("🗺️ Distribución geográfica HAMILTON PEREZ")
        texto_12 = """
        El mapa muestra el lugar de nacimiento de los pilotos L. Hamilton (Inglaterra) y L. Perez (México), con algunos datos como el nombre del piloto, el nombre de la escudería, el puntaje total que iobtuvieron en el F1-2016 y una imagen de de ellos. 
        """
        st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_12}</div>", unsafe_allow_html=True)
            
        with open("mapa.html", "r", encoding="utf-8") as mapa:
                html_content = mapa.read()
    
        components.html(html_content,height=600)

    