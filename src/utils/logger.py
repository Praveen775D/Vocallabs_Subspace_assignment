from loguru import logger

logger.add(
    "logs/pipeline.log",
    rotation="5 MB",
    retention="7 days",
    level="INFO"
)

app_logger = logger