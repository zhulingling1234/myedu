
import os

# os 常用方法演示
def os_demo():
    # 获取当前目录的路径
    getcwd = os.getcwd()
    print(getcwd)

    # 获取上级目录的路径
    abspath = os.path.abspath('..')
    print(abspath)

    # 获取上级目录的路径
    abspath1 = os.path.abspath('../..')
    print(abspath1)

#  open 方法演示
def open_demo():
    text_io = open('../test.text', 'w+')
    text_io.write("哈哈哈哈啊哈哈")

def open_demo1():
    text_io = open('../test.text', 'a+')
    text_io.write("吾问无为谓")

def open_demo2():
    # 相对路径 ../ test.text
    # 绝对路径  C:\Users\YSL\PycharmProjects\myedu\test.text
    #  r 代表只读模式 不可写入
    # w+  代表读写模式， 写入时会覆盖 原文档内容
    text_io = open('../test.text', 'w+')
    # 读取第一行
    readline = text_io.readline()
    print(readline)
    # 读取所有行 返回一个list 对象
    readlines = text_io.readlines()
    print(readlines)


if __name__ == '__main__':
    # 相对路径 ../ test.text
    # 绝对路径  C:\Users\Administrator\venv\Scripts\python.exe

    text_io = open('test.text', 'w+')



