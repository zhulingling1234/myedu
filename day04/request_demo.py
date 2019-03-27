
# 导入 requests （第三方类库）
import requests




if __name__ == '__main__':
    # 声明 login_data 变量名 用来存 登录的请求数据
    login_data = {"username":"admin","password":"123456"}
    # =后面是请求的网址（）url 格式为json  login_data 为请求数据 ； = 前面是赋予的名字 用于储存 数据
    login_response = requests.post(url='http://192.168.60.132:8080/admin/login', json=login_data)
    #  获取 login_response 的类型 并打印
    print(type(login_response))
    # login_response.text 为请求正文
    login_response_text = login_response.text
    # 打印 login_response_text
    print(login_response_text)
    # 获取响应正文 （ 字典格式） 必须为 json 格式
    login_response__json = login_response.json()
    #  取出响应正文中 key 为 message 的值
    print(login_response__json['message'])
