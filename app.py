import streamlit as st
import pandas as pd
import json
from classify import classify_email

st.set_page_config(page_title="AI Compliance Email Classifier", layout="wide")
st.title("📧 AI-Powered Compliance Email Classifier")

st.sidebar.header("Controls")
sample_size = st.sidebar.slider("Number of emails to classify", 5, 50, 10)

# Upload CSV
uploaded_file = st.file_uploader("Upload your email CSV file", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    # Check required columns
    if "subject" not in df.columns or "body" not in df.columns:
        st.error("CSV must contain 'subject' and 'body' columns")
    else:
        df["text"] = df["subject"].fillna("") + " " + df["body"].fillna("")
        st.success(f"✅ Loaded {len(df)} emails successfully!")

        # Sample emails for demo
        sampled_df = df.sample(min(sample_size, len(df)), random_state=42)
        results = []

        st.write("### 🔍 Classification Results")
        progress_text = st.empty()
        progress_bar = st.progress(0)

        # Automatically classify all emails
        for i, row in enumerate(sampled_df.itertuples(), 1):
            email_text = row.text
            output = classify_email(email_text)
            try:
                parsed = json.loads(output)
            except json.JSONDecodeError:
                parsed = {"error": output}

            results.append(parsed)

            # Show progress
            progress_text.text(f"Processing email {i}/{len(sampled_df)}")
            progress_bar.progress(i / len(sampled_df))

        # Display all results in table
        if results:
            results_df = pd.DataFrame(results)
            st.write("### 📊 Summary Table")
            st.dataframe(results_df)
            
            # Optionally show justification per email
            st.write("### 📄 Justifications / Source Texts")
            for i, res in enumerate(results, 1):
                st.write(f"**Email {i}:**")
                st.json(res)

else:
    st.info("Upload a CSV file containing your emails to start classification.")
