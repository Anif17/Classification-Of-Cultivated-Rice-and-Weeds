import streamlit as st

# --- PAGE SETUP ---
home_page = st.Page(
    page="Views/home.py",
    title="Home",
    icon="🏠",
    default=True,
)

prediction_page = st.Page(
    page="Views/prediction.py",
    title="Prediction",
    icon="🔮",
)

history_page = st.Page(
    page="Views/history.py",
    title="History",
    icon="🪶",
)

dataset_page = st.Page(
    page="Views/dataset.py",
    title="Dataset",
    icon="🗂️",
)

detail_page = st.Page(
    page="Views/detail.py",
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