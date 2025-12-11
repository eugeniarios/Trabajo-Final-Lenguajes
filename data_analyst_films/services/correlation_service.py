from pathlib import Path
import pandas as pd

ARTIFACTS_DIR = Path("artifacts")

def load_budget_rating_corr():
    return pd.read_json(ARTIFACTS_DIR / "budget_rating_corr.json")