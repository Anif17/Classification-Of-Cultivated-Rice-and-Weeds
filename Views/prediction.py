import streamlit as st
from PIL import Image
import torch
import torchvision.transforms as transforms
import torch.nn as nn
import torchvision.models as models
import pandas as pd
import time
import os
from torchvision.models import ResNet50_Weights

# Set page config (optional)
st.set_page_config(
    page_title="AgriVision: Smart Crop & Weeds Classifier", 
    layout="wide", 
    page_icon="🌾"
)

# Define the model path
model_path = 'Model/ResNet50_Adam_0.0001.pth'  # Replace with your model's path
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Class names for predictions
class_names = ['Barnyard Grass', 'Cultivated Rice', 'Weedy Rice']

# Initialize session state for storing uploaded images, predicted labels, and file names
if 'predicted_labels' not in st.session_state:
    st.session_state.predicted_labels = []  # To store predicted labels
if 'file_names' not in st.session_state:
    st.session_state.file_names = []  # To store file names

# Function to check if the model file exists and load the model
@st.cache_resource
def load_model(model_path):
    if not os.path.exists(model_path):
        st.error(f"Model file not found at path: {model_path}")
        return None  # Return None if model file is missing

    model = models.resnet50(weights=None)  # Initialize ResNet50 without pre-trained weights
    
    # Freeze all layers in the model
    for param in model.parameters():
        param.requires_grad = False

    # Modify the fully connected layer to match the number of classes
    model.avgpool = nn.AdaptiveAvgPool2d(output_size=(1, 1))
    in_features = model.fc.in_features

    model.fc = nn.Sequential(
        nn.Flatten(),
        nn.Linear(in_features, 128),
        nn.ReLU(),
        nn.Dropout(0.2),
        nn.Linear(128, len(class_names))  # Output layer matching the number of classes
    )

    # Load saved model weights
    model.load_state_dict(torch.load(model_path, map_location=device))
    model = model.to(device)
    model.eval()  # Set model to evaluation mode
    return model

# Load the model
model = load_model(model_path)

# Check if the model is successfully loaded
if model is None:
    st.stop()  # Stop execution if the model is not loaded

# Image preprocessing function
def preprocess_image(image):
    preprocess = transforms.Compose([
        transforms.Resize(size=(299, 299)),
        transforms.ToTensor(),
    ])
    image = preprocess(image).unsqueeze(0)
    return image.to(device)

# Streamlit App Interface
st.title("🎯 Classification of Cultivated Rice & Weeds")
st.subheader("🔍Identify Cultivated Rice & Weeds with Convolutional Neural Networks")

# File uploader
uploaded_file = st.file_uploader("🌿Choose a plant image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.session_state.file_names.append(uploaded_file.name)

    # Display image and prediction details side by side
    col1, col2 = st.columns([1, 2])

    with col1:
        st.image(image, caption=uploaded_file.name, width=350)

    # Preprocess image and make predictions
    image = preprocess_image(image)
    start_time = time.time()
    with torch.no_grad():
        outputs = model(image)
        _, predicted = torch.max(outputs, 1)
        confidence_scores = torch.nn.functional.softmax(outputs, dim=1).cpu().numpy()
    end_time = time.time()

    # Prediction results
    duration = end_time - start_time
    st.session_state.predicted_labels.append(class_names[predicted.item()])

    # Display the confidence scores in the second column
    with col2:
        st.subheader(f'**🎯Predicted Class:** {class_names[predicted.item()]}')
        
        # Display time taken for prediction
        st.write(f"🕒 **Time taken for prediction:** {duration:.4f} seconds")  # Display duration in seconds
        
        with st.expander("View Confidence Scores", expanded=False):  # Set expanded=True to show by default
            st.write("### Confidence Scores")

            # Create a DataFrame for the bar chart
            scores_df = pd.DataFrame({
                'Class': class_names,
                'Confidence': confidence_scores[0]
            })

            # Use Streamlit's bar_chart method with a larger layout
            st.write("<style>div.block-container { width: 100% !important; }</style>", unsafe_allow_html=True)  # Ensures full width
            st.bar_chart(scores_df.set_index('Class'), color=["#1f77b4"], use_container_width=True, horizontal=True)  # This automatically adjusts the chart width
            
            st.write(f"The reason for predicting class **{class_names[predicted.item()]}** is because it shows the highest confidence score of **{confidence_scores[0][predicted.item()]:.2%}**.")
            
        with st.expander("Prevention and Control Tips", expanded=True): # Set expanded=True to show by default
            # Display the reason for prediction
            predicted_class = class_names[predicted.item()]

            # Add description and suggestion based on the predicted label
            if predicted_class == 'Barnyard Grass':
               st.write("### Barnyard Grass")
               st.write("Barnyard Grass is a prevalent and competitive weed in rice fields, significantly reducing crop yields by competing for essential resources like nutrients, water, and sunlight.")
               st.write("#### Prevention Tips:")
               st.write("- **Adopt Transplanting Over Direct Seeding**: Use transplanting methods to establish rice seedlings early, outcompeting emerging Barnyard Grass.")
               st.write("- **Field Sanitation and Preparation**: Thoroughly till the soil and remove plant debris to disrupt Barnyard Grass seed banks.")
               st.write("- **Use Certified Seeds**: Ensure seeds are certified and free from Barnyard Grass contamination.")
               st.write("- **Crop Rotation and Fallowing**: Rotate rice with non-host crops or implement fallow periods to break the weed lifecycle.")
               st.write("- **Implement Clearfield® Production System (CPS)**: Follow CPS stewardship guidelines strictly to prevent herbicide resistance.")
               st.write("- **Use Multiple Herbicide Modes of Action**: Rotate herbicides with different modes to reduce resistance risk.")
               st.write("- **Regular Tilling and Manual Weeding**: Perform mechanical cultivation and manual weeding to physically remove Barnyard Grass.")
            
            elif predicted_class == 'Weedy Rice':
                st.write("### Weedy Rice")
                st.write("Weedy rice is a type of rice that has become invasive and competes with cultivated rice, leading to significant yield losses.")
                st.write("#### Prevention Tips:")
                st.write("- **Switch to transplanting**: Use traditional transplanting methods instead of direct seeding to reduce seed contamination.")
                st.write("- **Field sanitation**: Ensure thorough land preparation and removal of weedy rice seeds before planting.")
                st.write("- **Use certified seeds**: Prevent the use of contaminated seeds by relying on certified, high-quality seeds.")
                st.write("- **Integrated weed management**: Combine herbicides with mechanical weeding and regular monitoring.")
                st.write("- **Follow CPS stewardship guidelines**: When using the Clearfield® Production System, strictly adhere to its guidelines to avoid herbicide resistance.")
                st.write("- **Crop rotation and fallowing**: Alternate rice cultivation with other crops or allow fields to rest to disrupt the lifecycle of weedy rice.")
             

            elif predicted_class == 'Cultivated Rice':
                st.write("### Cultivated Rice")
                st.write("Cultivated rice is the primary crop grown in rice fields and plays a vital role in global food security.")
                st.write("#### Maintenance Tips:")
                st.write("- **Water management**: Maintain consistent water levels throughout the growing season to ensure proper development.")
                st.write("- **Fertilization**: Apply balanced fertilizers at appropriate growth stages to boost nutrient uptake and maximize yield.")
                st.write("- **Weed control**: Regularly monitor and remove any weeds to prevent competition for nutrients, water, and sunlight.")
                st.write("- **Disease monitoring**: Inspect plants frequently for signs of disease and apply appropriate treatments when necessary.")
                st.write("- **Harvesting timing**: Harvest the crop at the optimal time to maximize grain quality and minimize losses.")


# Footer
st.markdown(
    """
    <hr style="border:0.5px solid gray">
    <p style="text-align: center;">
        Developed by Muhammad Anif
    </p>
    """, unsafe_allow_html=True
)
