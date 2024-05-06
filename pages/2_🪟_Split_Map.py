import streamlit as st
import sturgmap.foliumap as sturgmap
import folium
from folium import TileLayer

st.set_page_config(layout="wide")

markdown = """
A Streamlit map template
<https://github.com/nathansturgill/sturgmap-web-app>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://i.imgur.com/UbOXYAU.png"
st.sidebar.image(logo)

st.title("Split-panel Map")

with st.expander("See source code"):
    with st.echo():
       m= sturgmap.Map([30, 20], zoom=4)
    layer_left = folium.TileLayer('cartodbpositron')
    layer_right = folium.TileLayer('openstreetmap')

    m.add_side_by_side_layers(layer_left, layer_right)

    m
m.to_streamlit(height=700)
