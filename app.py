import streamlit as st

st.set_page_config(
    page_title="Evidence",
    page_icon="🔎",
    layout="wide",
)

st.title("Evidence")

st.subheader("A verification layer, not another score.")

st.write(
    "Grade the evidence, not the person. Verify broadly, disclose narrowly."
)

st.divider()

st.markdown("### MVP Claim")

st.info(
    "At least MX$30,000 in monthly business inflows are directly verifiable."
)

st.caption(
    "This MVP evaluates evidence supporting the claim. "
    "It does not generate a credit score, risk score, "
    "probability of default, or lending recommendation."
)
import pandas as pd

st.divider()

st.markdown("### Synthetic Maria Evidence Data")

transactions = pd.read_csv("data/maria_transactions.csv")

st.dataframe(transactions, use_container_width=True)