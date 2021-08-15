import logging
import inspect


class CustomLogger:

    def custom_logger(self, log_level=logging.DEBUG):
        # set class/method name from where its called
        logger_name = inspect.stack()[1][3]
        # create logger
        logger = logging.getLogger(logger_name)
        # set level for logging
        logger.setLevel(log_level)
        # create file handler
        fh = logging.FileHandler("automation.log")
        # create formatter
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(message)s")
        # add formatter to file handler
        fh.setFormatter(formatter)
        # add console handler to logger
        logger.addHandler(fh)
        return logger
