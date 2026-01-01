# explain_risk.py
# Provides explanations for detected risks
def explain_risk(risk_id, risk_data):
    """
    Generate a clear, actionable explanation for a detected risk.

    Args:
        risk_id (str): Unique identifier for the risk.
        risk_data (dict): Dictionary containing risk details.

    Returns:
        str: Human-readable explanation of the risk.
    """
    risk_type = risk_data.get("type", "Unknown")
    severity = risk_data.get("severity", "N/A")
    description = risk_data.get("description", "No description provided.")
    impact = risk_data.get("impact", "Impact not specified.")
    recommendation = risk_data.get("recommendation", "No recommendation available.")

    explanation = (
        f"Risk ID: {risk_id}\n"
        f"Type: {risk_type}\n"
        f"Severity: {severity}\n"
        f"Details: {description}\n"
        f"Impact: {impact}\n"
    )

    if severity.lower() == "high":
        explanation += "⚠️ Immediate action required: This risk is of high severity.\n"
    elif severity.lower() == "medium":
        explanation += "⚠️ Prompt review recommended: This risk is of medium severity.\n"
    elif severity.lower() == "low":
        explanation += "ℹ️ Monitor this risk: It is currently low severity.\n"
    else:
        explanation += "ℹ️ Severity level is unspecified. Review as appropriate.\n"

    explanation += f"Recommendation: {recommendation}\n"

    return explanation