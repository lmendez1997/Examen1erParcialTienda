import streamlit as st
import pandas as pd
from datetime import date

st.set_page_config(page_title="Examen I Parcial - Tienda Electrodomésticos")

st.title("🛒 Examen I Parcial - Tienda de Electrodomésticos")

productos = [
    {"Nombre": "Refrigeradora", "Categoria": "Línea Blanca", "Precio": 18500},
    {"Nombre": "Lavadora", "Categoria": "Línea Blanca", "Precio": 12500},
    {"Nombre": "Microondas", "Categoria": "Cocina", "Precio": 3200},
    {"Nombre": "Licuadora", "Categoria": "Cocina", "Precio": 1800},
    {"Nombre": "Aire Acondicionado", "Categoria": "Climatización", "Precio": 9500},
    {"Nombre": "Plancha", "Categoria": "Hogar", "Precio": 950},
    {"Nombre": "Televisor", "Categoria": "Entretenimiento", "Precio": 14500},
    {"Nombre": "Cafetera", "Categoria": "Cocina", "Precio": 2100},
]

df_productos = pd.DataFrame(productos)
st.subheader("📦 Catálogo de Productos")
st.dataframe(df_productos)
st.subheader("🔎 Filtro por Precio")

precio_max = st.slider(
    "Mostrar productos hasta:",
    min_value=0,
    max_value=20000,
    value=20000,
    step=500
)

df_filtrado = df_productos[df_productos["Precio"] <= precio_max]

st.write("Productos filtrados:")
st.table(df_filtrado)

st.subheader("🛍 Selección de Producto")

producto_seleccionado = st.selectbox(
    "Seleccione un producto:",
    df_filtrado["Nombre"]
)

producto_info = df_productos[df_productos["Nombre"] == producto_seleccionado].iloc[0]
precio_unitario = producto_info["Precio"]

st.write(f"Precio unitario: L {precio_unitario:,.2f}")

cantidad = st.number_input(
    "Cantidad:",
    min_value=1,
    step=1
)

subtotal = precio_unitario * cantidad

st.write(f"Subtotal del producto: L {subtotal:,.2f}")
st.subheader("👤 Datos del Cliente")

nombre_cliente = st.text_input("Nombre del cliente")
rtn = st.text_input("RTN / Identidad")
fecha_factura = st.date_input("Fecha", value=date.today())

st.subheader("🧾 Resumen de Facturación")

if st.button("Generar Factura"):

    isv = subtotal * 0.15
    total = subtotal + isv

    st.write("### Detalle de Compra")
    detalle = pd.DataFrame({
        "Producto": [producto_seleccionado],
        "Cantidad": [cantidad],
        "Precio Unitario": [precio_unitario],
        "Subtotal": [subtotal]
    })

    st.table(detalle)

    st.write("### Cálculos Finales")
    st.write(f"Subtotal General: L {subtotal:,.2f}")
    st.write(f"ISV (15%): L {isv:,.2f}")
    st.write(f"Total a Pagar: L {total:,.2f}")

    st.success("Factura generada correctamente ✅")
