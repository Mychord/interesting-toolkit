#!python3
# coding=utf8
import json
import uuid
# 定义JSON文件路径
# json_file_path = './tianqing.json'

# 使用json.load()方法读取JSON文件并将其转换为Python对象
# with open(json_file_path, 'r') as json_file:
#     data = json.load(json_file)
#     print(data)


class Website: 
    def __init__(self, id, data):
        self.id = id
        self.data = data

data = [
    '网站:独特工具箱  <a href="https://www.dute.org/">点击打开查看</a>',
    '网站:自由钢琴  <a href="https://www.autopiano.cn/">点击打开查看</a>',
    '网站:doyoudo  <a href="https://www.doyoudo.com/">点击打开查看</a>',
    '网站:知乎  <a href="https://www.zhihu.com/">点击打开查看</a>'
]
# 定义要保存JSON的文件路径
json_file_path = './resource/datas/websites.json'

arr = []
for str in data: 
    id = uuid.uuid3(uuid.NAMESPACE_URL, str)
    print(id)
    website = Website(id, str)
    arr.append(website) 

# 使用json.dump()方法将Python对象转换为JSON并保存到文件中
with open(json_file_path, 'w') as json_file:
    json.dump(arr, json_file, ensure_ascii=False, indent=4)
