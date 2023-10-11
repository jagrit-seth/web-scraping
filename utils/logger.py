import logging
from logging.handlers import TimedRotatingFileHandler
import datetime


def configure_logger(feed_url):
    log_dir = "logs"
    log_file = f"{log_dir}/{feed_url.replace('/', '_').replace(':', '_')}_{datetime.datetime.now():%Y-%m-%d_%H-%M-%S}.log"

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    handler = TimedRotatingFileHandler(log_file, when="midnight", interval=1, backupCount=0)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    logger.addHandler(handler)

    return logger
