import streamlit as st
from datetime import datetime

# Configuración de la página
st.set_page_config(
    page_title="Resultados - Análisis Exploratorio",
    page_icon="📝",
    layout="wide"
)

st.title("📝 Plantilla de Entrega: Resultados del EDA")
st.markdown("""
### Instrucciones
Utiliza esta página para documentar tus hallazgos observados en la pestaña de **Análisis Exploratorio de Datos**. 
Complete cada sección de forma clara y concisa.
""")

st.divider()

# --- Formulario de Resultados ---
st.header("📋 Formulario de Análisis")

with st.form("form_resultados"):
    st.subheader("🔍 1. Identificación y Contexto")
    contexto = st.text_area(
        "¿De qué se trata el dataset? ¿Cuál es su origen y propósito?",
        placeholder="Ej: El dataset contiene registro de accidentes de tránsito en Colombia durante 2023, con información detallada sobre ubicación, tipo de accidente, participantes y circunstancias...",
        height=100
    )

    st.subheader("❗ 2. Calidad de los Datos")
    calidad = st.text_area(
        "¿Qué encontraste sobre datos faltantes y limpieza?",
        placeholder="Ej: El dataset está completo sin valores nulos. Se observó coherencia en los tipos de datos (fechas, números, categorías)...",
        height=100
    )

    st.subheader("📈 3. Hallazgos Estadísticos Clave")
    estadisticas = st.text_area(
        "¿Cuáles son los números y categorías más relevantes?",
        placeholder="Ej: El promedio de edad es 35 años. La categoría más frecuente es 'Choque'. Se observa mayor ocurrencia en zonas urbanas frente a rurales...",
        height=100
    )

    st.subheader("💡 4. Conclusión Final")
    conclusion = st.text_area(
        "¿Cuál es el mensaje principal de los datos?",
        placeholder="Ej: Los datos revelan una alta concentración de accidentes en períodos nocturnos, especialmente con conductores bajo influencia del alcohol...",
        height=80
    )
    
    # Botón de envío
    enviado = st.form_submit_button("✅ Generar Reporte", use_container_width=True)

# --- Generación de Reporte ---
if enviado:
    if contexto and calidad and estadisticas and conclusion:
        st.divider()
        st.success("✅ Reporte Generado Exitosamente")
        
        fecha_reporte = datetime.now().strftime("%d/%m/%Y %H:%M")
        
        reporte_md = f"""# Reporte de Análisis Exploratorio de Datos (EDA)

**Fecha de Generación:** {fecha_reporte}

---

## 1️⃣ Identificación y Contexto

{contexto}

---

## 2️⃣ Calidad de los Datos

{calidad}

---

## 3️⃣ Hallazgos Estadísticos Clave

{estadisticas}

---

## 4️⃣ Conclusión Final

{conclusion}

---

*Generado por el módulo de Análisis Exploratorio - Proyecto Integrador*
"""
        
        st.markdown("### 📄 Vista Previa del Reporte")
        st.markdown(reporte_md)
        
        st.divider()
        st.subheader("📥 Descargar Reporte")
        st.download_button(
            label="📥 Descargar como Markdown (.md)",
            data=reporte_md,
            file_name=f"reporte_eda_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md",
            mime="text/markdown",
            use_container_width=True
        )
    else:
        st.error("❌ Por favor, completa todas las secciones antes de generar el reporte.")

# --- Barra Lateral ---
with st.sidebar:
    st.markdown("---")
    st.subheader("💡 Consejos para el Análisis")
    st.markdown("""
    - Sé específico con números y porcentajes
    - Relaciona hallazgos entre secciones
    - Interpreta más allá de solo estadística
    - Proporciona contexto para tus conclusiones
    """)
    
    st.markdown("---")
    st.markdown("© 2026 - Proyecto Integrador de Analítica")
