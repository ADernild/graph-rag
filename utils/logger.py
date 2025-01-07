import logging

# Create a custom logger
logger = logging.getLogger("pdf_graph_transformer")
logger.setLevel(logging.DEBUG)

# Create handlers
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# Create formatters and add them to handlers
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
console_handler.setFormatter(formatter)

# Add handlers to the logger
logger.addHandler(console_handler)


def log_info(message: str):
    logger.info(message)


def log_error(message: str):
    logger.error(message)


def log_debug(message: str):
    logger.debug(message)
