import numpy as np

# confidence_score.py
# Calculates confidence scores for explanations
def calculate_confidence_score(probabilities):
    """
    Calculates the confidence score given a list or numpy array of probabilities.
    The confidence score is the maximum probability value, representing the model's certainty.

    Args:
        probabilities (list or np.ndarray): Probabilities for each class.

    Returns:
        float: Confidence score between 0 and 1.
    """
    probabilities = np.asarray(probabilities, dtype=np.float64)
    if probabilities.ndim != 1:
        raise ValueError("Input probabilities must be a 1D array or list.")
    if probabilities.size == 0:
        raise ValueError("Input probabilities array cannot be empty.")
    if not np.all((0.0 <= probabilities) & (probabilities <= 1.0)):
        raise ValueError("All probabilities must be between 0 and 1.")
    return float(np.max(probabilities))