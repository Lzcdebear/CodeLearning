import json
jsonString = '{"arrayOfNums":[{"number":0},{"number":1},{"number":2}],"arrayOfFruits":[{"fruit":"apple"},{"fruit":"banana"},{"fruit":"pear"}]}'
jsonObj = json.loads(jsonString)	#载入JSON格式字符串，返回字典对象
print(jsonObj.get("arrayOfNums"))	#获取字典中key为arrayOfNums的值
print(jsonObj.get("arrayOfNums")[1]) #获取字典中key为arrayOfNums的值（列表）的第1个元素
print(jsonObj.get("arrayOfNums")[1].get("number"))
print(jsonObj.get("arrayOfFruits")[1].get("fruit"))
