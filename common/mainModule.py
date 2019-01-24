import logging
import os.path
import time

# class Logger(object):
#     def __init__(self):
#         '''指定保存日志文件路径，日志级别，以及调用的文件将日志存入
#         指定的文件中
#         :param logger:
#         '''
        #创建一个logger
        # self.logger=logging.getLogger("mainModule")
logger=logging.getLogger("mainModule")
logger.setLevel(logging.INFO)


        #创建一个handler,用于写入日志文件
#print(log_path)
        # file_hanlder = logging.FileHandler(filename='example.log', encoding='utf-8')
rq=time.strftime('%Y%m%d%H%M',time.localtime(time.time()))
log_path=os.path.abspath('.')+'/logs/'
log_name=log_path+rq+'.log'
formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
handler =logging.FileHandler(log_name,encoding='utf-8')
handler.setLevel(logging.INFO)
handler.setFormatter(formatter)
console =logging.StreamHandler()
console.setLevel(logging.INFO)
console.setFormatter(formatter)
#写入文件handler
logger.addHandler(handler)
#控制台输出
logger.addHandler(console)


    # def getlog(self):
    #     return self.logger
