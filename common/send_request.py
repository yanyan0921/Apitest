import requests


class SendRequest:
    sess = requests.session()

    def all_send_request(self, method, url, **kwargs):
        print("------接口测试开始--------------")
        print("请求方式： %s" % method)
        print("接口地址： %s" % url)
        if "params" in kwargs.keys():
            print("请求params参数： %s" % kwargs["params"])
        if "json" in kwargs.keys():
            print("请求json参数： %s" % kwargs["json"])
        if "files" in kwargs.keys():
            print("请求files参数： %s" % kwargs["files"])
        res = SendRequest.sess.request(method, url, **kwargs)
        print("接口返回: %s" % res.text)
        print("--------接口测试结束------------")
