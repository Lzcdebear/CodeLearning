#filename: sample7-2-1.py
import json
jsonString = '{"arrayOfNums":[{"number":0},{"number":1},{"number":2}],\
"arrayOfFruits":[{"fruit":"apple"},{"fruit":"banana"},{"fruit":"pear"}]}'
jsonObj = json.loads(jsonString)	#载入JSON格式字符串，返回字典对象
print(jsonObj.get("arrayOfNums"))	#获取字典中key为arrayOfNums的值（该值为数组）
#获取字典中key为arrayOfNums的值（数组）的第1个元素（该元素为字典对象）
print(jsonObj.get("arrayOfNums")[1]) 
#获取字典中key为arrayOfNums的值（数组）的第1个元素中（字典对象）中key为"number"的值
print(jsonObj.get("arrayOfNums")[1].get("number"))
