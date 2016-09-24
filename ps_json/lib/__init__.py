# coding: utf-8

import os
import sys,codecs,json

def test_path(path):
    if not os.path.exists(path):
        print(path + " は存在しません。")
        sys.exit(1)

def get_json(path):
    with codecs.open(path,"r",encoding="utf-8")as file:
        result=json.load(file)

    return result

def set_json(path,obj):
    with codecs.open(path,"w",encoding="utf-8")as file:
        json.dump(obj,file,sort_keys=True,indent=2,ensure_ascii=False)

def set_key(path,key_name,value):
    if value.isdigit():
        value=int(value)
    elif value.lower()=="true":
        value=True
    elif value.lower()=="false":
        value=False
    else:
        value=value.decode("utf-8")

    if os.path.isfile(path):
        json_obj=get_json(path)
        json_obj[key_name]=value
    else:
        json_obj={key_name:value}

    set_json(path,json_obj)

def remove_key(path,key_name):
    test_path(path)
    json_obj=get_json(path)

    if not key_name in json_obj:
        print(key_name+" は存在しません。")
        sys.exit(1)

    json_obj.pop(key_name)
    set_json(path,json_obj)

def get_key_list(path):
    test_path(path)

    json_obj=get_json(path)
    key_list=[]

    for key_name in json_obj:
        key_list.append(key_name)

    key_list.sort()
    return key_list

def get_key_value(path,key_name):
    test_path(path)
    json_obj=get_json(path)

    if not key_name in json_obj:
        print(key_name+" は存在しません。")
        sys.exit(1)

    result=json_obj[key_name]
    return result
