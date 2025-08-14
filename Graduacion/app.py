import streamlit as st
import joblib
import numpy as np

# -------------------------------
# Cargar el modelo entrenado
# -------------------------------
modelo_entrenado = joblib.load("primermillon.joblib")

# -------------------------------
# Configuración de la página
# -------------------------------
st.set_page_config(
    page_title="Predictor de Éxito Académico",
    page_icon="🎓",
    layout="centered"
)

# -------------------------------
# TÍTULO Y AUTOR
# -------------------------------
st.title("🎓 Predictor de Éxito Académico")
st.subheader("Autor: Leandro Fiayo")

# -------------------------------
# IMAGEN DECORATIVA
# -------------------------------
st.image(
    "https://img2.pngtree.com/png-clipart/20230801/original/pngtree-cartoon-creative-boy-graduation-illustration-png-image_9093064.png",
    use_container_width=True
)

# -------------------------------
# INSTRUCCIONES
# -------------------------------
st.markdown("""
### 🧪 ¿Cómo usar esta aplicación?

1. Ajusta los deslizadores para ingresar la **Nota IA** y el **GPA** del estudiante (valores entre 0 y 1, con incrementos de 0.1).
2. Haz clic en el botón **"🔍 Predecir"** para obtener una predicción.
3. Recibirás un mensaje que indica si el estudiante **se graduará con éxito o no**.
""")

# -------------------------------
# ENTRADA DE DATOS CON SLIDERS
# -------------------------------
nota_ia = st.slider("📊 Nota IA", 0.0, 1.0, 0.5, step=0.1)
gpa = st.slider("📈 GPA", 0.0, 1.0, 0.5, step=0.1)

# -------------------------------
# BOTÓN DE PREDICCIÓN
# -------------------------------
if st.button("🔍 Predecir"):
    # Preparar los datos
    entrada = np.array([[nota_ia, gpa]])
    
    # Hacer predicción
    prediccion = modelo_entrenado.predict(entrada)[0]
    
    # Mostrar resultado
    if prediccion == 1:
        st.success("🎉 ¡Felicitaciones! Te vas a graduar con honores. 🎓")
    else:
        st.error("❌ No se graduará. Sigue esforzándote. 😔")

# -------------------------------
# PIE DE PÁGINA
# -------------------------------
st.markdown("---")
st.markdown("© 2025 Leandro Fiayo")
