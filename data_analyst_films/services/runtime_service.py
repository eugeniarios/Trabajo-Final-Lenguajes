from pathlib import Path
import pandas as pd

ARTIFACTS_DIR = Path("artifacts")

def load_runtime_evolution():
    return pd.read_json(ARTIFACTS_DIR / "runtime_evolution.json")