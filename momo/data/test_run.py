from data.read_yaml import read_yaml_data
import json
import os
def test_cret(s):
    url = "https://apistaging.mmears.com/auth/supportwxrel/wxqrcode/upload"
    url2 = "https://apistaging.mmears.com/auth/supportwxrel/wxqrcode/save"

    data = {
        'file': open("D:/pingguo/images.jpg", "rb")
    }


    '''上传图片'''
    rec = s.post(url=url, files=data).json()
    print(rec)
    b = rec.get('data')
    #print(b)
    data1 = {
        "url": b,
        "wxNo": "fshafh"

    }
    '''保存图片'''
    respont = s.post(url=url2, json=data1).json()
    #print(respont)


cur_path=os.path.dirname(os.path.realpath(__file__))
#print(cur_path)
yaml_path=os.path.join(cur_path,"test_data.yaml")
print(yaml_path)

def test2(s):
    '''创建账号'''
    param=read_yaml_data()['test']
    print(param)
    url="https://apistaging.mmears.com/customer/studentocean/savestudent"
    res=s.post(url=url,json= param).json()
    print(res)
