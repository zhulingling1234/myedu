#  class 类
# oject 对象 / 或者所有类的父类

#  声明类的语法 ：class ：就是声明一个类 ； Human :类的名字 ； ()：括号里面填 这个类的父类
#  类 开头大写 （规范写法） eg : Human
class Human(object):
    #  类的初始化方法  self ： 代表类本身
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
    #  方法是驼峰式  第二个字母开头大写  以此类推
    def myInfo(self):
        print('我叫%s,我今年%s岁，%s'%(self.name,self.age,self.sex))

#   继承

class Tester(Human):
    def zhiXingCeShi(self):
        print(self.name)
        print('我在执行测试，别打扰我')
        self.myInfo()


if __name__ == '__main__':
    # = 后面
    # human = Human('zhull',23,'女')
    # print(type(human))
    # # 对象可使用类中的方法
    # human.myInfo()
    #    继承
    tester = Tester('zll',23,'女')
    tester.zhiXingCeShi()
    print(type(tester))






