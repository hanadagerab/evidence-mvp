CLAIM_THRESHOLD = 30000


def calculate_verified_amount(transactions):
    """
    Sum only transactions whose final_status is Verified.
    """
    verified_transactions = transactions[
        transactions["final_status"] == "Verified"
    ]

    return verified_transactions["amount"].sum()


def evaluate_threshold(verified_amount):
    """
    Compare the directly verified amount with the MVP threshold.
    """
    if verified_amount >= CLAIM_THRESHOLD:
        return "Threshold met"

    return "Threshold not met"