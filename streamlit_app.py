import streamlit as st 
import pandas as pd 
import altair as alt
df= pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/refs/heads/master/penguins.csv")
df
c = alt.Chart(df).mark_circle().encode(
    x='bill_length_mm',
    y='body_mass_g',
    color='species',
).interactive()

tab1, tab2 = st.tabs(["Streamlit theme (default)", "Altair native theme"])

with tab1:
    # Use the Streamlit theme.
    # This is the default. So you can also omit the theme argument.
    st.altair_chart(c, theme="streamlit", use_container_width=True)
with tab2:
    # Use the native Altair theme.
    st.altair_chart(c, theme=None, use_container_width=True)