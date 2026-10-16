import streamlit as st

# Configuración inicial de la página
st.set_page_config(
    page_title="Construyamos un futuro juntos mi Hinata",
    page_icon="💜",
    layout="centered",
)

# --- ESTILOS CSS EN TEMÁTICA MORADA ---
st.markdown(
    """
    <style>
    /* Fondo principal y textos */
    .stApp {
        background-color: #120A21;
        color: #E2D9F3;
    }
    
    /* Títulos y encabezados */
    h1, h2, h3, h4 {
        color: #B388FF !important;
        text-align: center;
    }
    
    /* Estilos de botones */
    div.stButton > button {
        background-color: #7C4DFF !important;
        color: white !important;
        border-radius: 12px !important;
        border: none !important;
        padding: 10px 24px !important;
        font-weight: bold !important;
        width: 100%;
        transition: 0.3s;
    }
    
    div.stButton > button:hover {
        background-color: #B388FF !important;
        color: #120A21 !important;
        transform: scale(1.02);
    }
    
    /* Inputs de texto */
    .stTextInput input {
        background-color: #1A0F35 !important;
        color: white !important;
        border: 1px solid #7C4DFF !important;
        border-radius: 8px !important;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# --- CREDENCIALES ACTUALIZADAS ---
ID_CORRECTO = "11/10/2013"
PASSWORD_CORRECTO = "Hinata"

# --- RUTAS DE LOS ARCHIVOS LOCALES ---
AUDIO_MENU = "audio_menu.mp3"
AUDIO_INICIO = "audio_inicio.mp3"
AUDIO_DESARROLLO = "audio_desarrollo.mp3"
AUDIO_FINAL = "audio_final.mp3"

IMAGEN_INICIO = "imagen_inicio.png"
IMAGEN_FINAL = "imagen_final.jpeg"
VIDEO_DESARROLLO = "video_desarrollo.mp4"

# --- MANEJO DE ESTADO DE SESIÓN ---
if "autenticado" not in st.session_state:
  st.session_state.autenticado = False

if "pagina_actual" not in st.session_state:
  st.session_state.pagina_actual = "menu"

# --- 1. PANTALLA DE LOGIN ---
if not st.session_state.autenticado:
  st.markdown("<h1>🔐 Acceso Restringido</h1>", unsafe_allow_html=True)
  st.write("Por favor, ingresa tus datos para continuar:")

  usuario_id = st.text_input("ID (Fecha de nacimiento):", placeholder="DD/MM/AAAA")
  usuario_pass = st.text_input("Contraseña:", type="password")

  if st.button("Ingresar"):
    if usuario_id == ID_CORRECTO and usuario_pass == PASSWORD_CORRECTO:
      st.session_state.autenticado = True
      st.rerun()
    else:
      st.error("ID o contraseña incorrectos. Inténtalo de nuevo.")

# --- 2. CONTENIDO PRINCIPAL (AUTENTICADO) ---
else:
  # VISTA: MENÚ PRINCIPAL
  if st.session_state.pagina_actual == "menu":
    st.markdown(
        "<h1>Construyamos un futuro juntos mi Hinata 💜</h1>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<p style='text-align: center; font-size: 17px;'>Bienvenida a este"
        " espacio especial pensado con mucho cariño para ti. Selecciona una"
        " de las etapas para descubrir cada momento.</p>",
        unsafe_allow_html=True,
    )

    st.write("---")

    # Audio del Menú en bucle (se detiene al hacer clic en cualquier botón)
    st.audio(AUDIO_MENU, loop=True, autoplay=True)

    # Tres columnas / tarjetas de navegación
    col1, col2, col3 = st.columns(3)

    with col1:
      st.markdown("### 🚀 Inicio")
      st.write("El comienzo de nuestra historia.")
      if st.button("Ir a Inicio"):
        st.session_state.pagina_actual = "inicio"
        st.rerun()

    with col2:
      st.markdown("### 🌱 Desarrollo")
      st.write("Todo lo que hemos vivido.")
      if st.button("Ir a Desarrollo"):
        st.session_state.pagina_actual = "desarrollo"
        st.rerun()

    with col3:
      st.markdown("### ❤️ Final")
      st.write("Nuestro camino hacia adelante.")
      if st.button("Ir a Final"):
        st.session_state.pagina_actual = "final"
        st.rerun()

  # VISTA: SECCIÓN INICIO
  elif st.session_state.pagina_actual == "inicio":
    st.markdown("<h1>🚀 Inicio</h1>", unsafe_allow_html=True)

    # Audio de Inicio
    st.audio(AUDIO_INICIO, loop=True, autoplay=True)

    # Imagen mediana centrada
    col_img1, col_img2, col_img3 = st.columns([1, 2, 1])
    with col_img2:
      st.image(
          IMAGEN_INICIO,
          caption="Nuestros primeros momentos",
          use_container_width=True,
      )

    st.markdown("### El inicio de nuestro destino juntos")
    st.write(
        "Mi Hinata, cada segundo a tu lado se siente como el comienzo de algo"
        " mágico. Aún nos queda un mundo entero por recorrer, pero saber que"
        " existes y que nuestros caminos se cruzaron es lo más hermoso que me"
        " ha pasado. Te amo con todas mis fuerzas, te pienso en cada instante"
        " y sé que este es apenas el primer capítulo de nuestra gran"
        " historia."
    )

    st.write("---")
    if st.button("⬅️ Regresar al Menú Principal"):
      st.session_state.pagina_actual = "menu"
      st.rerun()

  # VISTA: SECCIÓN DESARROLLO
  elif st.session_state.pagina_actual == "desarrollo":
    st.markdown("<h1>🌱 Desarrollo</h1>", unsafe_allow_html=True)

    # Audio de Desarrollo
    st.audio(AUDIO_DESARROLLO, loop=True, autoplay=True)

    # Video mediano centrado
    col_vid1, col_vid2, col_vid3 = st.columns([1, 2, 1])
    with col_vid2:
      st.video(VIDEO_DESARROLLO)

    st.markdown("### Escribiendo nuestra historia paso a paso")
    st.write(
        "Mi amor, cada risa, cada momento compartido y cada detalle nuestro va"
        " construyendo lo que somos. No importa los retos que vengan, me"
        " encanta saber que estamos aprendiendo y creciendo juntos. Eres mi"
        " refugio, mi paz y la dueña de todos mis pensamientos. Te amo hoy,"
        " mañana y siempre, mi preciosa Hinata."
    )

    st.write("---")
    if st.button("⬅️ Regresar al Menú Principal"):
      st.session_state.pagina_actual = "menu"
      st.rerun()

  # VISTA: SECCIÓN FINAL
  elif st.session_state.pagina_actual == "final":
    st.markdown("<h1>❤️ Final</h1>", unsafe_allow_html=True)

    # Audio de Final
    st.audio(AUDIO_FINAL, loop=True, autoplay=True)

    # Imagen mediana centrada
    col_img1, col_img2, col_img3 = st.columns([1, 2, 1])
    with col_img2:
      st.image(
          IMAGEN_FINAL,
          caption="Un futuro prometedor",
          use_container_width=True,
      )

    st.markdown("### Un futuro infinito a tu lado")
    st.write(
        "Si esto es lo bonito del camino, no puedo imaginar lo maravilloso que"
        " será nuestro mañana. Mi única meta es seguir construyendo este"
        " hermoso futuro a tu lado, cuidándote y amándote como mereces. Eres el"
        " sueño más lindo hecho realidad, mi Hinata, y te prometo que lo mejor"
        " de nuestra historia todavía está por escribirse."
    )

    st.write("---")
    if st.button("⬅️ Regresar al Menú Principal"):
      st.session_state.pagina_actual = "menu"
      st.rerun()
