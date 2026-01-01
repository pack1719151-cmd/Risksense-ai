import pandas as pd
import numpy as np

# stats_checker.py
# Checks data statistics for anomalies
class StatsChecker:
    def __init__(self, dataframe: pd.DataFrame):
        self.df = dataframe.copy()

    def check_missing_values(self):
        missing = self.df.isnull().sum()
        percent = (missing / len(self.df)) * 100
        missing_report = pd.DataFrame({
            'missing_count': missing,
            'missing_percent': percent
        })
        return missing_report[missing_report['missing_count'] > 0]

    def check_outliers(self, z_thresh=3):
        numeric_cols = self.df.select_dtypes(include=np.number).columns
        outlier_report = {}
        for col in numeric_cols:
            col_zscore = np.abs((self.df[col] - self.df[col].mean()) / self.df[col].std(ddof=0))
            outliers = self.df[col][col_zscore > z_thresh]
            if not outliers.empty:
                outlier_report[col] = {
                    'count': outliers.count(),
                    'indices': outliers.index.tolist(),
                    'values': outliers.tolist()
                }
        return outlier_report

    def check_unique_values(self, threshold=0.9):
        unique_report = {}
        for col in self.df.columns:
            unique_count = self.df[col].nunique(dropna=True)
            unique_ratio = unique_count / len(self.df)
            if unique_ratio > threshold:
                unique_report[col] = {
                    'unique_count': unique_count,
                    'unique_ratio': unique_ratio
                }
        return unique_report

    def summary(self):
        return {
            "missing_values": self.check_missing_values(),
            "outliers": self.check_outliers(),
            "high_cardinality": self.check_unique_values()
        }
