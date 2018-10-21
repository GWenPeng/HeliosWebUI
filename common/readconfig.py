import  os
import configparser



def Readconfig(name):
        #配置文档读取函数
        cf=configparser.ConfigParser()
        #file_path=os.path.dirname(os.getcwd())+'/config/config.ini'
        parpath=os.path.abspath('.')
        parpath=os.path.dirname(parpath)
        ConfigPath=parpath+'\\config\\config.ini'
        cf.read(ConfigPath)
        #获取配置文件中BrowserName对应的值
        browserconfig=cf.get('browser',name)
        return browserconfig











