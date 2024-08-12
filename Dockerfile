# Utiliza una imagen base de Python
FROM python:3.9

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos de tu proyecto al contenedor
COPY . /app

# Instala las dependencias desde el archivo requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto que usará Streamlit
EXPOSE 8501

# Define el comando de inicio para Streamlit
CMD ["streamlit", "run", "main"]
