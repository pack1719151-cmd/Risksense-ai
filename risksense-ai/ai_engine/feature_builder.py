# feature_builder.py
# Builds features for AI models
import pandas as pd

def build_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    if "sales" in df and "returns" in df:
        df["return_ratio"] = df["returns"] / df["sales"]
    return df
class FeatureBuilder:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def build(self) -> pd.DataFrame:
        return build_features(self.df)
    def get_feature_info(self) -> dict:
        return {
            "columns": self.df.columns.tolist(),
            "num_rows": self.df.shape[0]
        }
        