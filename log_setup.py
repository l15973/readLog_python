import logging


def setup_logging(path, loggerName):
    logging.config.fileConfig(path)
    logger = logging.getLogger(loggerName)
    logger.info("Load log config completely.")
    return logger
