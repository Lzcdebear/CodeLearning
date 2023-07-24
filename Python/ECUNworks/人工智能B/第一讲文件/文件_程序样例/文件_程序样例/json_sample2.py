import json

json_book='''{"书名":"数据科学技术与应用","手机":"978-7-121-34655-1",
"作者":[{"姓名":"宋晖","邮箱":"hsong@163.com"},{"姓名":"刘晓强","邮箱":"xqliuwith@hotmail.com"}],
"价格":35.00,"出版年份":2018}'''
dt_book=json.loads(json_book)  #字符串转对象
print(dt_book)
print(type(dt_book))

with open("bookinfo.json","w",encoding="utf-8") as fw:
    json.dump(dt_book,fw,ensure_ascii=False)    #对象转字符串并写入文件
