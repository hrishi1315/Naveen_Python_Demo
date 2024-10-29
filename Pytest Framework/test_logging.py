import logging

a = logging.getLogger(__name__)

b= logging.FileHandler('logfile.log')

a.addHandler(b)


a.debug("Execute in debug mode")
a.info("any info needed?")
a.warning("warning message")
a.error("error occures")
a.critical("critical error got")