from data1.login import session,test_login
import jsonpath


def test_cret():
    s=session()
    test_login(s)
    url = "https://apistaging.mmears.com/customer/studentocean/savestudent"
    data={
        "gender": "UNKNOWN", "password": "655555", "contactPhone": "16364655556", "age": 5, "month": 0,
        "birthDate": "2015-06-30T16:00:00.000Z", "nickName": "tgt", "level": 1, "unit": 201, "specialLevel": 1,
        "ccId": 839, "birthYear": "2015", "birthMonth": "07"
    }
    res = s.post(url=url, json=data).json()
    print(res)
    assert jsonpath.jsonpath(res,"$..msg")[0]=='手机号已存在'


def test2():
   '''python作业9：
已知一个队列,如： [1, 3, 5, 7], 如何把第一个数字，放到第三个位置，得到： [3, 5, 1, 7]'''
   s=1
   for i in range(1,100):
       s=i+1
       if s==100:
           print(s)
           break

