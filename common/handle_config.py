import os
from configparser import ConfigParser
from common.handle_path import CONF_DIR


class Config(ConfigParser):
    def __init__(self, conf_file):
        super().__init__()
        self.read(conf_file, encoding='utf-8')

conf=Config(os.path.join(CONF_DIR, 'config.ini'))
# print((conf.get('mysql', 'host')))
# print((conf.get('sql_info', 'sql_order')))
# print(conf.get('guid_info', 'guid_endnumberlist003'))
# print(type(eval(conf.get('guid_info', 'guid_endnumberlist003'))))
# print(conf.get('mysql', 'host'))
# print(conf.get('request', 'url'))
# host = conf.get('mysql', 'host')
# sql = conf.get('sql_statement', 'sql')
# print(host)
# print(sql, type(sql))
# class Read_Config:
#     #定义一个读取配置的类
#     def __init__(self, filepath=CONF_DIR + r'\config.ini'):
#         self.cf = configparser.ConfigParser()
#         self.cf.read(filepath)
#
#     def get_config_str(self, section, option):
#         return self.cf.get(section, option)
#
#     def get_config_boolean(self, section, option):
#         return self.cf.getboolean(section, option)
#
#     def get_config_int(self, section, option):
#         return self.cf.getint(section, option)
#
#     def get_config_float(self, section, option):
#         return self.cf.getfloat(section, option)
#
# if __name__ == '__main__':
#     test = Read_Config().get_config_int("mysql", "port")
#     print(test)
#     print(type(test))
