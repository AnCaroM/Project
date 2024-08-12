import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Función para cada sección
def Modelo_logistico():
    st.title('Simulación del Modelo Logístico de Crecimiento Poblacional')

    r = st.slider('Tasa de crecimiento máximo (r)', 0.0, 1.0, 0.5, step=0.01)
    K = st.slider('Capacidad de carga (K)', 100, 1000, 500, step=50)
    P0 = st.slider('Población inicial (P0)', 1, 100, 10)
    periodos = st.slider('Número de períodos', 1, 100, 20)

    P = [P0]

    for t in range(1, periodos + 1):
        Pt = P[-1] + r * P[-1] * (1 - P[-1] / K)
        P.append(Pt)

    st.subheader('Gráfica del Crecimiento Poblacional')
    fig, ax = plt.subplots()
    ax.plot(range(periodos + 1), P, marker='o')
    ax.set_title('Crecimiento poblacional usando el modelo logístico')
    ax.set_xlabel('Períodos')
    ax.set_ylabel('Población')
    ax.grid(True)
    # Mostrar la gráfica en la aplicación
    st.pyplot(fig)
    #Tabla
    st.subheader('Resultados')
    resultados = {'Población': P}
    st.write(resultados)


def Modelo_exponencial():
    st.title('Simulación del Modelo Exponencial de Crecimiento Poblacional')

    # Parámetros de entrada
    r = st.slider('Tasa de crecimiento (r)', 0.0, 1.0, 0.2, step=0.01)
    P0 = st.slider('Población inicial (P0)', 1, 100, 10)
    periodos = st.slider('Número de períodos', 1, 100, 20)

    # Lista para almacenar los valores de la población
    P = [P0]

    # Simulación de los períodos
    for t in range(1, periodos + 1):
        Pt = P[-1] * (1 + r)
        P.append(Pt)
    # Graficar los resultados
    st.subheader('Gráfica del Crecimiento Poblacional')
    fig, ax = plt.subplots()
    ax.plot(range(periodos + 1), P, marker='o')
    ax.set_title('Crecimiento poblacional usando el modelo exponencial')
    ax.set_xlabel('Períodos')
    ax.set_ylabel('Población')
    ax.grid(True)
    st.pyplot(fig)

    # Mostrar los resultados
    st.subheader('Resultados')
    resultados = {'Población': P}
    st.write(resultados)

def Modelo_mathusiano():
    st.title('Simulación del Modelo Malthusiano de Crecimiento Poblacional con Inmigración')

    # Parámetros de entrada
    r = st.slider('Tasa de crecimiento (r)', 0.0, 1.0, 0.2, step=0.01)
    I = st.slider('Tasa de inmigración (I)', 0, 100, 10, step=1)
    P0 = st.slider('Población inicial (P0)', 1, 100, 10)
    periodos = st.slider('Número de períodos', 1, 100, 20)

    # Lista para almacenar los valores de la población
    P = [P0]

    # Simulación de los períodos
    for t in range(1, periodos + 1):
        Pt = P[-1] + r * P[-1] + I
        P.append(Pt)

    # Graficar los resultados
    st.subheader('Gráfica del Crecimiento Poblacional con Inmigración')
    fig, ax = plt.subplots()
    ax.plot(range(periodos + 1), P, marker='o')
    ax.set_title('Crecimiento poblacional con inmigración usando el modelo Malthusiano')
    ax.set_xlabel('Períodos')
    ax.set_ylabel('Población')
    ax.grid(True)

    # Mostrar la gráfica en la aplicación
    st.pyplot(fig)

    # Mostrar los resultados en una tabla
    st.subheader('Resultados')
    resultados = {'Población': P}
    st.write(resultados)

def Modelo_rickert():
    # Título de la aplicación
    st.title('Simulación del Modelo de Crecimiento de Rickert')

    # Parámetros de entrada
    r = st.slider('Tasa de crecimiento (r)', 0.0, 1.0, 0.2, step=0.01)
    K = st.slider('Capacidad de carga (K)', 100, 1000, 500, step=50)
    m = st.slider('Parámetro de saturación (m)', 0.1, 10.0, 2.0, step=0.1)
    P0 = st.slider('Población inicial (P0)', 1, 100, 10)
    periodos = st.slider('Número de períodos', 1, 100, 20)

    # Lista para almacenar los valores de la población
    P = [P0]

    # Simulación de los períodos
    for t in range(1, periodos + 1):
        Pt = P[-1] + r * P[-1] * (1 - (P[-1] / K)**m)
        Pt = max(Pt, 0)  # La población no puede ser negativa
        P.append(Pt)

    # Graficar los resultados
    st.subheader('Gráfica del Crecimiento Poblacional')
    fig, ax = plt.subplots()
    ax.plot(range(periodos + 1), P, marker='o')
    ax.set_title('Crecimiento poblacional usando el modelo de Rickert')
    ax.set_xlabel('Períodos')
    ax.set_ylabel('Población')
    ax.grid(True)
    st.pyplot(fig)
    # Mostrar los resultados en una tabla
    st.subheader('Resultados')
    resultados = {'Población': P}
    st.write(resultados)

def Modelo_verhults():
    # Título de la aplicación
    st.title('Simulación del Modelo de Crecimiento de Verhulst')

    # Parámetros de entrada
    r = st.slider('Tasa de crecimiento (r)', 0.0, 1.0, 0.2, step=0.01)
    K = st.slider('Capacidad de carga (K)', 100, 1000, 500, step=50)
    P0 = st.slider('Población inicial (P0)', 1, 100, 10)
    periodos = st.slider('Número de períodos', 1, 100, 20)
    P = [P0]
    # Simulación de los períodos usando la fórmula de Verhulst
    for t in range(1, periodos + 1):
        Pt = K / (1 + (K - P0) / P0 * np.exp(-r * t))
        P.append(Pt)
    # Graficar los resultados
    st.subheader('Gráfica del Crecimiento Poblacional')
    fig, ax = plt.subplots()
    ax.plot(range(periodos + 1), P, marker='o')
    ax.set_title('Crecimiento poblacional usando el modelo de Verhulst')
    ax.set_xlabel('Períodos')
    ax.set_ylabel('Población')
    ax.grid(True)
    st.pyplot(fig)
    # Mostrar los resultados en una tabla
    st.subheader('Resultados')
    resultados = {'Población': P}
    st.write(resultados)

def Modelo_gompertz():
    st.title('Simulación del Modelo de Crecimiento de Gompertz')
    # Parámetros de entrada
    r = st.slider('Tasa de crecimiento (r)', 0.0, 1.0, 0.2, step=0.01)
    K = st.slider('Capacidad de carga (K)', 100, 1000, 500, step=50)
    P0 = st.slider('Población inicial (P0)', 1, 100, 10)
    periodos = st.slider('Número de períodos', 1, 100, 20)
    P = [P0]
    # Simulación de los períodos usando la fórmula de Gompertz
    for t in range(1, periodos + 1):
        Pt = K * np.exp(-np.exp(r * (t - np.log(K / P0))))
        P.append(Pt)
    # Graficar los resultados
    st.subheader('Gráfica del Crecimiento Poblacional')
    fig, ax = plt.subplots()
    ax.plot(range(periodos + 1), P, marker='o')
    ax.set_title('Crecimiento poblacional usando el modelo de Gompertz')
    ax.set_xlabel('Períodos')
    ax.set_ylabel('Población')
    ax.grid(True)
    st.pyplot(fig)
    # Mostrar los resultados en una tabla
    st.subheader('Resultados')
    resultados = {'Población': P}
    st.write(resultados)



# Crear el menú en la barra lateral
menu = st.sidebar.selectbox("Modelos", ["Modelo Logistico", "Modelo Exponencial", "Modelo Mathusiano", "Modelo Rickert", "Modelo Verhults", "Modelo Gompertz"])

# Mostrar la sección seleccionada
if menu == "Modelo Logistico":
    Modelo_logistico()
elif menu == "Modelo Exponencial":
    Modelo_exponencial()
elif menu == "Modelo Mathusiano":
    Modelo_mathusiano()
elif menu == "Modelo Rickert":
    Modelo_rickert()
elif menu == "Modelo Verhults":
    Modelo_verhults()
elif menu == "Modelo Gompertz":
    Modelo_gompertz()
