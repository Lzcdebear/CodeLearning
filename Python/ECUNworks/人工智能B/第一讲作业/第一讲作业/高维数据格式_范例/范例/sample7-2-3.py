#filename: sample7-2-3.py
import json
f = open('stus.json', encoding="utf-8")
jsonObj = json.load(f)    #直接载入文件对象
print(jsonObj )
