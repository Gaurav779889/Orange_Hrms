import configparser
config = configparser.RawConfigParser()
<<<<<<< HEAD
config.read(".\\Configuration\\config.ini")
=======
config.read(".\\Configurations\\config.ini")
>>>>>>> 0d90d321fa968defed606e43122b8377e9590444

class ReadConfig:
    @staticmethod
    def get_username():
        username = config.get("login", "username")
        return username

    @staticmethod
    def get_password():
        return config.get("login", "password")

    @staticmethod
    def get_login_url():
        return config.get("urls", "login_url")