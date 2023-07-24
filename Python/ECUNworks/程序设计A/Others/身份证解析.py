ids=input("请输入身份证号码：") 
#"309012199606230083"
year = ids[6:10]
month = ids[10:12]
day = ids[12:14]
sex = ids[-2]

sex = int(sex) % 2

#构造生日 
birthday=f"{year}年{month}月{day}日"

if sex == 1:
   msg2 = '男'
else:
   msg2 = '女'
#构造输出字符串 
msg=f"出生年月:{birthday},性别:{msg2}"

print(msg)