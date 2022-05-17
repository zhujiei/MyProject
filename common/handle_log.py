"""
============================
Author:向飞
Time:2020/12/11 21:09
E-mail:947985203@qq.com
============================
"""
import logging
from common.handle_config import conf
from common.handle_path import LOGS_DIR
import os
def create_log(name='xianfei',level='DEBUG',filename='mylog',sh_level='INFO',fh_level='INFO'):
    # 第一步：创建日志收集器
    log=logging.getLogger(name)
    # 第二步：设置收集器收集日志的等级
    log.setLevel(level)
    # 第三步：设置输出日志输出渠道
    # 3.1 输出到文件
    fh=logging.FileHandler(filename,encoding='utf-8')
    fh.setLevel(fh_level)
    log.addHandler(fh)
    # 3.2 输出到控制台
    sh=logging.StreamHandler()
    sh.setLevel(sh_level)
    log.addHandler(sh)
    # 第四步：设置日志输出的格式内容
    fmt = '%(asctime)s %(name)s %(levelname)s %(filename)s-%(lineno)d line:%(message)s'
    format=logging.Formatter(fmt)
    # 4.1为输出渠道设置输出格式
    fh.setFormatter(format)
    sh.setFormatter(format)
    # 返回一个日志收集器
    return log
log=create_log(conf.get('logging','name'),conf.get('logging','level'),
               filename=os.path.join(LOGS_DIR,conf.get('logging','filename')))

