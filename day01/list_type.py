# 全局变量
blist = [2,5,8,6,11]
# 声明一个 list_demo 方法
def list_demo():
    # 局部变量
    alist = [4, 'ysl', '8', 7]
    print(alist)
    # 通过索引访问 元素
    print(alist[0])
    print(alist[1])
    # 倒序访问
    print(alist[-1])
    print(alist[-2])
    print(blist)

# 更新列表中的元素
def list_update(alist):
    alist[0] = 1
    print(alist[0])
    print(alist)

# 切片操作
def list_update1(alist):
    # 从索引2 的位置 取 到索引5
    print(alist[2:6])
    # 从索引0 的位置 取 到索引5
    print(alist[:6])
    # 从索引3 的位置 取 到索引末尾
    print(alist[3:])


# 删除方法  list.pop()
def pop_demo(alist):
    # 打印 alist.pop()
    # pop（）方法两个作用 第一个取出最后一位的值，第二个从列表中
    print(alist.pop())
    print(alist)
    alist . pop(4)
    print(alist)

# 讲列表排序的方法
def orderby_demo():
    print('调用正序排的方法')
    sort_demo()
    print('调用倒序排的方法')
    reverse_demo()


    pass
# 正序方法
def sort_demo():
    # 将blist 正序排列
    blist.sort()
    print(blist)

    pass
def reverse_demo():
    # 将blist倒序排
    blist.reverse()
    print(blist)
    pass

# 列表/集合
if __name__ == '__main__':
    alist = [4, 'ysl', '8', 7,6,2,5]
    # list_update1(alist)
    # list_update(blist)
    # pop_demo(alist)
    # print(blist.pop(4))
    # alist.pop(4)
    # print(alist)
    orderby_demo()