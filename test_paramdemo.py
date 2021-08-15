import pytest


"""@pytest.fixture(params=["a", "b"])
def demo_fixture(request):
    print(request.param)"""

"""
def test_login(demo_fixture):
    print("Login Successful")
"""


@pytest.mark.skip
def test_logoff():
    print("Login Successful")


@pytest.mark.parametrize("a,b, final", [(2, 3, 5), (3, 5, 8), (2, 6, 11)])
def test_sum(a, b, final):
    assert a+b == final

