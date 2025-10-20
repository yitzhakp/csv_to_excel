import streamlit as st
import pandas as pd
from io import BytesIO

st.title("Convertidor CSV a EXCEL")

def to_excel(df):
  output = BytesIO()
  with pd.ExcelWriter(output, engine="xlsxwriter") as writer:
    df.to_excel(writer, index=False, sheet_name="Resultados")
  processed_data = output.getvalue()
  return processed_data

archivo = st.file_uploader("Sube un archivo CSV", type=["csv"])
if archivo is not None:
  df = pd.read_csv(archivo)
  st.write("📊 Vista previa de los datos:")
  st.dataframe(df)
  st.download_button(
    label="📥 Descargar Excel con resultados",
    data=to_excel(df),
    file_name=f"{archivo.name.split('.', 2)[0]}.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
  )