import pytest


# class Test01:
#     """"""
# def setup_class(self):
#     print("setup_class")
#
# def teardown_class(self):
#     print("teardown_class")
#
# def setup(self):
#     print("setup")
#
# def teardown(self):
#     print("teardown")

# # 测试方法
# @pytest.mark.run(order=2)
# def test02(self):
#     print("test022被执行")
#
# # 测试方法
# @pytest.mark.run(order=1)
# def test03(self):
#     print("test03被执行")
# @pytest.fixture()
# def b():
#     print("")
#     print("b")
# @pytest.mark.usefixtures("b")
# class TestFixture:
#     # 1. 将普通函数设置成工厂函数
#     # @pytest.fixture()  # 默认为函数级别
#     # def befor(self):
#     #     print("before被执行")
#
#     def test001(self):
#         print("")
#         print("test001被执行")
#
#     # 2. 调用工厂函数 ->1. 参数形式调用
#     def test002(self):
#         print("")
#         print("test002被执行")
# @pytest.fixture(autouse=True,scope="class")
# def b():
#     print("")
#     print("b")
#
# class TestFixture:
#     # 1. 将普通函数设置成工厂函数
#     # @pytest.fixture()  # 默认为函数级别
#     # def befor(self):
#     #     print("before被执行")
#
#     def test001(self):
#         print("")
#         print("test001被执行")
#
#     # 2. 调用工厂函数 ->1. 参数形式调用
#     def test002(self):
#         print("")
#         print("test002被执行")
# @pytest.fixture(params=[1,2,3])  # 默认为函数级别
# def befor(request):
#     return request.param
#
#
# class TestFixture:
#
#     def test001(self, befor):
#         print("")
#         print("befor:", befor)
#         print("test001被执行")
# version = 3.9
# class TestFixture:
#
#     def test001(self):
#         print("test001被执行")
#
#     @pytest.mark.xfail(version>=3.0,reason="跳过该测试用例")
# #     def test002(self):
# #         print("test002被执行")
# def add():
#     return True
#
#
# class TestFixture:
#
#     def test001(self):
#         print("test001被执行")
#
#     @pytest.mark.xfail(add, reason="当前用例未实现")
#     def test002(self):
#         print("test002被执行")
"""多个参数引用"""
class TestLogin02:
    # 第二步：装饰器 修饰
    # @pytest.mark.parametrize("username,pwd",[("user001","123456"),("user002","1234567")])
    # @pytest.mark.parametrize("username","pwd",[("user001","123456"),("user002","1234567")]) # 错误写法
    @pytest.mark.parametrize("username,pwd,expect",[("user001",123456,"0k"),("user001",1234567,"0k")])
    def test_login(self, username, pwd, expect):
        print("username:", username)
        print("pwd:", pwd)