import pytest
import requests,jsonpath
#s=requests.session()

@pytest.fixture(scope="session",autouse=True)
def s():
    s = requests.session()
    return s

@pytest.fixture(scope="session",autouse=True)
def login(s,code=123456,email="yujiao@mmears.com",password="eXVqaWFvMTIzNDU2"):
    url = "https://apistaging.mmears.com/auth/login"
    data = {
        "code": code,
        "email": email,
        "password":password
    }

    res = s.post(url=url, data=data).json()
    #print(res)
    token=jsonpath.jsonpath(res,"$..token")
    #print(token[0])
    h={
        "x-app-id": "1",
        "x-auth-token":token[0]
    }
    s.headers.update(h)









# if __name__ == '__main__':
#     pytest.main(["s","conftest.py"])


