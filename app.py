import pandas as pd
import plotly.express as px
import streamlit as st

# Leer los datos
car_data = pd.read_csv('vehicles_us.csv')

# Crear botones
hist_button = st.button('Construir histograma')  # Botón para el histograma
scatter_button = st.button('Construir gráfico de dispersión')  # Botón para el gráfico de dispersión

# Acción al hacer clic en el botón de histograma
if hist_button:
    # Escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    
    # Crear un histograma
    fig = px.histogram(car_data, x="odometer")
    
    # Mostrar el gráfico interactivo
    st.plotly_chart(fig, use_container_width=True)

# Acción al hacer clic en el botón de gráfico de dispersión
if scatter_button:
    # Escribir un mensaje
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    
    # Crear un gráfico de dispersión (scatter plot)
    fig_scatter = px.scatter(car_data, x="odometer", y="price", title="Gráfico de dispersión: Odometer vs. Price")
    
    # Mostrar el gráfico interactivo
    st.plotly_chart(fig_scatter, use_container_width=True)

    