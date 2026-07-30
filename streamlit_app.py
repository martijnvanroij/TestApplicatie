import streamlit as st

from CoolProp.CoolProp import PropsSI

 

st.set_page_config(page_title="Hydrogen Tank Mass Calculator", page_icon="🧪")

 

st.title("Hydrogen Tank Mass Calculator")

st.write("Calculate hydrogen mass in a tank using CoolProp.")

 

st.subheader("Inputs")

 

temperature = st.number_input(

    "Temperature [K]",

    min_value=1.0,

    value=300.0,

    step=1.0

)

 

pressure_bar = st.number_input(

    "Pressure [bar]",

    min_value=0.001,

    value=100.0,

    step=1.0

)

 

volume = st.number_input(

    "Tank Volume [m³]",

    min_value=0.000001,

    value=0.1,

    step=0.01,

    format="%.6f"

)

 

pressure_pa = pressure_bar * 1e5

 

try:

   density = PropsSI("D", "T", temperature, "P", pressure_pa, "Hydrogen")

   mass = density * volume

 

   st.subheader("Output")

   st.metric("Hydrogen Mass in Tank [kg]", f"{mass:.6f}")



   with st.expander("Calculation details"):

    st.write(f"Temperature: {temperature:.2f} K")

    st.write(f"Pressure: {pressure_bar:.2f} bar ({pressure_pa:.2f} Pa)")

    st.write(f"Volume: {volume:.6f} m³")

    st.write(f"Density from CoolProp: {density:.6f} kg/m³")

    st.write(f"Mass = Density × Volume = {mass:.6f} kg")

 

except Exception as e:

    st.error("Calculation failed. Please check the input values.")

    st.exception(e)