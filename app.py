
import streamlit as st

st.set_page_config(
    page_title="Sistema Experto - Oncología Mamaria",
    page_icon="🩺",
    layout="centered"
)

# -------------------------
# ESTILOS
# -------------------------
st.markdown("""
<style>
.main-title {
    text-align: center;
    font-size: 2rem;
    font-weight: 700;
    margin-bottom: 0.2rem;
}
.sub-title {
    text-align: center;
    color: #555;
    margin-bottom: 1.2rem;
}
.result-box {
    padding: 1rem;
    border-radius: 12px;
    margin-top: 1rem;
}
.small-note {
    font-size: 0.9rem;
    color: #666;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">Sistema Experto de Oncología Mamaria</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="sub-title">Evaluación preliminar de signos de alarma de cáncer de mama</div>',
    unsafe_allow_html=True
)

st.info(
    "Este sistema es un prototipo académico basado en reglas. "
    "No diagnostica cáncer ni reemplaza la evaluación de un profesional de salud."
)

st.divider()

# -------------------------
# FUNCIONES DEL SISTEMA EXPERTO
# -------------------------
def determinar_masa_mamaria(bulto_nuevo, duro_fijo):
    # RULE 1
    if bulto_nuevo == "Sí" and duro_fijo == "Sí":
        return "Prioritaria"

    # RULE 2
    if bulto_nuevo == "Sí" and duro_fijo == "No":
        return "Presente"

    # RULE 3
    return "Ausente"


def determinar_alteraciones_piel_pezon(cambio_piel, retraccion_pezon):
    # RULE 4
    if cambio_piel == "Sí" or retraccion_pezon == "Sí":
        return "Sí"

    # RULE 5
    return "No"


def determinar_signos_asociados(secrecion_sanguinolenta, ganglios):
    # RULE 6
    if secrecion_sanguinolenta == "Sí" or ganglios == "Sí":
        return "Sí"

    # RULE 7
    return "No"


def determinar_nivel_atencion(masa_mamaria, alteraciones_piel_pezon, signos_asociados):
    # RULE 8
    if (
        masa_mamaria == "Prioritaria"
        or alteraciones_piel_pezon == "Sí"
        or signos_asociados == "Sí"
    ):
        return 1, "Evaluación médica prioritaria"

    # RULE 9
    if (
        masa_mamaria == "Presente"
        and alteraciones_piel_pezon == "No"
        and signos_asociados == "No"
    ):
        return 2, "Evaluación médica recomendada"

    # RULE 10
    return 3, "No se identificaron signos de alarma dentro de los criterios evaluados"


# -------------------------
# INTERFAZ
# -------------------------
st.subheader("Datos de evaluación")
st.write("Responda las siguientes preguntas:")

with st.form("formulario_evaluacion"):
    bulto_nuevo = st.radio(
        "1. ¿Ha notado un bulto o engrosamiento nuevo en la mama?",
        ["No", "Sí"],
        horizontal=True
    )

    if bulto_nuevo == "Sí":
        duro_fijo = st.radio(
            "2. ¿El bulto se siente duro o parece estar fijo?",
            ["No", "Sí"],
            horizontal=True
        )
    else:
        duro_fijo = "No"
        st.caption("2. La pregunta sobre dureza o fijación no aplica porque no se reportó un bulto nuevo.")

    cambio_piel = st.radio(
        "3. ¿Ha observado cambios recientes en la piel de la mama, como hundimientos, hoyuelos o aspecto de piel de naranja?",
        ["No", "Sí"],
        horizontal=True
    )

    retraccion_pezon = st.radio(
        "4. ¿Ha notado retracción o hundimiento reciente del pezón?",
        ["No", "Sí"],
        horizontal=True
    )

    secrecion_sanguinolenta = st.radio(
        "5. ¿Presenta secreción sanguinolenta por el pezón?",
        ["No", "Sí"],
        horizontal=True
    )

    ganglios = st.radio(
        "6. ¿Ha notado un bulto o ganglio en la axila o cerca de la clavícula?",
        ["No", "Sí"],
        horizontal=True
    )

    evaluar = st.form_submit_button("Evaluar", use_container_width=True)

# -------------------------
# MOTOR DE INFERENCIA
# -------------------------
if evaluar:
    masa_mamaria = determinar_masa_mamaria(bulto_nuevo, duro_fijo)

    alteraciones_piel_pezon = determinar_alteraciones_piel_pezon(
        cambio_piel,
        retraccion_pezon
    )

    signos_asociados = determinar_signos_asociados(
        secrecion_sanguinolenta,
        ganglios
    )

    nivel, recomendacion = determinar_nivel_atencion(
        masa_mamaria,
        alteraciones_piel_pezon,
        signos_asociados
    )

    st.divider()
    st.subheader("Resultado del Sistema Experto")

    if nivel == 1:
        st.error(f"**Nivel 1 — {recomendacion}**")
        st.write(
            "El sistema identificó uno o más signos considerados prioritarios "
            "dentro de la base de conocimiento del prototipo."
        )

    elif nivel == 2:
        st.warning(f"**Nivel 2 — {recomendacion}**")
        st.write(
            "Se identificó una masa mamaria reportada sin otros signos prioritarios "
            "considerados por este prototipo."
        )

    else:
        st.success(f"**Nivel 3 — {recomendacion}**")
        st.write(
            "Las respuestas proporcionadas no activaron las reglas de alarma definidas "
            "en este Sistema Experto."
        )

    with st.expander("Ver razonamiento del Sistema Experto"):
        st.write(f"**Masa mamaria:** {masa_mamaria}")
        st.write(f"**Alteraciones de piel o pezón:** {alteraciones_piel_pezon}")
        st.write(f"**Signos asociados:** {signos_asociados}")
        st.write(f"**Nivel resultante:** Nivel {nivel}")

        st.markdown("### Reglas aplicadas")
        if masa_mamaria == "Prioritaria":
            st.code("IF bulto_nuevo = si AND duro_fijo = si THEN masa_mamaria = prioritaria;")
        elif masa_mamaria == "Presente":
            st.code("IF bulto_nuevo = si AND duro_fijo = no THEN masa_mamaria = presente;")
        else:
            st.code("IF bulto_nuevo = no THEN masa_mamaria = ausente;")

        if alteraciones_piel_pezon == "Sí":
            st.code("IF cambio_piel = si OR retraccion_pezon = si THEN alteraciones_piel_pezon = si;")
        else:
            st.code("IF cambio_piel = no AND retraccion_pezon = no THEN alteraciones_piel_pezon = no;")

        if signos_asociados == "Sí":
            st.code("IF secrecion_sanguinolenta = si OR ganglios = si THEN signos_asociados = si;")
        else:
            st.code("IF secrecion_sanguinolenta = no AND ganglios = no THEN signos_asociados = no;")

        if nivel == 1:
            st.code(
                "IF masa_mamaria = prioritaria OR "
                "alteraciones_piel_pezon = si OR "
                "signos_asociados = si "
                "THEN nivel_atencion = nivel_1;"
            )
        elif nivel == 2:
            st.code(
                "IF masa_mamaria = presente AND "
                "alteraciones_piel_pezon = no AND "
                "signos_asociados = no "
                "THEN nivel_atencion = nivel_2;"
            )
        else:
            st.code(
                "IF masa_mamaria = ausente AND "
                "alteraciones_piel_pezon = no AND "
                "signos_asociados = no "
                "THEN nivel_atencion = nivel_3;"
            )

st.divider()
st.caption(
    "Proyecto académico — Sistema Experto basado en reglas IF–THEN. "
    "Ante cualquier cambio mamario persistente o preocupante, consulte a un profesional de salud."
)
