def classify_transaction(row):
    """
    Deterministically assign one final evidence status.

    Possible outputs:
    - Verified
    - Corroborated
    - Unresolved
    - Excluded
    """

    # Exclusion rules come first.
    if row["is_duplicate"] == "yes":
        return "Excluded", "Duplicate transaction"

    if row["is_refund_reversal"] == "yes":
        return "Excluded", "Refund or reversal"

    if row["is_self_transfer"] == "yes":
        return "Excluded", "Self-transfer"

    if row["is_business_related"] == "no":
        return "Excluded", "Not related to business activity"

    # Ambiguous or incomplete evidence.
    if row["is_business_related"] == "unknown":
        return "Unresolved", "Business purpose is unclear"

    if row["evidence_present"] == "no":
        return "Unresolved", "Supporting evidence is incomplete or missing"

    # Cash is not directly verified in this MVP
    # unless independent support exists.
    if row["source"] == "Cash":
        if row["independent_support"] == "yes":
            return "Verified", "Cash activity has independent supporting evidence"
        else:
            return "Corroborated", "Cash activity has supporting but non-independent evidence"

    # Structured digital inflows may be Verified when
    # independent support is present.
    if row["source"] in ["SPEI", "Mercado Pago"]:
        if row["independent_support"] == "yes":
            return "Verified", "Independent evidence supports the business inflow"
        else:
            return "Corroborated", "Business inflow has support but lacks independent verification"

    # Fallback rule.
    return "Unresolved", "Available evidence does not clearly support classification"