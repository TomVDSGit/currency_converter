import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

custom_file_handler = logging.FileHandler('todo_logging.log')
custom_file_handler.setLevel(logging.INFO)

custom_file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(lineno)d - %(message)s')
custom_file_handler.setFormatter(custom_file_formatter)

logger.addHandler(custom_file_handler)
