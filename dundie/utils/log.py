from logging import handlers
import logging
import os

LOG_LEVEL = os.getenv("LOG_LEVEL", "WARNING").upper()

log = logging.getLogger("dundie")

fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s'
    '1:%(lineno)d f:%(filename)s: %(message)s'
)


def get_logger(logfile="dundie.log"):
    """Returns a configred logger"""
    fh = handlers.RotatingFileHandler(
        logfile,
        maxBytes=300,
        backupCount=10,
    )
    fh.setLevel(LOG_LEVEL)

    fh.setFormatter(fmt)

    log.addHandler(fh)

    return log


