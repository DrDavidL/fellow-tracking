import streamlit as st
import pandas as pd
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Load OpenAI API key from environment variables
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

LOG_FILE = "log.csv"

def load_log():
    if os.path.exists(LOG_FILE):
        return pd.read_csv(LOG_FILE)
    return pd.DataFrame(columns=["timestamp", "experience"])

def save_log(df):
    df.to_csv(LOG_FILE, index=False)

def analyze_log(log_df):
    if log_df.empty:
        return "No experiences logged yet. Please add some experiences to get recommendations."

    # Prepare the prompt for GPT-4o
    log_text = "\n".join(log_df["experience"].tolist())
    prompt = f"""
    You are an AI assistant specializing in clinical informatics.
    A fellow has logged the following clinical informatics experiences:

    {log_text}

    Based on these experiences, please provide recommendations for next steps to ensure all key clinical informatics topics are covered during their rotations.
    Consider areas like:
    - Clinical Decision Support
    - Electronic Health Records (EHR) implementation and optimization
    - Data Analytics and Visualization in healthcare
    - Health Information Exchange (HIE) and Interoperability
    - Telemedicine and Digital Health
    - Patient Safety and Quality Improvement through Informatics
    - Biomedical Informatics and Genomics
    - Public Health Informatics
    - Regulatory and Ethical aspects of Clinical Informatics

    Provide actionable recommendations, identifying gaps and suggesting specific types of experiences or learning opportunities.
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant specializing in clinical informatics."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error analyzing log with GPT-4o: {e}"

st.set_page_config(page_title="Clinical Informatics Fellow Log & Analyzer", layout="wide")

st.title("Clinical Informatics Fellow Log & Analyzer")

# Experience Logging Section
st.header("Log New Experience")
with st.form("experience_form"):
    new_experience = st.text_area("Describe your recent clinical informatics experience:")
    submitted = st.form_submit_button("Add to Log")

    if submitted and new_experience:
        log_df = load_log()
        new_entry = pd.DataFrame([{"timestamp": pd.Timestamp.now(), "experience": new_experience}])
        log_df = pd.concat([log_df, new_entry], ignore_index=True)
        save_log(log_df)
        st.success("Experience added to log!")
    elif submitted and not new_experience:
        st.warning("Please enter an experience to log.")

# Display Log Section
st.header("Experience Log")
log_df = load_log()
if not log_df.empty:
    st.dataframe(log_df.sort_values(by="timestamp", ascending=False))
else:
    st.info("No experiences logged yet.")

# Analysis Section
st.header("Recommendations for Next Steps")
if st.button("Analyze Log and Get Recommendations"):
    with st.spinner("Analyzing experiences with GPT-4o..."):
        recommendations = analyze_log(log_df)
        st.write(recommendations)

st.markdown("---")
st.markdown("Developed for Clinical Informatics Fellows")
