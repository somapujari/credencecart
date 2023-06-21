
import configparser
config = configparser.RawConfigParser()
config.read(r'C:\Users\Dell\PycharmProjects\credence\configuration\config.ini')


class ReadConfig:
    @staticmethod
    def get_appplication_url():
        url = config.get('common info','base_url')
        return url

    @staticmethod
    def get_user_mail():
        user_mail = config.get('common info','user_mail')
        return user_mail

    @staticmethod
    def get_password():
        password = config.get('common info','password')
        return password

