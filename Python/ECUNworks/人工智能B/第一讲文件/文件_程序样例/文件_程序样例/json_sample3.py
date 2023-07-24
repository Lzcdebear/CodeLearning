import json

with open("bookinfo.json","r",encoding="utf-8") as fr:
    dt_book2=json.load(fr)    #从json文件读取并转json对象（字典）
print(dt_book2)

print(dt_book2.get("手机"))
print(dt_book2.get("作者")[0].get("邮箱"))

print("作者：")
for d in dt_book2.get("作者"):
    print(d.get("姓名"),"\t",d.get("邮箱"))
