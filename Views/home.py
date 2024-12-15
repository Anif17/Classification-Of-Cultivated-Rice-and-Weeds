import streamlit as st
from PIL import Image

# Set page config (optional)
st.set_page_config(page_title="AgriVision: Smart Crop & Weeds Classifier", layout="wide",page_icon="🌾")

st.markdown(
    """
    <style>
    .reportview-container {
        background-color: #f0f0f0; /* Light gray background */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Display Title and Subtitle
st.image(r"Images/home.png", width=300)
st.title("Paddy & Weeds Classifier")

st.sidebar.success("Select a page below.")

# Catchy tagline
st.subheader(
    "**Welcome to the Classification of Cultivated Rice & Weeds Application!**  \n"
    "This application utilizes a ResNet-50 model to accurately classify cultivated rice with other weeds into three categories:  \n"

)

# Create a three-column layout for categories
col1, col2, col3 = st.columns(3)

# Define images and titles for categories
categories = [
    {"title": "Cultivated Rice", "image": r"Images/cultivated_rice.jpeg"},
    {"title": "Weedy Rice", "image": r"Images/weedy_rice.png"},
    {"title": "Barnyard Grass", "image": r"Images/barnyard_grass.jpg"},
]

# Populate columns with images and titles
with col1:
    st.image(categories[0]["image"], width=300)
    st.subheader(categories[0]["title"])

with col2:
    st.image(categories[1]["image"], width=300)
    st.subheader(categories[1]["title"])

with col3:
    st.image(categories[2]["image"], width=300)
    st.subheader(categories[2]["title"])

st.write("Utilize this tool to swiftly and accurately classify your images of cultivated rice and weeds, enhancing your agricultural efficiency.")


# HTML button styled link
st.markdown(
    """
    <style>
    .custom-button {
        display: inline-block;
        padding: 10px 20px;
        font-size: 16px;
        color: white;  /* Text color set to white */
        background-color: #cccccf;  /* Background color */
        border: none;
        border-radius: 5px;
        text-align: center;
        text-decoration: none;  
        cursor: pointer;
    }
    .custom-button:hover {
        background-color: #b7b7ba;  /* Darker color on hover */
    }
    </style>
    <a href="/prediction" class="custom-button" target="_self">Start Classifying</a>
    """,
    unsafe_allow_html=True
)

