import os
import streamlit as st
from PIL import Image
import gdown

st.set_page_config(page_title="AgriVision: Smart Crop & Weeds Classifier", layout="wide", page_icon="🌾")

st.title("🍃Dataset Classification for Cultivated Rice and Weeds")
st.subheader("🗂️ A Comprehensive Collection of Cultivated Rice and Weeds Images")

GDRIVE_FILE_ID_PIC = '1rbhcx2uxwfqRjr28m-HiyupaB-sglvbq'
GDRIVE_URL = f'https://drive.google.com/uc?id={GDRIVE_FILE_ID_PIC}&export=download'
 # Replace with your Google Drive URL

@st.cache_resource
def download_and_extract_zip():
    output = 'dataset.zip'  # Temporary file name for the downloaded zip
    st.write("Downloading dataset...")
    gdown.download(GDRIVE_URL, output, quiet=False)
    
    # Check if the file is downloaded
    if os.path.exists(output):
        st.write("Dataset downloaded successfully.")
    else:
        st.write("Failed to download dataset.")
    
    # Extract the dataset
    import zipfile
    extract_dir = "extracted_dataset"  # Define your extraction directory
    with zipfile.ZipFile(output, 'r') as zip_ref:
        zip_ref.extractall(extract_dir)
    
    st.write("Dataset extracted successfully.")
    return extract_dir

# Function to list categories and images
def list_categories_and_images(extract_dir):
    categories = [f for f in os.listdir(extract_dir) if os.path.isdir(os.path.join(extract_dir, f))]
    selected_category = st.selectbox("Choose a category", categories)
    
    if selected_category:
        image_dir = os.path.join(extract_dir, selected_category)
        images = os.listdir(image_dir)
        selected_image = st.selectbox("Choose an image", images)
        
        if selected_image:
            image_path = os.path.join(image_dir, selected_image)
            image = Image.open(image_path)
            st.image(image, caption=f"{selected_category} - {selected_image}", width=500)
            
            # Provide download link
            with open(image_path, "rb") as file:
                st.download_button(
                    label="Download Image",
                    data=file,
                    file_name=selected_image,
                    mime="image/png"
                )

def dataset_page():
    # st.image(r"data.PNG", use_column_width=True)
    extract_dir = download_and_extract_zip()
    list_categories_and_images(extract_dir)

dataset_page()
