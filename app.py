import streamlit as st
import pandas as pd

from verification import classify_transaction
from claim_engine import (
    calculate_verified_amount,
    evaluate_threshold,
    CLAIM_THRESHOLD,
)

st.set_page_config(
    page_title="Evidence",
    page_icon="🔎",
    layout="wide",
)

# ----------------------------
# Load + classify synthetic evidence
# ----------------------------

transactions = pd.read_csv("data/maria_transactions.csv")

classification_results = transactions.apply(
    classify_transaction,
    axis=1,
)

transactions[["final_status", "reason"]] = pd.DataFrame(
    classification_results.tolist(),
    index=transactions.index,
)

# ----------------------------
# Deterministic claim calculation
# ----------------------------

verified_amount = calculate_verified_amount(transactions)
claim_result = evaluate_threshold(verified_amount)

category_totals = (
    transactions.groupby("final_status")["amount"]
    .sum()
    .to_dict()
)

verified_total = category_totals.get("Verified", 0)
corroborated_total = category_totals.get("Corroborated", 0)
unresolved_total = category_totals.get("Unresolved", 0)
excluded_total = category_totals.get("Excluded", 0)

# ----------------------------
# View selector
# ----------------------------

st.sidebar.title("Evidence")
st.sidebar.caption("Synthetic MVP")

view = st.sidebar.radio(
    "Choose view",
    ["María View", "Third-Party View"],
)

# ============================================================
# MARÍA VIEW
# ============================================================

if view == "María View":

    st.title("Evidence")
    st.subheader("A verification layer, not another score.")

    st.write(
        "Grade the evidence, not the person. "
        "Verify broadly, disclose narrowly."
    )

    st.caption("Demo uses synthetic data only.")

    st.divider()

    # ----------------------------
    # MVP Claim
    # ----------------------------

    st.markdown("### MVP Claim")

    st.info(
        "At least MX$30,000 in monthly business inflows "
        "are directly verifiable."
    )

    st.caption(
        "This MVP evaluates evidence supporting the claim. "
        "It does not generate a credit score, risk score, "
        "probability of default, or lending recommendation."
    )

    # ----------------------------
    # Claim Result
    # ----------------------------

    st.divider()

    st.markdown("### Claim Result")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            label="Directly Verified Amount",
            value=f"MX${verified_amount:,.0f}",
        )

    with col2:
        st.metric(
            label="Claim Threshold",
            value=f"MX${CLAIM_THRESHOLD:,.0f}",
        )

    if claim_result == "Threshold met":
        st.success("Threshold met")
    else:
        st.warning("Threshold not met")

    st.caption(
        "Only evidence classified as Verified is included "
        "in the directly verified amount."
    )

    # ----------------------------
    # Evidence Breakdown
    # ----------------------------

    st.markdown("### Evidence Breakdown")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "Verified",
            f"MX${verified_total:,.0f}",
        )

    with c2:
        st.metric(
            "Corroborated",
            f"MX${corroborated_total:,.0f}",
        )

    with c3:
        st.metric(
            "Unresolved",
            f"MX${unresolved_total:,.0f}",
        )

    with c4:
        st.metric(
            "Excluded",
            f"MX${excluded_total:,.0f}",
        )

    st.caption(
        "These categories remain separate. "
        "Corroborated and unresolved evidence are never "
        "blended into the directly verified total."
    )

    # ----------------------------
    # María explanation
    # ----------------------------

    st.markdown("### What this means for María")

    st.markdown(
        f"María has **MX\\${verified_amount:,.0f} in directly "
        f"verified business inflows**. The claim requires "
        f"at least **MX\\${CLAIM_THRESHOLD:,.0f}**."
    )

    st.write(
        "- **Verified** evidence counts toward the claim.\n"
        "- **Corroborated** evidence has support, but not enough "
        "independent support to count as directly verified.\n"
        "- **Unresolved** evidence is too incomplete or ambiguous "
        "to classify more strongly.\n"
        "- **Excluded** activity does not belong in the claim, "
        "such as self-transfers, refunds, duplicates, or "
        "non-business activity."
    )

    # ----------------------------
    # Full evidence table
    # ----------------------------

    st.markdown("### María's Evidence")

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
        width="stretch",
    )

    st.caption(
        "Evidence is evaluated for this specific claim only. "
        "The system grades the evidence, not María."
    )

# ============================================================
# THIRD-PARTY VIEW
# ============================================================

else:

    st.title("Third-Party Evidence Summary")

    st.subheader("Minimal disclosure for one specific claim.")

    st.info(
        "This view intentionally excludes María's raw transaction "
        "history and relational data."
    )

    st.caption("Demo uses synthetic data only.")

    st.divider()

    # ----------------------------
    # Claim
    # ----------------------------

    st.markdown("### Claim")

    st.write(
        "**At least MX$30,000 in monthly business inflows "
        "are directly verifiable.**"
    )

    # ----------------------------
    # Result
    # ----------------------------

    summary_col1, summary_col2 = st.columns(2)

    with summary_col1:
        st.metric(
            label="Claim Result",
            value=claim_result,
        )

    with summary_col2:
        st.metric(
            label="Directly Verified Amount",
            value=f"MX${verified_amount:,.0f}",
        )

    # ----------------------------
    # Evidence Categories
    # ----------------------------

    st.markdown("### Evidence Categories")

    st.write(
        f"- Verified: MX${verified_total:,.0f}\n"
        f"- Corroborated: MX${corroborated_total:,.0f}\n"
        f"- Unresolved: MX${unresolved_total:,.0f}\n"
        f"- Excluded: MX${excluded_total:,.0f}"
    )

    # ----------------------------
    # Provenance
    # ----------------------------

    st.markdown("### Provenance")

    st.write(
        "Evidence was derived from synthetic SPEI records, "
        "synthetic Mercado Pago records, and synthetic cash evidence."
    )

    # ----------------------------
    # Coverage limitations
    # ----------------------------

    st.markdown("### Coverage Limitations")

    st.write(
        "- Only the provided synthetic evidence was evaluated.\n"
        "- Cash without independent supporting evidence is not "
        "directly verified.\n"
        "- Corroborated and unresolved evidence does not enter "
        "the directly verified total.\n"
        "- Missing or ambiguous evidence can reduce coverage.\n"
        "- The result applies only to the stated monthly inflow claim.\n"
        "- This is not a credit score, risk score, probability of "
        "default, or lending recommendation."
    )

    st.success(
        "Minimal disclosure check passed: no raw transaction history "
        "or relational data is displayed in this view."
    )

    st.info(
        "Verify broadly, disclose narrowly: this view shares only "
        "the minimum information needed to communicate the claim "
        "result and evidence coverage."
    )