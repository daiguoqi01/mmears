import pytest,requests,jsonpath



def session():
    s=requests.session()
    return s

def test_login(s=session()):

    url = "https://apistaging.mmears.com/auth/login"
    data = {
        "code": 123456,
        "email":"yujiao@mmears.com",
        "password": "eXVqaWFvMTIzNDU2"
    }
    res = s.post(url=url, data=data).json()
    token=jsonpath.jsonpath(res,"$..token")
    print(token[0])
    h = {
        "x-app-id": "1",
        "x-auth-token": token[0]
    }
    s.headers.update(h)

if __name__ == '__main__':
    #s=session()
    test_login()





