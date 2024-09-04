import streamlit as st
from transformers import pipeline

# Set up the page configuration
st.set_page_config(
    page_title="Dental Radiology Report Generator",
    page_icon="🦷",
    layout="centered"
)

# Apply custom CSS for background image and color theme
st.markdown(
    """
    <style>
    [data-testid="stAppViewContainer"] {
        background-image: url("https://images.unsplash.com/photo-1451187580459-43490279c0fa?fm=jpg&q=60&w=3000&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8N3x8bmF0dXJlJTIwZW5lcmd5fGVufDB8fDB8fHww");
        background-size: cover;
        padding: 0; /* Center the app */
    }
    [data-testid="stHeader"] {
        background-color: rgba(0, 0, 0, 0);
    }
    h1 {
        color: #1f78b4; /* Title color */
    }
    .stButton>button {
        color: white;
        background-color: #1f78b4; /* Button color */
        border-radius: 10px;
    }
    .stButton>button:hover {
        background-color: #005f6b; /* Hover button color */
    }
    .st-form div[data-baseweb="select"] {
        /* background-color: white; */
    }
    /* Slider styles */
    .stSlider input[type="range"] {
        -webkit-appearance: none;
        width: 100%;
        background-color: #e3f2fd; /* Slider track color */
        border-radius: 10px;
    }
    .stSlider input[type="range"]::-webkit-slider-thumb {
        -webkit-appearance: none;
        background-color: #0288d1; /* Slider handle color */
        border-radius: 10px;
        width: 20px;
        height: 20px;
        cursor: pointer;
    }
    .stSlider input[type="range"]::-moz-range-thumb {
        background-color: #0288d1; /* Slider handle color */
        border-radius: 10px;
        width: 20px;
        height: 20px;
        cursor: pointer;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Load model and tokenizer from Hugging Face
model_name = "Chanvitha/llama-2-7b-dental"
pipe = pipeline("text-generation", model=model_name)

# Streamlit UI
st.title("Dental Radiology Report Generator")
prompt = st.text_area("Enter your dental findings:")

if st.button("Generate Report"):
    pass
    result = pipe(f"[INST] <<SYS>>\nGenerate a radiology report based on the following dental findings:\n<</SYS>>\n\n{prompt} [/INST]", max_length=512)
    st.write(result[0]['generated_text'])
