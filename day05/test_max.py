# 如何使用 pytest 做测试
#  1.设置Pycharm
#  2.新建模块：以 test 开头
#  3.新建类以  test 开头
#  4.在类中新建方法以 test_ 开头





import allure

@allure.feature("类上的装饰器")
class TestYsl:
    @allure.story("max类上装饰器")
    def test_Max(self):
        assert 1<2

    @allure.story("max1方法上装饰器")
    def test_Max1(self):
        assert 3 < 2

    @allure.story("max2类上装饰器")
    def test_Max2(self):
        assert 5 > 2



