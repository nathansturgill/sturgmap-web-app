import streamlit as st
import sturgmap.foliumap as sturgmap

st.set_page_config(layout="wide")

markdown = """
A Streamlit map template
<https://github.com/nathansturgill/sturgmap-web-app>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://i.imgur.com/UbOXYAU.png"
st.sidebar.image(logo)

st.title("Interactive Raster Map")

with st.expander("See source code"):
    with st.echo():

       m= sturgmap.Map()
    url = "https://github.com/opengeos/datasets/releases/download/raster/landsat7.tif"
    m.add_raster(url, name='landsat.tif', opacity=0.4)
    m

m.to_streamlit(height=700)
