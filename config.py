import os
from pathlib import Path
from dotenv import load_dotenv

# 1. Load keys from .env
load_dotenv()

# 2.  Project root folder
BASE_DIR = Path(__file__).resolve().parent

# 3. Folder paths
DATA_DIR = BASE_DIR / "data"
MODELS_DIR = BASE_DIR / "models"
VECTOR_DB_DIR = BASE_DIR / "vector_db"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"

# 4.  API keys
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")

# 5.  Region settings
REGION = {
    "name": os.getenv("ACTIVE_REGION", "sf"),
    "socrata_domain": "data.sf.gov",
    "tables": {
        "crashes": {
            "dataset_id": "ubvf-ztfx",
            "columns": {
                "crash_id": "case_id_pkey",
                "date": "collision_datetime",
                "lat": "tb_latitude",
                "lon": "tb_longitude",
                "intersection_id": "cnn_intrsctn_fkey",
                "intersection_type": "intersection",
                "killed": "number_killed",
                "injured": "number_injured",
            },
        },
        "streets": {"dataset_id": "3psu-pn9h"},
        "pavement": {"dataset_id": "5aye-4rtt"},
    },
}

# 6.Paths for the active region
REGION_RAW_DIR = RAW_DIR / REGION["name"]
REGION_PROCESSED_DIR = PROCESSED_DIR / REGION["name"]
REGION_MODELS_DIR = MODELS_DIR / REGION["name"]

# 7. Create folders if missing
for directory in [DATA_DIR, MODELS_DIR, VECTOR_DB_DIR,
                  REGION_RAW_DIR, REGION_PROCESSED_DIR, REGION_MODELS_DIR]:
    directory.mkdir(parents=True, exist_ok=True)