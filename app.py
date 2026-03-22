import streamlit as st
from PIL import Image
import random

# -----------------------------
# Streamlit Page Config
# -----------------------------
st.set_page_config(
    page_title="Smart Grocery Shelf-Life Predictor",
    page_icon="🍎",
    layout="centered"
)

# -----------------------------
# Title & Description
# -----------------------------
st.title("🍎 Smart Grocery Shelf-Life Predictor")
st.write(
    "Upload an image of any fruit and get an estimated freshness state.\n\n"
    "**This is a prototype demo (no ML model yet).**"
)

# -----------------------------
# File Upload
# -----------------------------
uploaded_file = st.file_uploader(
    "Upload a fruit image",
    type=["jpg", "jpeg", "png"]
)

# -----------------------------
# Mock Prediction Logic
# -----------------------------
def mock_predict():
    classes = ["Fresh 🟢", "Ripening 🟡", "Spoiled 🔴"]
    confidence = random.randint(70, 95)
    return random.choice(classes), confidence

# -----------------------------
# Display Result
# -----------------------------
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Fruit Image", use_column_width=True)

    if st.button("Predict Freshness"):
        label, confidence = mock_predict()

        st.subheader("Prediction Result")
        st.write(f"**Status:** {label}")
        st.write(f"**Confidence:** {confidence}%")

        if "Fresh" in label:
            st.success("This fruit is fresh and safe to consume.")
        elif "Ripening" in label:
            st.warning("Consume soon to avoid spoilage.")
        else:
            st.error("This fruit appears spoiled. Avoid consumption.")

st.markdown("---")
st.caption("Prototype version • ML model will be added later")
