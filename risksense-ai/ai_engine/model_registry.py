# model_registry.py
# Manages AI model versions and metadata
import joblib
from pathlib import Path

MODEL_DIR = Path("models")
MODEL_DIR.mkdir(exist_ok=True)

def save_model(model, name: str):
    joblib.dump(model, MODEL_DIR / f"{name}.joblib")

def load_model(name: str):
    return joblib.load(MODEL_DIR / f"{name}.joblib")
class ModelRegistry:
    def __init__(self):
        self.models = {}

    def register_model(self, name: str, model):
        self.models[name] = model
        save_model(model, name)

    def get_model(self, name: str):
        if name not in self.models:
            self.models[name] = load_model(name)
        return self.models[name]
    def list_models(self) -> list:
        return list(self.models.keys())
    def unregister_model(self, name: str):
        if name in self.models:
            del self.models[name]
            MODEL_DIR / f"{name}.joblib").unlink(missing_ok=True)
    def model_info(self, name: str) -> dict:
        if name in self.models:
            model = self.models[name]
            return {
                "name": name,
                "type": type(model).__name__,
                "parameters": model.get_params() if hasattr(model, 'get_params') else {}
            }
        return {}
        