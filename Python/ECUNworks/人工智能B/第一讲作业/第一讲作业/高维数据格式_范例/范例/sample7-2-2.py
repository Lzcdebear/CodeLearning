#filename: sample7-2-2.py
import json
f = open('stus.json', encoding='utf-8')  #该JSON文件的编码格式是utf-8，指定用这种编码格式来打开文件
content = f.read() 	#使用loads（）方法需要先读文件
jsonObj = json.loads(content)
print(jsonObj )    #打印JSON对象（jsonObj）的字符串表示
