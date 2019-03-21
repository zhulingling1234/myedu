# 声明一个 int_demo()方法
def int_demo():
    # 声明 aint 变量，赋值 1
    aint = 3
    # 打印 aint 的值
    print(aint)
    # 打印 aint 的类型；type(aint)：获取 aint 类型
    print(type(aint))


# 声明一个 sub 方法 参数有两个 aint,bint
def sub(aint, bint):
    # 打印 aint 参数
    print(aint)
    # 打印 bint 参数
    print(bint)
    # 返回 aint-bint
    return aint - bint


# 声明一个 float_demo()方法
def float_demo():
    # 声明 afloat 变量，赋值 1
    afloat = 3.8
    # 打印 afloat 的值
    print(afloat)
    # 打印 afloat 的类型；type(afloat)：获取 afloat 类型
    print(type(afloat))




if __name__ == '__main__':
    # int_demo()
    # 提取变量 ctrl+alt+v
    # 调用 sub 方法 传入3,2， 得到返回值，赋值给 result 变量
    # result = sub(3, 2)
    # print(result)
    float_demo()
