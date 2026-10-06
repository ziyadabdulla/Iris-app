import streamlit as st


st.set_page_config(
    page_title="Iris Explorer",
    page_icon="🌸",
    layout="wide",
)

pages = [
    st.Page("general.py", title="General Information", icon=":material/info:", default=True),
    st.Page("visualisation.py", title="Visualisations", icon=":material/monitoring:"),
    st.Page("iris.py", title="Species Prediction", icon=":material/local_florist:"),
]

page = st.navigation(pages)
page.run()
