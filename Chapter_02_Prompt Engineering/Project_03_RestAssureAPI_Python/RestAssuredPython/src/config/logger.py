import logging
import os
from datetime import datetime
from src.config.config import Config

class LoggerSetup:
    """Centralized logging configuration."""

    _logger = None

    @classmethod
    def get_logger(cls, name="RestAssuredFramework"):
        """Get or create logger instance."""
        if cls._logger is None:
            cls._logger = cls._setup_logger(name)
        return cls._logger

    @classmethod
    def _setup_logger(cls, name):
        """Configure logger with file and console handlers."""
        os.makedirs(Config.LOG_DIR, exist_ok=True)

        logger = logging.getLogger(name)
        logger.setLevel(Config.LOG_LEVEL)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_file = os.path.join(Config.LOG_DIR, f"api_test_{timestamp}.log")

        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )

        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        return logger
