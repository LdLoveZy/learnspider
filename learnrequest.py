# -- coding: utf-8 --
import requests

response = requests.get("https://www.baidu.com")
print(type(response))
print(response.status_code)
print(type(response.text))
print(response.text)
print(response.cookies)

#各种请求方式
#requests.post()
#requests.delete()
#requests.put()
#requests.get()

#get请求带参数
data = {
    'name': 'Ld',
    'age': 22,
    'sex': 'man'
}
response = requests.get("http://httpbin.org/get", params=data)
print("带请求参数的get")
print(response.text)

#解析json
response = requests.get("http://httpbin.org/get")
print("解析json串")
print(response.json())

#获取二进制数据
response = requests.get("https://www.baidu.com/img/bd_logo1.png")
print("获取二进制数据")
print(response)