import logging

# class LogGen:
#     @staticmethod
#     def loggen():
#         logging.basicConfig(filename='.\\logs\\automatiologin.logs', format='%(message)s:  %(asctime)s')
#         logger = logging.getLogger()
#         logger.setLevel(logging.DEBUG)
#         formatter = logging.Formatter('%(message)s  %(asctime)s')
#         return logger


import logging

class LogGen:
    def loggen():
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)

        formatter = logging.Formatter('%(message)s %(asctime)s')

        file_handler = logging.FileHandler('./logs/automatiologin.logs')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        return logger
