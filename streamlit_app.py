import streamlit as st

# --- PAGE SETUP ---
home_page = st.Page(
    page="views/home.py",
    title="Home",
    icon="🏠",
    default=True,
)

prediction_page = st.Page(
    page="views/prediction.py",
    title="Prediction",
    icon="🔮",
)

history_page = st.Page(
    page="views/history.py",
    title="History",
    icon="🪶",
)

dataset_page = st.Page(
    page="views/dataset.py",
    title="Dataset",
    icon="🗂️",
)

detail_page = st.Page(
    page="views/detail.py",
    title="Detail",
    icon="📝",
)

## --- NAVIGATION SETUP ---
pg = st.navigation({
    "💡 Info": [home_page, detail_page],
    "⚙️ Project": [prediction_page, history_page, dataset_page],
})

st.logo("Images/home.png")

## --- RUN NAVIGATION ---
pg.run()