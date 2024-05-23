import logging
from Examples.TestModule import TestClass

# Create a logger
logger = logging.getLogger('example_logger')
logger.setLevel(logging.DEBUG)

# Create a console handler
handler = logging.StreamHandler()

# Create a logging format
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(handler)

# Use the logger in your code
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')
tm = TestClass()
