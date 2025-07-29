import os
from pathlib import Path

PROJECT_NAME = 'sentiment_analysis'

PATH_PROJECT = Path(__file__).resolve().parents[1]
PATH_PROJECT_ROOT = Path(os.getenv('SERVICE_SENTIMENT_ANALYSIS_ROOT', PATH_PROJECT))

PATH_LOGS = PATH_PROJECT_ROOT / 'logs'
PATH_CONFIGS = PATH_PROJECT_ROOT / 'configs'
PATH_DATABASE = PATH_PROJECT_ROOT / 'database' / 'reviews.db'
