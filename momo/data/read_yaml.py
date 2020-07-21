import yaml
import os,json


cur_path=os.path.dirname(os.path.realpath(__file__))
#print(cur_path)
yaml_path=os.path.join(cur_path,"test_data.yaml")
print(yaml_path)


def read_yaml_data():
    #f = open(yaml_path, "r", encoding="utf-8")
    f = open('../data/test_data.yaml',"r",encoding="utf-8")
    data=f.read()
    d=yaml.load(data,Loader=yaml.FullLoader)
    return d



if __name__ == '__main__':
    cur_path = os.path.dirname(os.path.realpath(__file__))
    #print(cur_path)
    yaml_path = os.path.join(cur_path, "test_data.yaml")
    #print(yaml_path)
    d=read_yaml_data()
    print(d)

