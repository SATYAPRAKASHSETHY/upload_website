import streamlit as st
import os

# Create uploads folder if not exists
if not os.path.exists("uploads"):
    os.makedirs("uploads")
st.title("📁 File Upload and Sharing App")
uploaded_file = st.file_uploader("Choose a file to upload", type=None)

if uploaded_file:
    file_path = os.path.join("uploads", uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success(f"Uploaded `{uploaded_file.name}` successfully!")

    # Shareable download link
    st.markdown(f"### 👉 [Click to download `{uploaded_file.name}`](uploads/{uploaded_file.name})")
