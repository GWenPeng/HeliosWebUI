# 获取URL函数
def geturl(url):
    urls=url.split('/')
    urls=urls[0]+'//'+urls[2]+'/'+urls[3]+'/'
    return  urls
