
# 导入 requests 第三方包
import requests



if __name__ == '__main__':
    # 封装请求参数
    data = {"username": "admin", "password": "123456"}
    # 发送请求 带上两个参数 url 和 请求正文 json
    response = requests.post(url='http://192.168.60.132:8080/admin/login',json=data)
    test_body = response.text
    print(type(test_body))
    print(test_body)
    json_body = response.json()
    print(type(test_body))
    print(json_body)

    assert 200 == response.status_code
    assert '成功' in json_body['message']
    #  给 code 断言
    assert 200 == json_body['code']

    data_dict = json_body['data']




