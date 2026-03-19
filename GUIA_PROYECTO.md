# 📝 Proyecto Integrador: Analítica de Datos con Streamlit y Pandas

## 🏢 Información General
*   **Tipo de Trabajo:** Grupal.
*   **Objetivo:** Desarrollar una aplicación web interactiva que permita realizar un Análisis Exploratorio de Datos (EDA) sobre un conjunto de datos seleccionado por el grupo, documentar los resultados y desplegar el código en GitHub.

---

## 🛠️ Fase 1: Configuración del Entorno Virtual (LIDER DE GRUPO)
El **Líder del Grupo** debe iniciar el proyecto localmente. Los integrantes se unirán más tarde mediante el repositorio.

1.  **Crear carpeta del proyecto:**
    ```bash
    mkdir proyecto_analitica
    cd proyecto_analitica
    ```
2.  **Crear entorno virtual:**
    ```bash
    python -m venv .venv
    ```
3.  **Activar entorno virtual:**
    *   **Windows:** `.venv\Scripts\activate`
    *   **Mac/Linux:** `source .venv/bin/activate`
4.  **Instalar dependencias:**
    ```bash
    pip install streamlit pandas
    pip freeze > requirements.txt
    ```

---

## 🏗️ Fase 2: Estructura del Proyecto
El proyecto debe seguir la siguiente estructura de carpetas para habilitar la navegación multipágina de Streamlit:

```text
proyecto_analitica/
├── Inicio.py                                 # Página de inicio (Portada)
├── pages/                                    # Carpeta para páginas adicionales
│   ├── 1_Análisis Exploratorio de Datos (EDA).py # Módulo de Análisis
│   └── 2_Resultados (EDA).py                 # Plantilla de entrega
├── data/                                     # (Opcional) Carpeta para el dataset CSV
├── .gitignore                                # Archivos que git debe ignorar
└── requirements.txt                          # Lista de librerías necesarias
```

---

## 💻 Fase 3: Implementación del Código

### 1. Página de Inicio (`Inicio.py`)
Debe funcionar como la "cara" del proyecto. Incluye:
*   Título del proyecto.
*   Introducción al problema que están analizando.
*   Objetivos del grupo.
*   Lista de integrantes y sus roles.

### 2. Módulo EDA (`pages/1_Análisis Exploratorio de Datos (EDA).py`)
Utiliza Pandas y Streamlit para:
*   Cargar el archivo CSV mediante `st.file_uploader`.
*   Mostrar una vista previa de los datos (`df.head()`).
*   Mostrar dimensiones, tipos de datos y valores nulos.
*   Presentar estadísticas descriptivas generales.
*   **REGLA:** No usar gráficos, enfocarse en la interpretación numérica y textual.

### 3. Plantilla de Resultados (`pages/2_Resultados (EDA).py`)
Crea un formulario con `st.text_area` para que el grupo redacte sus conclusiones finales basadas en lo observado en la página de EDA.

---

## 🚀 Fase 4: Git y GitHub (Paso del Líder e Integrantes)

> [!IMPORTANT]
> **Solo se debe crear UN repositorio por grupo**, el cual será administrado por el **Líder del Grupo**. Los demás integrantes deben ser agregados como colaboradores.

### Para el Líder:
1.  **Crear archivo `.gitignore`:**
    Crea un archivo llamado `.gitignore` y añade:
    ```text
    .venv/
    __pycache__/
    .streamlit/
    *.csv
    ```
2.  **Inicializar repositorio local:**
    ```bash
    git init
    git add .
    git commit -m "Initial commit: Estructura base del proyecto"
    ```
3.  **Subir a GitHub:**
    *   Crea un repositorio nuevo en GitHub (público).
    *   Conéctalo:
    ```bash
    git remote add origin https://github.com/LIDER_USUARIO/PROYECTO.git
    git branch -M main
    git push -u origin main
    ```
4.  **Agregar Colaboradores:**
    *   En GitHub: `Settings` > `Collaborators` > `Add people`. Agrega a tus compañeros.

### Para los Integrantes:
1.  **Clonar el repositorio:** Una vez que el líder los agregue, clonen el proyecto:
    ```bash
    git clone https://github.com/LIDER_USUARIO/PROYECTO.git
    cd PROYECTO
    ```
2.  **Configurar entorno local:** Sigan los pasos de la Fase 1 (crear `.venv` e instalar `requirements.txt`).
3.  **Colaborar:** Realicen cambios, hagan `commit` y `push` a la rama principal (o usen ramas si conocen el flujo).

---

## 📤 Entregable Final
El grupo debe enviar:
1.  El enlace al repositorio de GitHub.
2.  El archivo de reporte generado por la aplicación (en formato Markdown o PDF).
3.  Una breve demostración de cómo funciona la carga del dataset seleccionado.

**¡Éxitos en su investigación, detectives de datos!** 🕵️‍♂️📊
