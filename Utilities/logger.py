import inspect
import logging


class Logger_class:
    @staticmethod
    def get_logger():
<<<<<<< HEAD
        logger = logging.getLogger(inspect.stack()[1][3])
        logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s : %(name)s : %(funcName)s : %(levelname)s - %(message)s')
=======
        logger = logging.getLogger(inspect.stack()[1][3])#ethod anle apan
        logger.setLevel(logging.INFO)# set the level
        formatter = logging.Formatter('%(asctime)s : %(name)s : %(funcName)s : %(levelname)s - %(message)s')# giving format
>>>>>>> 0d90d321fa968defed606e43122b8377e9590444
        file_handler = logging.FileHandler('.\\Logs\\OrangeHRM.log')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        return logger