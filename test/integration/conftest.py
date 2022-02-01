# test/conftest.py
import pytest

# class Params():
#     def __init__(self, username, password):
#         self.username = username
#         self.password = password

def pytest_addoption(parser):
    parser.addoption("--username", action="store", help="input username")
    parser.addoption("--password", action="store", help="input password")

@pytest.fixture(scope="class")
def params(request):
    # params = Params(request.config.getoption('--username'), request.config.getoption('--password'))
    params = {}
    params['username'] = request.config.getoption('--username')
    params['password'] = request.config.getoption('--password')
    if params['username'] is None or params['password'] is None:
        pytest.skip()
    request.cls.params = params