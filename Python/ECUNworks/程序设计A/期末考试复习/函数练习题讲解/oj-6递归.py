#1） 使用递归求斐波那契数列第n项的值
#2） 使用全局变量，统计递归函数调用次数
#3）改进递归调用算法，提高递归运算效率 
#提示：定义字典，使用字典保存以求出的斐波那契数
# pn = pn-1 + pn-2
# p0=0,p1=1
def fibonacci(n):
    if n ==0 or n == 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def fibonacci(n):
    global count
    count = count + 1
    if n in pre_dict:  # in 检查字典中是否有某个key
        return pre_dict[n]
    else:
        val = fibonacci(n-2) + fibonacci(n-1)
        pre_dict[n] = val
        return val

pre_dict  =  {0:0,1:1}
count = 0
num  =  int(input())
fib = fibonacci(num)
print(f"fib={fib},count={count}")