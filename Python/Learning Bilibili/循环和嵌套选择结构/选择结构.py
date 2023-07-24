# 这里将会展示选择结构的不同形式和输入方式
# 先用取款展示
money = 1000
a = int(input('请输入取款金额'))
if money >= a:
    print('余额为：  ', money - a)
else:
    print('余额不足')
# 接下来再展示奇偶性分析的一种条件结构，基础就是偶数都可以被2整除
b = int(input('input a number'))
if b % 2 == 0:
    print('这是一个偶数')
else:
    print('这是一个奇数')
# 最后展示的是多分支结构，用到elif，就是前一个条件不成立是判断是否为elif后的条件成立
s = int(input('input a student''s score'))
if 90 <= s <= 100:
    print('A')
elif 80 <= s <= 90:
    print('B')
elif 70 <= s <= 80:
    print('C')
elif 60 <= s <= 70:
    print('D')
elif s <= 60:
    print('E')
else:
    print('Sorry, you wrote a wrong score')
# 最后将要展示的是嵌套结构，运用到的是if里面再加上if，是在第一个if成立之后进行的第二次判断，和上面的分支结构并不一样
# 此处设想一种会员购物的情况
'''如果是会员，则
              >= 200  90%
              >= 300  80%
              其余情况  95%
   如果不是会员，则没有优惠'''
x = int(input('您的消费金额'))
y = input('您是否为会员（是/否）')
if y in '是':
    if x >= 300:
        fin = x * 0.8
    elif x >= 200:
        fin = x * 0.9
    else:
        fin = x * 0.95
else:
    fin = x
print(fin)
# 最后是一种简单方便清洁的选择语句的写法
# 主要内容就是 A if  else B
# 当if成立的时候就会执行A，当if不成立的时候就会执行B
# 以比较数字的大小为例
num_a = int(input('The first number'))
num_b = int(input('The second number'))
print('The num_a is bigger than/equal to the num_b' if num_a >= num_b else 'The num_a is smaller than the num_b')
# 如果一个选择结构中没有if判断的具体内容而只有一个对象，则if自动为判断if后面的对象是否为True如果是False则会跳到else段
age = str(input('your age'))
if age:
    print(age)
else:
    print('your age:' + age)
