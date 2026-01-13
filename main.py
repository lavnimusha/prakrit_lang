import streamlit as st
from openai import OpenAI
import streamlit as st

# ---------- EXTRACT KEY ----------

# ----------------------------
# CONFIG
# ----------------------------
st.set_page_config(
    page_title="Prakrit Translator",
    page_icon="📜",
    layout="centered"
)
OPENAI_API_KEY=st.secrets["OPENAI_KEY"]

client = OpenAI(api_key=OPENAI_API_KEY)

# ----------------------------
# CORE TRANSLATION FUNCTION
# ----------------------------
def convert_prakrit(sentence: str) -> str:
    prompt = f"""
You are an expert in Maharashtrian Prakrit and classical Indic poetry.

IMPORTANT RULES (STRICT):
- Translate ONLY what is present in the text
- DO NOT add philosophy, metaphors, or new imagery
- NO abstraction like knowledge, truth, light unless explicitly present
- Preserve imagery such as clouds, lightning, thunder, directions
- Avoid interpretive or explanatory additions
- Maintain grammatical relations and gender accurately

TASK:
1. Provide Hindi translation.
2. Provide English translation.

TEXT:
{sentence}
"""

    response = client.chat.completions.create(
        model="gpt-5.2",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    return response.choices[0].message.content.strip()

# ----------------------------
# STREAMLIT UI
# ----------------------------
st.title("📜 Prakrit → Hindi & English Translator")
st.caption("Strict • Literal • No added imagination")

input_text = st.text_area(
    "Enter Prakrit text:",
    height=150,
    placeholder="Paste Prakrit verse here..."
)

if st.button("Translate"):
    if not input_text.strip():
        st.warning("Please enter some Prakrit text.")
    else:
        with st.spinner("Translating..."):
            try:
                result = convert_prakrit(input_text)
                st.success("Translation completed")
                st.text(result)
            except Exception as e:
                st.error(f"Error: {e}")







