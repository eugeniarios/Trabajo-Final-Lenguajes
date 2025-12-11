from pathlib import Path
import pandas as pd

ARTIFACTS_DIR = Path("artifacts")

def load_roi_by_genre():
    return pd.read_json(ARTIFACTS_DIR / "roi_by_genre.json")

def load_roi_by_country():
    return pd.read_json(ARTIFACTS_DIR / "roi_by_country.json")