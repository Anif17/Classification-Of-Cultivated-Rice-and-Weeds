import streamlit as st
import pandas as pd

# Set page config (optional)
st.set_page_config(page_title="AgriVision: Smart Crop & Weeds Classifier", layout="wide", page_icon="🌾")

st.title("🧭 History Classification of Cultivated Rice & Weeds")
st.subheader("🔍 Identify Cultivated Rice & Weeds with Convoluted Neural Networks")

# Check if there are any predictions stored in session state
if 'file_names' in st.session_state and 'predicted_labels' in st.session_state:
    if st.session_state.file_names:
        # Prepare data for DataFrame
        data = {
            "File Name": st.session_state.file_names,
            "Predicted Label": st.session_state.predicted_labels,
        }
        df = pd.DataFrame(data)

        # Display the history of predictions in a table
        st.subheader("📝 Prediction History")
        
        # Display the DataFrame as a table
        st.table(df)  # Display the entire history in a table format
        
        for index, row in df.iterrows():
            with st.expander(f"Prediction {index + 1}"):
                st.write(f"**File Name:** {row['File Name']}")
                st.write(f"**Predicted Label:** {row['Predicted Label']}")
                # Optionally add more details if needed

       

    else:
        st.write("No prediction history available.")
else:
    st.write("No prediction history available.")
