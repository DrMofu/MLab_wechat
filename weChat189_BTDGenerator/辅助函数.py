import random,re,os
import requests,json
def 随便选一个元素(列表):
    return random.choice(列表)

def 随便来一个数(最小值,最大值):
    数 = random.randint(最小值,最大值)
    return 数

def 另起一段():
    内容 = "<br/><br/>"
    return 内容

def 生成标题(大废话,前置标题数据库,后置标题数据库):
    前置标题 = 随便选一个元素(前置标题数据库)
    后置标题 = 随便选一个元素(后置标题数据库)

    标题 = 前置标题 + 大废话 + "。" + 后置标题
    标题 = 标题.replace("d",str(随便来一个数(最小值 = 0,最大值 = 100)))
    return 标题

def 读JSON文件(文件名):
    with open(文件名,mode='r',encoding="utf-8") as 文件:
        return json.loads(文件.read())

def 生成人名(姓数据库,名数据库,人名长度):
    姓 = 随便选一个元素(姓数据库)
    名 = ""
    for 循环 in range(0,人名长度-1):
        名 += 随便选一个元素(名数据库)
    return 姓+名
    
def 爬取图片(大废话):
    搜图地址 = "https://pic.sogou.com/pics?start=0&reqType=ajax&query="
    回复 = requests.get(搜图地址+大废话)
    收到数据 = json.loads(回复.text)
    图片地址列表 = []
    for 数据 in 收到数据['items']:
        图片地址列表.append(数据['ori_pic_url'])
        
    while True:
        random.shuffle(图片地址列表)
        for 图片地址 in 图片地址列表:
            yield "<br/><br/><div style='text-align: center;'><img src='图片地址' style='max-width: 100%;max-height: 100%;'></div><br/>".replace("图片地址",图片地址)

def 来点废话(大废话,正文废话,专家名称):
    while True:
        random.shuffle(正文废话)
        for 废话 in 正文废话:
            yield 废话.replace('x',大废话).replace('r',专家名称)

def 加上结论(大废话,狗屁结论):
    return "<br/><br/>"+随便选一个元素(狗屁结论).replace('x',大废话)
