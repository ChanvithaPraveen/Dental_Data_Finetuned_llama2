![dental](https://github.com/user-attachments/assets/c49b6cc5-d926-4530-83a2-e32559a23080)
# Dental Radiology Report Generator

This project provides a Streamlit application for generating dental radiology reports using a fine-tuned language model. The model is fine-tuned on a dataset of dental findings to generate comprehensive radiology reports based on user input.

## Project Overview

The application uses the `transformers` library from Hugging Face to load a pre-trained language model and generate text based on user-provided dental findings. The Streamlit interface allows users to input their findings and get a generated report.

## Prerequisites

Before running the application, ensure you have the following installed:

- Python 3.8 or higher
- `transformers` library
- `streamlit` library
- `torch` library
- `peft` library
- `trl` library

You can install the required libraries using pip:

```bash
pip install transformers streamlit torch peft trl
```

## Project Setup

1. **Clone the Repository**

   Clone this repository to your local machine using:

   ```bash
   git clone <https://github.com/ChanvithaPraveen/Dental_Data_Finetuned_llama2.git>
   ```

2. **Navigate to the Project Directory**

   ```bash
   cd dental-radiology-report-generator
   ```


## Running the Streamlit App

1. **Navigate to the Streamlit App Directory**

   ```bash
   cd streamlit-app
   ```

2. **Run the Streamlit Application**

   ```bash
   streamlit run app.py
   ```

   This command will start the Streamlit app and open it in your default web browser.

## App Details

### Features

- **Text Input:** Enter dental findings in a text area.
- **Report Generation:** Click the "Generate Report" button to receive a radiology report based on the findings.
