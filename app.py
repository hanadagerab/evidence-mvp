import streamlit as st

import pandas as pd
from verification import classify_transaction

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
st.divider()

st.markdown("### Synthetic Maria Evidence Data")

transactions = pd.read_csv("data/maria_transactions.csv")

classification_results = transactions.apply(
    classify_transaction,
    axis=1
)

transactions[["final_status", "reason"]] = pd.DataFrame(
    classification_results.tolist(),
    index=transactions.index
)

display_columns = [
    "transaction_id",
    "date",
    "source",
    "description",
    "amount",
    "final_status",
    "reason",
    "provenance",
]

st.dataframe(
    transactions[display_columns],
    use_container_width=True
)