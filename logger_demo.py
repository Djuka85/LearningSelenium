import logging


class LoggerDemo:

    def sample_logger(self):
        # will help setting the level
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)

        # create console handler of file handler and set the log level
        ch = logging.StreamHandler()  # will display logs on console
        fh = logging.FileHandler("demologfile.log")  # will output logs to specified file

        # create formatter - how do we want our logs to be formatted
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(message)s",
                                      datefmt="%m/%d/%Y %I:%M:%S %p")
        formatter1 = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(message)s")
        # add formatter to console or file handler
        ch.setFormatter(formatter)
        fh.setFormatter(formatter1)

        # add console handler to logger
        logger.addHandler(ch)
        logger.addHandler(fh)

        logger.debug("debug log statement")
        logger.info("info log statement")
        logger.warning("warning log statement")
        logger.error("error log statement")
        logger.critical("critical log statement")


ld = LoggerDemo()
ld.sample_logger()
