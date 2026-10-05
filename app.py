
import streamlit as st

# ============================================================
# CONFIGURACIÓN GENERAL
# ============================================================

st.set_page_config(
    page_title="Sistema Experto | Oncología Mamaria",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# ESTILOS
# ============================================================

st.markdown(
    """
    <style>
        :root {
            color-scheme: light;
        }

        html, body, [data-testid="stAppViewContainer"] {
            background-color: #F6F8FC !important;
            color: #111827 !important;
        }

        [data-testid="stHeader"] {
            background: rgba(246, 248, 252, 0.95) !important;
        }

        [data-testid="stSidebar"] {
            background-color: #FFFFFF !important;
            border-right: 1px solid #E5E7EB;
        }

        [data-testid="stSidebar"] * {
            color: #111827 !important;
        }

        .block-container {
            max-width: 1180px;
            padding-top: 2rem;
            padding-bottom: 3rem;
        }

        h1, h2, h3, h4, h5, h6,
        p, label, span, div {
            color: #111827;
        }

        /* Encabezado principal */
        .hero {
            background: linear-gradient(135deg, #7A1F4D 0%, #A73368 100%);
            border-radius: 20px;
            padding: 2.1rem 2.3rem;
            margin-bottom: 1.5rem;
            box-shadow: 0 12px 30px rgba(122, 31, 77, 0.16);
        }

        .hero .eyebrow {
            color: #FCE7F3 !important;
            font-size: 0.83rem;
            font-weight: 700;
            letter-spacing: 0.08em;
            text-transform: uppercase;
            margin-bottom: 0.5rem;
        }

        .hero .title {
            color: #FFFFFF !important;
            font-size: 2.25rem;
            font-weight: 800;
            line-height: 1.15;
            margin-bottom: 0.45rem;
        }

        .hero .subtitle {
            color: #FDF2F8 !important;
            font-size: 1.02rem;
            line-height: 1.55;
            max-width: 900px;
        }

        /* Tarjetas */
        .card {
            background: #FFFFFF;
            border: 1px solid #E5E7EB;
            border-radius: 16px;
            padding: 1.25rem 1.3rem;
            min-height: 145px;
            box-shadow: 0 4px 16px rgba(17, 24, 39, 0.05);
        }

        .card .kicker {
            color: #7A1F4D !important;
            font-weight: 800;
            font-size: 0.9rem;
            margin-bottom: 0.35rem;
        }

        .card .card-title {
            color: #111827 !important;
            font-size: 1.08rem;
            font-weight: 750;
            margin-bottom: 0.35rem;
        }

        .card .card-text {
            color: #4B5563 !important;
            font-size: 0.94rem;
            line-height: 1.5;
        }

        /* Panel de evaluación */
        .section-box {
            background: #FFFFFF;
            border: 1px solid #E5E7EB;
            border-radius: 16px;
            padding: 1.3rem 1.4rem 0.7rem 1.4rem;
            margin-bottom: 1rem;
        }

        .section-number {
            display: inline-flex;
            width: 30px;
            height: 30px;
            align-items: center;
            justify-content: center;
            border-radius: 50%;
            background: #FCE7F3;
            color: #7A1F4D !important;
            font-weight: 800;
            margin-right: 0.45rem;
        }

        .section-title {
            display: inline;
            color: #111827 !important;
            font-size: 1.12rem;
            font-weight: 800;
        }

        /* Resultado */
        .result {
            border-radius: 16px;
            padding: 1.35rem 1.5rem;
            margin-top: 0.75rem;
            border: 1px solid;
        }

        .result h3 {
            margin: 0 0 0.35rem 0;
        }

        .result p {
            margin: 0.25rem 0 0 0;
            line-height: 1.55;
        }

        .level1 {
            background: #FFF1F2;
            border-color: #FECDD3;
        }
        .level1 h3, .level1 strong {
            color: #9F1239 !important;
        }

        .level2 {
            background: #FFF7ED;
            border-color: #FED7AA;
        }
        .level2 h3, .level2 strong {
            color: #9A3412 !important;
        }

        .level3 {
            background: #ECFDF5;
            border-color: #A7F3D0;
        }
        .level3 h3, .level3 strong {
            color: #065F46 !important;
        }

        /* Etiquetas */
        .tag {
            display: inline-block;
            background: #F3F4F6;
            color: #374151 !important;
            border: 1px solid #E5E7EB;
            border-radius: 999px;
            padding: 0.25rem 0.6rem;
            margin: 0.1rem 0.25rem 0.1rem 0;
            font-size: 0.82rem;
            font-weight: 650;
        }

        /* Texto auxiliar */
        .muted {
            color: #6B7280 !important;
            font-size: 0.92rem;
        }

        /* Botón principal */
        div[data-testid="stFormSubmitButton"] > button {
            width: 100%;
            background: #7A1F4D !important;
            color: #FFFFFF !important;
            border: 1px solid #7A1F4D !important;
            border-radius: 12px !important;
            min-height: 3rem;
            font-weight: 800 !important;
            box-shadow: 0 6px 16px rgba(122, 31, 77, 0.18);
        }

        div[data-testid="stFormSubmitButton"] > button:hover {
            background: #68183F !important;
            border-color: #68183F !important;
        }

        div[data-testid="stFormSubmitButton"] > button p {
            color: #FFFFFF !important;
        }

        /* Radios */
        div[role="radiogroup"] label,
        div[role="radiogroup"] label p,
        div[role="radiogroup"] span {
            color: #111827 !important;
        }

        /* Expander */
        [data-testid="stExpander"] {
            background: #FFFFFF;
            border: 1px solid #E5E7EB;
            border-radius: 12px;
        }

        /* Métricas */
        [data-testid="stMetric"] {
            background: #FFFFFF;
            border: 1px solid #E5E7EB;
            border-radius: 14px;
            padding: 1rem;
        }

        /* Footer */
        .footer {
            text-align: center;
            color: #6B7280 !important;
            font-size: 0.84rem;
            padding: 1rem 0 0.5rem 0;
        }

        /* Oculta menú inferior de Streamlit para presentación */
        footer {
            visibility: hidden;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# ============================================================
# BASE DE CONOCIMIENTO / MOTOR DE INFERENCIA
# ============================================================

def determinar_masa_mamaria(bulto_nuevo: str, duro_fijo: str):
    # RULE 1
    if bulto_nuevo == "Sí" and duro_fijo == "Sí":
        return "Prioritaria", "RULE 1"

    # RULE 2
    if bulto_nuevo == "Sí" and duro_fijo == "No":
        return "Presente", "RULE 2"

    # RULE 3
    return "Ausente", "RULE 3"


def determinar_alteraciones_piel_pezon(cambio_piel: str, retraccion_pezon: str):
    # RULE 4
    if cambio_piel == "Sí" or retraccion_pezon == "Sí":
        return "Sí", "RULE 4"

    # RULE 5
    return "No", "RULE 5"


def determinar_signos_asociados(secrecion_sanguinolenta: str, ganglios: str):
    # RULE 6
    if secrecion_sanguinolenta == "Sí" or ganglios == "Sí":
        return "Sí", "RULE 6"

    # RULE 7
    return "No", "RULE 7"


def determinar_nivel_atencion(
    masa_mamaria: str,
    alteraciones_piel_pezon: str,
    signos_asociados: str
):
    # RULE 8
    if (
        masa_mamaria == "Prioritaria"
        or alteraciones_piel_pezon == "Sí"
        or signos_asociados == "Sí"
    ):
        return 1, "Evaluación médica prioritaria", "RULE 8"

    # RULE 9
    if (
        masa_mamaria == "Presente"
        and alteraciones_piel_pezon == "No"
        and signos_asociados == "No"
    ):
        return 2, "Evaluación médica recomendada", "RULE 9"

    # RULE 10
    return (
        3,
        "No se identificaron signos de alarma dentro de los criterios evaluados",
        "RULE 10"
    )


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:
    st.markdown("## 🩺 Sistema Experto")
    st.caption("Prototipo académico basado en reglas IF–THEN")

    st.markdown("### Especialidad")
    st.write("**Oncología**")

    st.markdown("### Área")
    st.write("**Oncología mamaria**")

    st.markdown("### Objetivo")
    st.write(
        "Realizar una evaluación preliminar de signos de alarma "
        "y generar un nivel de orientación."
    )

    st.divider()

    st.markdown("### Flujo de razonamiento")
    st.write("1. Se recopilan los hechos.")
    st.write("2. Se activan reglas IF–THEN.")
    st.write("3. Se obtienen factores intermedios.")
    st.write("4. Se determina el nivel de atención.")

    st.divider()

    st.warning(
        "Este sistema es académico y orientativo. "
        "No sustituye una consulta médica ni confirma un diagnóstico."
    )


# ============================================================
# CABECERA
# ============================================================

st.markdown(
    """
    <div class="hero">
        <div class="eyebrow">Sistema experto basado en conocimiento</div>
        <div class="title">Evaluación preliminar de signos de alarma mamaria</div>
        <div class="subtitle">
            Prototipo académico que utiliza una base de conocimiento y reglas
            IF–THEN para clasificar signos reportados y determinar un nivel de
            orientación.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# ============================================================
# TARJETAS INFORMATIVAS
# ============================================================

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown(
        """
        <div class="card">
            <div class="kicker">01 · ENTRADAS</div>
            <div class="card-title">Hechos del usuario</div>
            <div class="card-text">
                Se recopilan seis respuestas sobre masa mamaria, cambios de
                piel/pezón y signos asociados.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with c2:
    st.markdown(
        """
        <div class="card">
            <div class="kicker">02 · INFERENCIA</div>
            <div class="card-title">Reglas IF–THEN</div>
            <div class="card-text">
                El motor de inferencia aplica diez reglas para obtener
                conclusiones intermedias y una recomendación final.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with c3:
    st.markdown(
        """
        <div class="card">
            <div class="kicker">03 · SALIDA</div>
            <div class="card-title">Nivel de atención</div>
            <div class="card-text">
                El resultado se clasifica en Nivel 1, Nivel 2 o Nivel 3,
                según las reglas activadas.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.write("")

# ============================================================
# PESTAÑAS
# ============================================================

tab_eval, tab_rules, tab_about = st.tabs(
    ["🧪 Evaluación", "📚 Base de conocimiento", "ℹ️ Acerca del sistema"]
)

# ============================================================
# TAB 1: EVALUACIÓN
# ============================================================

with tab_eval:

    st.markdown("## Evaluación")
    st.markdown(
        '<div class="muted">Responda las preguntas según los signos observados.</div>',
        unsafe_allow_html=True
    )
    st.write("")

    with st.form("formulario_evaluacion"):

        st.markdown(
            """
            <div class="section-box">
                <span class="section-number">1</span>
                <span class="section-title">Masa mamaria</span>
            </div>
            """,
            unsafe_allow_html=True
        )

        bulto_nuevo = st.radio(
            "¿Ha notado un bulto o engrosamiento nuevo en la mama?",
            ["No", "Sí"],
            horizontal=True,
            key="bulto_nuevo"
        )

        if bulto_nuevo == "Sí":
            duro_fijo = st.radio(
                "¿El bulto se siente duro o parece estar fijo?",
                ["No", "Sí"],
                horizontal=True,
                key="duro_fijo"
            )
        else:
            duro_fijo = "No"
            st.caption(
                "La pregunta sobre dureza o fijación no aplica porque "
                "no se reportó un bulto nuevo."
            )

        st.write("")

        st.markdown(
            """
            <div class="section-box">
                <span class="section-number">2</span>
                <span class="section-title">Piel y pezón</span>
            </div>
            """,
            unsafe_allow_html=True
        )

        cambio_piel = st.radio(
            "¿Ha observado cambios recientes en la piel de la mama, como "
            "hundimientos, hoyuelos o aspecto de piel de naranja?",
            ["No", "Sí"],
            horizontal=True,
            key="cambio_piel"
        )

        retraccion_pezon = st.radio(
            "¿Ha notado retracción o hundimiento reciente del pezón?",
            ["No", "Sí"],
            horizontal=True,
            key="retraccion_pezon"
        )

        st.write("")

        st.markdown(
            """
            <div class="section-box">
                <span class="section-number">3</span>
                <span class="section-title">Signos asociados</span>
            </div>
            """,
            unsafe_allow_html=True
        )

        secrecion_sanguinolenta = st.radio(
            "¿Presenta secreción sanguinolenta por el pezón?",
            ["No", "Sí"],
            horizontal=True,
            key="secrecion_sanguinolenta"
        )

        ganglios = st.radio(
            "¿Ha notado un bulto o ganglio en la axila o cerca de la clavícula?",
            ["No", "Sí"],
            horizontal=True,
            key="ganglios"
        )

        st.write("")

        evaluar = st.form_submit_button("🔎 Evaluar signos")

    # --------------------------------------------------------
    # INFERENCIA
    # --------------------------------------------------------

    if evaluar:

        masa_mamaria, regla_masa = determinar_masa_mamaria(
            bulto_nuevo, duro_fijo
        )

        alteraciones_piel_pezon, regla_piel = (
            determinar_alteraciones_piel_pezon(
                cambio_piel, retraccion_pezon
            )
        )

        signos_asociados, regla_signos = determinar_signos_asociados(
            secrecion_sanguinolenta, ganglios
        )

        nivel, recomendacion, regla_final = determinar_nivel_atencion(
            masa_mamaria,
            alteraciones_piel_pezon,
            signos_asociados
        )

        st.divider()
        st.markdown("## Resultado")

        if nivel == 1:
            st.markdown(
                f"""
                <div class="result level1">
                    <h3>🔴 Nivel 1 · Evaluación prioritaria</h3>
                    <strong>{recomendacion}</strong>
                    <p>
                        El motor de inferencia identificó al menos un factor
                        clasificado como prioritario dentro de la base de conocimiento.
                    </p>
                </div>
                """,
                unsafe_allow_html=True
            )

        elif nivel == 2:
            st.markdown(
                f"""
                <div class="result level2">
                    <h3>🟠 Nivel 2 · Evaluación recomendada</h3>
                    <strong>{recomendacion}</strong>
                    <p>
                        Se identificó una masa mamaria reportada sin otros factores
                        prioritarios considerados por el prototipo.
                    </p>
                </div>
                """,
                unsafe_allow_html=True
            )

        else:
            st.markdown(
                f"""
                <div class="result level3">
                    <h3>🟢 Nivel 3 · Sin alarmas activadas</h3>
                    <strong>{recomendacion}</strong>
                    <p>
                        Las respuestas proporcionadas no activaron las reglas
                        de alarma definidas en este sistema experto.
                    </p>
                </div>
                """,
                unsafe_allow_html=True
            )

        st.write("")
        st.markdown("### Factores inferidos")

        m1, m2, m3 = st.columns(3)

        with m1:
            st.metric("Masa mamaria", masa_mamaria)

        with m2:
            st.metric(
                "Alteraciones piel/pezón",
                alteraciones_piel_pezon
            )

        with m3:
            st.metric("Signos asociados", signos_asociados)

        st.write("")

        with st.expander("🧠 Ver razonamiento del Sistema Experto"):

            st.markdown("#### Hechos proporcionados")

            hechos = {
                "Bulto nuevo": bulto_nuevo,
                "Duro o fijo": duro_fijo,
                "Cambio en piel": cambio_piel,
                "Retracción del pezón": retraccion_pezon,
                "Secreción sanguinolenta": secrecion_sanguinolenta,
                "Ganglios": ganglios
            }

            for nombre, valor in hechos.items():
                st.write(f"**{nombre}:** {valor}")

            st.divider()
            st.markdown("#### Inferencias")

            st.write(
                f"**{regla_masa}** → Masa mamaria = **{masa_mamaria}**"
            )
            st.write(
                f"**{regla_piel}** → Alteraciones de piel o pezón = "
                f"**{alteraciones_piel_pezon}**"
            )
            st.write(
                f"**{regla_signos}** → Signos asociados = "
                f"**{signos_asociados}**"
            )
            st.write(
                f"**{regla_final}** → Nivel de atención = **Nivel {nivel}**"
            )

# ============================================================
# TAB 2: BASE DE CONOCIMIENTO
# ============================================================

with tab_rules:

    st.markdown("## Base de conocimiento")
    st.write(
        "El sistema utiliza diez reglas de producción derivadas de las "
        "tablas de decisión."
    )

    st.markdown(
        """
        <span class="tag">Masa mamaria</span>
        <span class="tag">Piel / pezón</span>
        <span class="tag">Signos asociados</span>
        <span class="tag">Nivel de atención</span>
        """,
        unsafe_allow_html=True
    )

    st.write("")

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

# ============================================================
# TAB 3: ACERCA DEL SISTEMA
# ============================================================

with tab_about:

    st.markdown("## Acerca del prototipo")

    st.markdown(
        """
        **Dominio:** Servicios de salud  
        **Especialidad:** Oncología  
        **Área delimitada:** Oncología mamaria  
        **Tipo de sistema:** Sistema Experto basado en reglas  

        El sistema representa conocimiento mediante reglas IF–THEN.
        A partir de los hechos introducidos por el usuario, obtiene tres
        factores intermedios:

        - Masa mamaria.
        - Alteraciones de piel o pezón.
        - Signos asociados.

        Finalmente, esos factores alimentan el motor de inferencia que
        determina el nivel de atención.
        """
    )

    st.warning(
        "Este prototipo no realiza un diagnóstico clínico ni descarta "
        "enfermedades. Su finalidad es exclusivamente académica y orientativa."
    )

# ============================================================
# PIE
# ============================================================

st.divider()
st.markdown(
    """
    <div class="footer">
        Proyecto académico · Sistema Experto basado en reglas IF–THEN<br>
        Oncología · Oncología mamaria
    </div>
    """,
    unsafe_allow_html=True
)
