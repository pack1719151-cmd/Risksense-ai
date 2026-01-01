import numpy as np
from scipy.stats import ks_2samp

# drift_detector.py
# Detects data drift over time
class DriftDetector:
    """
    Detects data drift between two datasets using statistical tests.
    """

    def __init__(self, threshold=0.05):
        """
        Args:
            threshold (float): p-value threshold for drift detection.
        """
        self.threshold = threshold

    def detect_drift(self, reference_data, new_data):
        """
        Compares reference_data and new_data for drift.

        Args:
            reference_data (np.ndarray): Baseline data.
            new_data (np.ndarray): Incoming data to compare.

        Returns:
            dict: Feature-wise drift results.
        """
        # Input validation
        if not isinstance(reference_data, np.ndarray) or not isinstance(new_data, np.ndarray):
            raise TypeError("Both reference_data and new_data must be numpy arrays.")
        if reference_data.ndim != 2 or new_data.ndim != 2:
            raise ValueError("Both reference_data and new_data must be 2D arrays.")
        if reference_data.shape[1] != new_data.shape[1]:
            raise ValueError("reference_data and new_data must have the same number of features (columns).")
        if reference_data.shape[0] == 0 or new_data.shape[0] == 0:
            raise ValueError("Input arrays must not be empty.")

        drift_results = {}
        num_features = reference_data.shape[1]
        for i in range(num_features):
            stat, p_value = ks_2samp(reference_data[:, i], new_data[:, i])
            drift_results[f'feature_{i}'] = {
                'p_value': p_value,
                'drift': p_value < self.threshold
            }
        return drift_results