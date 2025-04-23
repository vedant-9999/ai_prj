import streamlit as st
from spam_filter import predict_spam, accuracy

st.set_page_config(page_title="Spam Filter", layout="centered")

st.title("📧 Email Spam Classifier")
st.write("Type or paste an email below and check if it's Spam or Ham.")

# Input field
email_input = st.text_area("Enter your email text:")

if st.button("Check"):
    if email_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        prediction = predict_spam(email_input)
        if prediction == "Spam":
            st.error("🚫 It's Spam!")
        else:
            st.success("✅ It's Ham (Not Spam)")

st.markdown(f"**Model Accuracy:** `{accuracy * 100:.2f}%`")
