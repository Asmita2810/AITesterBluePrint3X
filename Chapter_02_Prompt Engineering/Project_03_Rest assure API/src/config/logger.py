import logging
from pathlib import Path
from .config import Config

class LoggerManager:
    """Centralized logging management"""

    _loggers = {}

    @classmethod
    def setup_logging(cls):
        """Initialize logging configuration"""
        Path(Config.LOGS_DIR).mkdir(parents=True, exist_ok=True)

        logging.basicConfig(
            level=Config.LOG_LEVEL,
            format=Config.LOG_FORMAT,
            handlers=[
                logging.FileHandler(Config.LOGS_DIR / "test_execution.log"),
                logging.StreamHandler()
            ]
        )

    @classmethod
    def get_logger(cls, name: str) -> logging.Logger:
        """Get or create logger"""
        if name not in cls._loggers:
            cls._loggers[name] = logging.getLogger(name)
        return cls._loggers[name]
