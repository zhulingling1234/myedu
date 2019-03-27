
# 步长

def list_bianli():
    alist = ['哈哈','好','密码','余余']
    for i in alist:
        print("--遍历")
        print(i)
        print(i + 'hello')


def chenfabiao():
    for i in range(1,10):
        for j in range(1,i+1):
            print('%s * %s = %s' %(i,j,i*j),end=' ')
        print(' ')
#  基础 if else 语法演示
def if_demo():
    a = False
    if a:
        print('a 是 对的')
    else:
        print('a 是 错的')

# 判断 a 和 b 的大小
def if_demo1():
    a = 10
    b = 20
    if a>b:
        print('a 大于 b')
    else:
        print('a 小于 b')


# 输出 比较大的值
def if_demo2():
    a = 10
    b = 20
    if a>b:
        print('a')
    else:
        print('b')

# 取余

def jisuan(a,b):
    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)
    print(a % b)

def duibi(a,b,c):
    print(a > b)
    print(a < b)
    print(a == b)
    print(a == c)
    print(a >= b)
    print(a != b)

def deng(a):
    a += 1  # a = a+1
    print(a)
    a *= 2  # a = a*2
    print(a)
    a -= 5  # a = a-5
    print(a)
    a /= 2  # a = a/2
    print(a)


if __name__ == '__main__':
     # for i in range(5):
     #    print('hello world')
     #      for j in range(2):
     #        print('内循环')
    # for i in range(1,10):
    #     for j in range(1,i+1):
    #         print('%s * %s = %s' %(i,j,i*j),end=' ')
    #     print(' ')
    #  a = 10
    #  b = 20
    #  if a > b:
    #      print('a')
    #  else:
    #      print('b')
    #  将 1到 50 的奇数 加起来
    nub = 0
    for i in range(1,51):
        if i%2 !=0:
            nub = nub+i
    print(nub)
    for i in range(5):
        print('hello world')






