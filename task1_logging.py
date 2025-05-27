import logging

# Создание логгера
logger = logging.getLogger('multi_logger')
logger.setLevel(logging.DEBUG)

# Формат логов
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# Хендлер для DEBUG и INFO
debug_info_handler = logging.FileHandler('debug_info.log')
debug_info_handler.setLevel(logging.DEBUG)
debug_info_handler.setFormatter(formatter)

# Хендлер для WARNING и выше
warn_error_handler = logging.FileHandler('warnings_errors.log')
warn_error_handler.setLevel(logging.WARNING)
warn_error_handler.setFormatter(formatter)

# Добавление хендлеров к логгеру
logger.addHandler(debug_info_handler)
logger.addHandler(warn_error_handler)

# Пример логов
logger.debug("Это сообщение уровня DEBUG")
logger.info("Это сообщение уровня INFO")
logger.warning("Это сообщение уровня WARNING")
logger.error("Это сообщение уровня ERROR")
logger.critical("Это сообщение уровня CRITICAL")
