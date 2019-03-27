# 声明一个全量 dict 变量 （字典）

adict = {"name":"ysl","pwd":"123456"}

# 这是一个字符串，不过他是json 格式，也是字典的格式
adictstr = '{"name":"ysl","pwd":"123456","1":"数字1"}'
import json

# str --> dict 字符串 转 dict
def zhuanhuanleixing():
    pass



def china_demo():
    loads = json.loads(adictstr)
    print(type(loads))



if __name__ == '__main__':
     # print(adict)
     # adict.pop('name')
     # print(adict['name'])
     # print(adict)
     loads = json.loads(adictstr)
     print(type(loads))
     loads = json.loads(adictstr)
     dumps = json.dumps(loads, ensure_ascii=False)
     print(dumps)
     print(adict)
     print(adict['name'])
     adict.pop('name')
     print(adict)
