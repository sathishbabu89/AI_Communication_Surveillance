
```markdown
# AI Communication Surveillance

This project is an **AI-powered email compliance monitoring system** for internal corporate communications. It uses **DeepSeek LLM** via `litellm` to automatically classify emails into potential compliance risk categories and assign priority levels.

---

## Features

- Upload any CSV file containing emails (`subject` + `body`).  
- Automatically classify emails into categories:
  - Secrecy
  - Market Manipulation / Misconduct
  - Market Bribery
  - Change in Communication
  - Complaints
  - Employee Ethics
- Assign a **priority score** from 1 (Low) to 5 (Critical).  
- Display **justification / source text** for each classification.  
- Fully automated: no per-email buttons required.

---

## Folder Structure

```

email\_compliance\_app/
│── .env.example           # Environment variable template
│── app.py                 # Streamlit UI
│── classify.py            # LLM classification logic
│── synthetic\_emails.csv   # Sample email dataset
│── requirements.txt       # Dependencies
│── README.md              # Project documentation

````

---

## Setup

1. **Clone the repository:**
```bash
git clone https://github.com/sathishbabu89/AI_Communication_Surveillance.git
cd AI_Communication_Surveillance
````

2. **Create a virtual environment (optional but recommended):**

```bash
python -m venv my_env
source my_env/bin/activate  # Linux / MacOS
my_env\Scripts\activate     # Windows
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

4. **Configure environment variables:**

* Copy `.env.example` to `.env` and add your **DeepSeek API key**:

```
DEEPSEEK_API_KEY=your_api_key_here
```

---

## Usage

1. Run the Streamlit app:

```bash
streamlit run app.py
```

2. Upload a CSV file with emails.
3. Adjust the **number of emails** to classify using the sidebar slider.
4. View **classification results**, **priority**, and **justification** in the UI.

---

## CSV Format

The CSV must contain at least these columns:

| Column  | Description        |
| ------- | ------------------ |
| subject | Email subject line |
| body    | Email body content |

---

## Security Note

* **Do not commit your `.env` file** with real API keys to GitHub.
* Use `.env.example` for sharing templates.

---

## License

This project is for demonstration and POC purposes.

```
