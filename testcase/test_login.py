import time
import pytest

from common.send_request import SendRequest
from common.yaml_util import write_yaml, read_testcase_yaml


class TestLogin:
    pass

    @pytest.mark.parametrize("caseinfo", ["百里", "北凡", "星瑶"])
    def test_login(self, caseinfo):
        print("登录接口：" + caseinfo)

    @pytest.mark.parametrize("name,age", [["百里", "13"], ["北凡", "12"], ["星瑶", "11"]])
    def test_register(self, name, age):
        print("注册接口：%s" % name, age)
