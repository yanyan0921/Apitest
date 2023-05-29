import pytest as pytest
from common.send_request import SendRequest
from common.yaml_util import write_yaml, read_testcase_yaml, read_yaml


class TestApi:
    # 获取鉴权码
    @pytest.mark.parametrize("caseinfo", read_testcase_yaml("/testcase/get_token.yaml"))
    def test_get_token(self, caseinfo):
        print("---------------------")
        name = caseinfo["name"]
        method = caseinfo["request"]["method"]
        url = caseinfo["request"]["url"]
        params = caseinfo["request"]["params"]
        headers = caseinfo["request"]["headers"]
        validate = caseinfo["validate"]
        print("------------------------")

        res = SendRequest().all_send_request(method=method, url=url, params=params)
        result = res.json()
        print(result)
        if "access_token" in result.keys():
            write_yaml({"access_token": result["access_token"]})

    # 编辑标签接口
    def test_edit_flag(self):
        url = "https://api.weixin.qq.cpm/cgi-bin/tags/update?accsee_token=" + read_yaml("access_token")
        datas = {"tag": {"id": 134, "name": "广东人"}}
        res = SendRequest().all_send_request(method="post", url=url, json=datas)
        print(res.json())

    def test_file_upload(self):
        url = "https://api.weixin.qq.cpm/cgi-bin/media/uploadimg?accsee_token=" + read_yaml("access_token")
        datas = {
            "media": open("E:\\shu.jpg", mode="rb")
        }
        res = SendRequest().all_send_request(method="post", url=url, files=datas)
        print(res.json())
