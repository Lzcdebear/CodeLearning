keywords = '''
False               class               from                or
None                continue            global              pass
True                def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
break               for                 not
'''
s = input('变量名：')
checked = False
# 判断首字母
if s[0] == '_' or 97 <= ord(s[0]) <= 122 or 65 <= ord(s[0]) <= 90:
  # 判断其他字符是否符合规则
  for i in s[1:]:
      if i != '_' and not i.isalnum():
          checked = False
          break
  else:
      if s in keywords:
          checked = False
      else:
          checked = True
if checked:          
      print('变量名合法')
else:
    print('变量名不合法')
