import logging

# Basic config (expand for DB, caching, etc.)
APP_NAME = "Number Analyzer API"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(APP_NAME)
