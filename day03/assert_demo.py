



def zuihou():
    a = "123456"
    # try 用于异常处理  如果出现异常 则执行 except 内的代码
    try:
        # 判断 a 是否包含 5
        assert '5' in a
    # except 报错后执行
    except:
        print('a里面没有7')
    finally:
        print('最后-----')

def while_demo():
    a = 0
    while a < 5:
        print('hello world')
        a+=1


if __name__ == '__main__':
    astr = '哈我发的密码'
    # assert '我' in astr
    # assert '你' in astr
    try:
        assert '你' in astr
    except:
        print('报错啦，断言没通过')
    finally:
        print('------')












