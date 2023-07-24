import json

j_str1='{"firstName":"Json"}'
dt_1=json.loads(j_str1)  #字符串转对象
print(dt_1,type(dt_1))

j_str2=json.dumps(dt_1)  #对象转字符串
print(j_str2,type(j_str2))

dt_2={"姓名":"张三"}
#j_str2=json.dumps(dt_2)
j_str2=json.dumps(dt_2,ensure_ascii=False) #序列化时不使用默认的ascii编码以输出中文
print(j_str2,type(j_str2))
