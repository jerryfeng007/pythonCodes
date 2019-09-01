import logging

'''
# 输出到指定的文件内
logging.basicConfig(filename=log_file, level=logging.DEBUG, format=log_format, filemode='w')

# 如果不写 filename和filemode 则默认打印到console
# logging.basicConfig(level=logging.DEBUG, format=log_format)

# log level
# logging.CRITICAL>logging.ERROR>logging.WARNING>logging.INFO>logging.DEBUG
# 如果设置为info,则打印info及它以上级别的日志
'''

print('---------------------把日志打印到console，且写入到文件-----------------------------------')


def the_log(log_file):

    # 创建一个logger
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # 创建一个handler，将log写入文件
    fh = logging.FileHandler(log_file, mode='w')
    fh.setLevel(logging.INFO)

    # 创建一个handler，将log输出到控制台
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)

    # 设置log格式
    log_format = '%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s: %(message)s'
    formatter = logging.Formatter(log_format)
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    # 把handler添加到logger里，理解为汇报给大领导即可
    logger.addHandler(fh)
    logger.addHandler(ch)

    return logger


file = 'log_log.txt'
logger = the_log(file)

# 输出具体的日志信息
logger.debug('debug message挨踢脱口秀')
logger.info('info message挨踢脱口秀')
logger.warning('warning message88小强测试品牌')
logger.error('error message测试帮日记')
logger.critical('critical message小强测试品牌')
