
# import pytest


# @pytest.fixture(scope="package")
# def order():
#     return []


# @pytest.fixture(scope="package")
# def a(order):
#     order.append("a")


# @pytest.fixture(scope="package")
# def b(a, order):
#     order.append("b")


# @pytest.fixture(scope="package")
# def c(b, order):
#     order.append("c")


# @pytest.fixture(scope="package")
# def d(c, order):
#     order.append("d")


# @pytest.fixture(scope="package")
# def e(d, order):
#     order.append("e")


# @pytest.fixture(scope="package")
# def f(e, order):
#     order.append("f")


# @pytest.fixture(scope="package")
# def g(f,order):
#     order.append("g")

# class TestMain:
#     def test_order(self, g,f,e,d,c,b,a,order):
#         assert order == ["a", "b", "c", "d", "e", "f", "g"]

# # import pytest


# # @pytest.fixture(scope="session")
# # def order():
# #     return []


# # @pytest.fixture
# # def func(order):
# #     order.append("function")


# # @pytest.fixture(scope="class")
# # def cls(order):
# #     order.append("class")


# # @pytest.fixture(scope="module")
# # def mod(order):
# #     order.append("module")


# # @pytest.fixture(scope="package")
# # def pack(order):
# #     order.append("package")


# # @pytest.fixture(scope="package")
# # def sess(order):
# #     order.append("session")


# # class TestClass:
# #     def test_order(self, func, cls, mod, pack, sess, order):
# #         assert order == [ "package","session", "module", "class", "function"]