# 🚀 Guía Rápida: Cómo Ejecutar el Proyecto

## ✅ Pre-requisitos
- Python 3.8+ instalado
- Entorno virtual configurado
- Archivos del proyecto clonados

---

## 🎯 Pasos para Ejecutar

### 1️⃣ Activar el Entorno Virtual

**Windows:**
```bash
.venv\Scripts\activate
```

**Mac/Linux:**
```bash
source .venv/bin/activate
```

### 2️⃣ Instalar/Actualizar Dependencias
```bash
pip install -r requirements.txt
```

### 3️⃣ Ejecutar la Aplicación
```bash
streamlit run Inicio.py
```

Se abrirá automáticamente en tu navegador (http://localhost:8501)

---

## 📊 Cómo Usar la Aplicación

### En la Página "Análisis Exploratorio"
1. **Selecciona un CSV** desde la lista desplegable o carga uno nuevo
2. **Observa la vista previa** de las primeras 10 filas
3. **Revisa la estructura** (número de filas, columnas, tipos)
4. **Analiza calidad** de datos (valores faltantes)
5. **Explora estadísticas** numéricas y categóricas

### En la Página "Resultados"
1. **Completa el formulario** con tus hallazgos
2. **Genera el reporte** haciendo clic en el botón
3. **Descarga** el archivo Markdown (.md)

---

## 🐛 Solución de Problemas

### Error: "ModuleNotFoundError: No module named 'streamlit'"
```bash
pip install streamlit pandas numpy
```

### Error: "No such file or directory: 'Inicio.py'"
Asegúrate de estar en la carpeta correcta:
```bash
cd cesde_ntp_EDA
```

### Error: "Port 8501 already in use"
```bash
streamlit run Inicio.py --server.port 8502
```

---

## 📝 Verificar Proyecto

Para verificar que todo esté configurado correctamente:
```bash
python verificar_proyecto.py
```

---

## 💡 Consejos
- Prueba con el dataset incluido primero
- Lee los tips ("💡") en la aplicación
- Completa todas las secciones del formulario para generar reporte
- Los reportes se descargan en formato Markdown

---

## 📞 Ayuda
Si encuentras problemas, verifica:
1. ✓ Python versión 3.8+
2. ✓ Entorno virtual activado
3. ✓ Dependencias instaladas (`pip list`)
4. ✓ Archivo CSV con formato válido

---

*¡Éxito con tu análisis de datos!* 🎉
