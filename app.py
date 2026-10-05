import streamlit as st

# =========================================================
# CONFIGURACIÓN GENERAL
# =========================================================

st.set_page_config(
    page_title="Sistema Experto | Oncología Mamaria",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# ESTILOS
# =========================================================

st.markdown("""
<style>

[data-testid="stAppViewContainer"] {
    background: #f6f8fb;
}

.block-container {
    max-width: 1150px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* CABECERA */

.hero {
    background: linear-gradient(135deg, #7b1e48 0%, #a63162 100%);
    padding: 2rem 2.2rem;
    border-radius: 18px;
    color: white;
    margin-bottom: 1.5rem;
    box-shadow: 0 8px 24px rgba(0,0,0,0.08);
}

.hero-title {
    font-size: 2.2rem;
    font-weight: 750;
    margin-bottom: 0.3rem;
}

.hero-subtitle {
    font-size: 1.05rem;
    opacity: 0.92;
}

/* TARJETAS */

.card {
    background: white;
    padding: 1.4rem;
    border-radius: 16px;
    border: 1px solid #e7e9ef;
    box-shadow: 0 4px 15px rgba(0,0,0,0.04);
    margin-bottom: 1rem;
}

.card-title {
    font-size: 1.15rem;
    font-weight: 700;
    margin-bottom: 0.5rem;
}

.soft-text {
    color: #667085;
    font-size: 0.95rem;
}

/* RESULTADOS */

.result-level-1 {
    background: #fff1f2;
    border-left: 6px solid #dc2626;
    padding: 1.3rem;
    border-radius: 12px;
}

.result-level-2 {
    background: #fff7ed;
    border-left: 6px solid #f59e0b;
    padding: 1.3rem;
    border-radius: 12px;
}

.result-level-3 {
    background: #ecfdf3;
    border-left: 6px solid #16a34a;
    padding: 1.3rem;
    border-radius: 12px;
}

/* ETIQUETAS */

.badge {
    display: inline-block;
    padding: 0.3rem 0.7rem;
    border-radius: 999px;
    background: #f1f3f7;
    font-size: 0.85rem;
    margin-right: 0.3rem;
}

/* BOTÓN */

.stButton > button,
.stFormSubmitButton > button {
    border-radius: 10px;
    font-weight: 600;
    min-height: 3rem;
}

/* SIDEBAR */

section[data-testid="stSidebar"] {
    background-color: #ffffff;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# FUNCIONES DEL SISTEMA EXPERTO
# =========================================================

def determinar_masa_mamaria(bulto_nuevo, duro_fijo):

    # RULE 1
    if bulto_nuevo == "Sí" and duro_fijo == "Sí":
        return "Prioritaria", "RULE 1"

    # RULE 2
    if bulto_nuevo == "Sí" and duro_fijo == "No":
        return "Presente", "RULE 2"

    # RULE 3
    return "Ausente", "RULE 3"


def determinar_alteraciones_piel_pezon(
    cambio_piel,
    retraccion_pezon
):

    # RULE 4
    if cambio_piel == "Sí" or retraccion_pezon == "Sí":
        return "Sí", "RULE 4"

    # RULE 5
    return "No", "RULE 5"


def determinar_signos_asociados(
    secrecion_sanguinolenta,
    ganglios
):

    # RULE 6
    if secrecion_sanguinolenta == "Sí" or ganglios == "Sí":
        return "Sí", "RULE 6"

    # RULE 7
    return "No", "RULE 7"


def determinar_nivel_atencion(
    masa_mamaria,
    alteraciones_piel_pezon,
    signos_asociados
):

    # RULE 8
    if (
        masa_mamaria == "Prioritaria"
        or alteraciones_piel_pezon == "Sí"
        or signos_asociados == "Sí"
    ):
        return (
            1,
            "Evaluación médica prioritaria",
            "RULE 8"
        )

    # RULE 9
    if (
        masa_mamaria == "Presente"
        and alteraciones_piel_pezon == "No"
        and signos_asociados == "No"
    ):
        return (
            2,
            "Evaluación médica recomendada",
            "RULE 9"
        )

    # RULE 10
    return (
        3,
        "No se identificaron signos de alarma dentro de los criterios evaluados",
        "RULE 10"
    )


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.title("🩺 Sistema Experto")

    st.markdown(
        """
        **Especialidad:** Oncología  
        **Área:** Oncología mamaria  
        **Tipo:** Sistema experto basado en reglas
        """
    )

    st.divider()

    st.markdown("### Funcionamiento")

    st.markdown(
        """
        1. Se recopilan los signos reportados.
        2. Se activan reglas IF–THEN.
        3. Se obtienen factores intermedios.
        4. El motor de inferencia determina el nivel de atención.
        """
    )

    st.divider()

    st.warning(
        "Prototipo académico. No sustituye una evaluación médica."
    )


# =========================================================
# CABECERA
# =========================================================

st.markdown("""
<div class="hero">
    <div class="hero-title">
        Sistema Experto de Oncología Mamaria
    </div>

    <div class="hero-subtitle">
        Evaluación preliminar de signos de alarma asociados al cáncer de mama
    </div>
</div>
""", unsafe_allow_html=True)


# =========================================================
# INFORMACIÓN INICIAL
# =========================================================

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
        <div class="card-title">🎯 Objetivo</div>
        <div class="soft-text">
        Identificar signos de alarma mediante una base de conocimiento
        compuesta por reglas.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <div class="card-title">🧠 Motor de inferencia</div>
        <div class="soft-text">
        Evalúa hechos ingresados y aplica reglas IF–THEN para obtener
        una conclusión.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
        <div class="card-title">📋 Resultado</div>
        <div class="soft-text">
        El sistema determina uno de tres niveles de orientación médica.
        </div>
    </div>
    """, unsafe_allow_html=True)


# =========================================================
# FORMULARIO
# =========================================================

st.markdown("## Evaluación")

st.write(
    "Seleccione la respuesta que describa mejor la situación actual."
)

with st.form("formulario_evaluacion"):

    st.markdown("### 1. Evaluación de masa mamaria")

    bulto_nuevo = st.radio(
        "¿Ha notado un bulto o engrosamiento nuevo en la mama?",
        ["No", "Sí"],
        horizontal=True
    )

    if bulto_nuevo == "Sí":

        duro_fijo = st.radio(
            "¿El bulto se siente duro o parece estar fijo?",
            ["No", "Sí"],
            horizontal=True
        )

    else:

        duro_fijo = "No"

        st.caption(
            "La evaluación de dureza o fijación no se aplica "
            "porque no se reportó un bulto nuevo."
        )

    st.divider()

    st.markdown("### 2. Evaluación de piel y pezón")

    cambio_piel = st.radio(
        "¿Ha observado cambios recientes en la piel de la mama "
        "como hundimientos, hoyuelos o aspecto de piel de naranja?",
        ["No", "Sí"],
        horizontal=True
    )

    retraccion_pezon = st.radio(
        "¿Ha notado retracción o hundimiento reciente del pezón?",
        ["No", "Sí"],
        horizontal=True
    )

    st.divider()

    st.markdown("### 3. Signos asociados")

    secrecion_sanguinolenta = st.radio(
        "¿Presenta secreción sanguinolenta por el pezón?",
        ["No", "Sí"],
        horizontal=True
    )

    ganglios = st.radio(
        "¿Ha notado un bulto o ganglio en la axila "
        "o cerca de la clavícula?",
        ["No", "Sí"],
        horizontal=True
    )

    st.write("")

    evaluar = st.form_submit_button(
        "🔎 Evaluar signos",
        use_container_width=True
    )


# =========================================================
# MOTOR DE INFERENCIA
# =========================================================

if evaluar:

    masa_mamaria, regla_masa = determinar_masa_mamaria(
        bulto_nuevo,
        duro_fijo
    )

    alteraciones_piel_pezon, regla_piel = (
        determinar_alteraciones_piel_pezon(
            cambio_piel,
            retraccion_pezon
        )
    )

    signos_asociados, regla_signos = (
        determinar_signos_asociados(
            secrecion_sanguinolenta,
            ganglios
        )
    )

    nivel, recomendacion, regla_final = determinar_nivel_atencion(
        masa_mamaria,
        alteraciones_piel_pezon,
        signos_asociados
    )

    st.divider()

    st.markdown("## Resultado del Sistema Experto")

    # =====================================================
    # RESULTADO PRINCIPAL
    # =====================================================

    if nivel == 1:

        st.markdown(
            f"""
            <div class="result-level-1">

            <h3>🔴 Nivel 1</h3>

            <strong>{recomendacion}</strong>

            <p>
            El motor de inferencia identificó uno o más
            factores clasificados como prioritarios dentro
            de la base de conocimiento.
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )

    elif nivel == 2:

        st.markdown(
            f"""
            <div class="result-level-2">

            <h3>🟠 Nivel 2</h3>

            <strong>{recomendacion}</strong>

            <p>
            Se identificó una masa mamaria sin otros signos
            prioritarios contemplados por el sistema.
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )

    else:

        st.markdown(
            f"""
            <div class="result-level-3">

            <h3>🟢 Nivel 3</h3>

            <strong>{recomendacion}</strong>

            <p>
            Las respuestas no activaron las reglas de alarma
            definidas en la base de conocimiento.
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )

    st.write("")

    # =====================================================
    # FACTORES INFERIDOS
    # =====================================================

    st.markdown("### Factores obtenidos")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "Masa mamaria",
            masa_mamaria
        )

    with c2:
        st.metric(
            "Alteraciones piel/pezón",
            alteraciones_piel_pezon
        )

    with c3:
        st.metric(
            "Signos asociados",
            signos_asociados
        )

    # =====================================================
    # EXPLICACIÓN DE INFERENCIA
    # =====================================================

    with st.expander(
        "🧠 Ver razonamiento del Sistema Experto"
    ):

        st.markdown("#### Hechos proporcionados")

        st.write(
            f"**Bulto nuevo:** {bulto_nuevo}"
        )

        st.write(
            f"**Duro o fijo:** {duro_fijo}"
        )

        st.write(
            f"**Cambios en piel:** {cambio_piel}"
        )

        st.write(
            f"**Retracción del pezón:** {retraccion_pezon}"
        )

        st.write(
            f"**Secreción sanguinolenta:** "
            f"{secrecion_sanguinolenta}"
        )

        st.write(
            f"**Ganglios:** {ganglios}"
        )

        st.divider()

        st.markdown("#### Inferencias realizadas")

        st.write(
            f"**{regla_masa}:** "
            f"Masa mamaria → {masa_mamaria}"
        )

        st.write(
            f"**{regla_piel}:** "
            f"Alteraciones de piel o pezón → "
            f"{alteraciones_piel_pezon}"
        )

        st.write(
            f"**{regla_signos}:** "
            f"Signos asociados → {signos_asociados}"
        )

        st.write(
            f"**{regla_final}:** "
            f"Nivel de atención → Nivel {nivel}"
        )

    # =====================================================
    # REGLAS DE LA BASE DE CONOCIMIENTO
    # =====================================================

    with st.expander(
        "📚 Ver reglas de la base de conocimiento"
    ):

        st.code(
"""
RULE 1
IF bulto_nuevo = si AND duro_fijo = si
THEN masa_mamaria = prioritaria;

RULE 2
IF bulto_nuevo = si AND duro_fijo = no
THEN masa_mamaria = presente;

RULE 3
IF bulto_nuevo = no
THEN masa_mamaria = ausente;

RULE 4
IF cambio_piel = si OR retraccion_pezon = si
THEN alteraciones_piel_pezon = si;

RULE 5
IF cambio_piel = no AND retraccion_pezon = no
THEN alteraciones_piel_pezon = no;

RULE 6
IF secrecion_sanguinolenta = si OR ganglios = si
THEN signos_asociados = si;

RULE 7
IF secrecion_sanguinolenta = no AND ganglios = no
THEN signos_asociados = no;

RULE 8
IF masa_mamaria = prioritaria OR
   alteraciones_piel_pezon = si OR
   signos_asociados = si
THEN nivel_atencion = nivel_1;

RULE 9
IF masa_mamaria = presente AND
   alteraciones_piel_pezon = no AND
   signos_asociados = no
THEN nivel_atencion = nivel_2;

RULE 10
IF masa_mamaria = ausente AND
   alteraciones_piel_pezon = no AND
   signos_asociados = no
THEN nivel_atencion = nivel_3;
""",
            language="text"
        )


# =========================================================
# PIE DE PÁGINA
# =========================================================

st.divider()

st.markdown(
    """
    <div style="
        text-align:center;
        color:#667085;
        font-size:0.85rem;
        padding:1rem;
    ">
        Sistema Experto académico basado en reglas IF–THEN<br>
        Especialidad: Oncología · Área: Oncología Mamaria
    </div>
    """,
    unsafe_allow_html=True
)
