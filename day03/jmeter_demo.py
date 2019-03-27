import requests

if __name__ == '__main__':

    login_data = {"username": "admin", "password": "123456"}
    login_resp = requests.post(url='http://192.168.60.132:8080/admin/login', json=login_data)
    login_json = login_resp.json()
    print(login_json)

    # 提取响应中的data 的值(这是一个字典类型的值)
    data_dict = login_json['data']
    # 提取 data_dict 字典 中 tokenHead 的值
    token_head = data_dict['tokenHead']
    # 提取 data_dict 字典 中 token 的值
    token_ = data_dict['token']
    # 封装 请求头
    head = {'Authorization': token_head + ' ' + token_}

    # 发起 Info 请求 , 传入指定参数 headers 值为 head
    info_resp = requests.get(url='http://192.168.60.132:8080/admin/info', headers=head)
    info_json = info_resp.json()
    print(info_json)

    # 获取订单列表
    response = requests.get('http://192.168.60.132:8080/order/list?pageNum=1&pageSize=10&status=1&orderType=', headers=head)
    print(response.text)
    response_json = response.json()
    json_data_ = response_json['data']
    list_ = json_data_['list']
    list__1 = list_[0]
    order_id = list__1['id']

    # 发货
    fahuo_data = [
                  {
                    "deliveryCompany": "顺丰",
                    "deliverySn": "22222",
                    "orderId": order_id
                  }
                ]
    requests_post = requests.post('http://192.168.60.132:8080/order/update/delivery', headers=head,json=fahuo_data)
    print(requests_post.text)
    json = requests_post.json()

    # 关闭订单
    close_param = {'ids':order_id,'note':'guggg'}
    get = requests.post('http://192.168.60.132:8080/order/update/close',params=close_param, headers=head)
    print(get.text)
    json1 = get.json()