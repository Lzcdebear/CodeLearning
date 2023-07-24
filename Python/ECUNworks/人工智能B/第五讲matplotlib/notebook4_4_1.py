# coding=utf-8
import matplotlib.pyplot as plt
import numpy as np

'''
matplotlib进行图形的绘画的步骤一般是
创建画布、子图
准备数据
添加画布内容
保存绘制图形
'''

# 坐标系的创建
'''
matplotlib中的坐标轴一般有 x 和 y 
'''

# 准备数据
x = np.arange(-1 * np.pi, 2 * np.pi, 0.01)  #准备[−π,2π]间隔0.01的数组
y = np.sin(x)
# 添加画布内容
plt.title('y = sin(x)')              #图表标题
plt.xlabel('x')                      #x轴标题
plt.ylabel('y')                      #y轴标题
#绘制图形
plt.plot(x, y)                       #绘制曲线图
plt.grid()                           #绘制网格线
plt.savefig("sinx.png")              #保存图形文件
plt.show()                           #显示图形

'''
2. 图元属性设置
  图形的精细控制，可以通过设置Pyplot的rcParams参数和plot函数的format_string参数值获得不同格式的曲线图。

（1）设置rcParams参数   
Pyplot使用rcParams配置文件来自定义图形的各种属性，
	视图窗口的大小
	每英寸点数
	线条样式和宽度
	颜色
	坐标轴
	文本
	字体
线条常用rcParams参数如表4-4-2所示。

  例如设置线型：plt.rcParams["lines.linestyle"]="-."image.png
'''

'''
其中常用的 rcParams参数和函数
lines.linewidth		线条宽度								0 - 10，默认是1.5
lines.linestyle		线条样式								4种样式
-、--、-.、:、
lines.martker		线条上点的样式							可以取 o D +
lines.markersize	点的大小								0 - 10，默认是1
font.sans-serif		字体类型设置（跟在后面的就是字体名字）	其他具体字体
axes.unicode_minus	负号是否使用unicode编码					True或者False
'''

'''
2）设置plot参数format_string
plot()函数可以基于图元属性进行绘制图形，其常用格式如下所示：
	matplotlib.pyplot.plot(x, y, format_string,…)
其中，format_string数据格式字符串由三项组成，格式为“format_string = '[color][marker][line]'”分别表示绘制的色彩、
数据点的标记或线的格式，其中这三项每一项都是可选的，并可以自由搭配。
'''

'''
颜色color选项
b	蓝色
g	绿色
r	红色
y	黄色
k	黑色

marker选项
.	点
o	圆
+	加号
*	星号
v	实心三角形

line选项
-		实线
--		虚线
-.		点划线
:		点构成的虚线 
'''

# 实验2：绘制函数sin(x)和cos(x) 在[0,2π]上的图形。
import matplotlib.pyplot as plt
import numpy as np

# 准备数据
x = np.arange(0, 2 * np.pi, 0.01)
y1 = np.sin(x)
y2 = np.cos(x)

#设置RC参数
plt.rcParams["lines.linestyle"]="-."        #设置线条样式
plt.rcParams["lines.linewidth"]=3         #设置线条宽度

# 添加画布内容
plt.title('y = sin(x) and y=cos(x)')
plt.xlabel('x')
plt.ylabel('y')

#绘制图形
plt.plot(x, y1,"r")                       #设置线条颜色为红色
plt.plot(x, y2,"k")                       #设置线条颜色为黑色
plt.grid()
plt.show()

# 三. 创建子图（MATLIB方式）
# 实验3：分别使用2个子图绘制函数y=sin(x)和y=cos(x)在[−π,2π]上的图形
import matplotlib.pyplot as plt
import numpy as np
#plt.figure(figsize=(10, 8))  #设置画布尺寸为10*8英尺
x = np.arange(-1 * np.pi, 2 * np.pi, 0.01)
#画第1个子图
plt.subplot(2,1,1) #（行、列、子图编号）
plt.plot(x,np.sin(x))
#画第2个子图
plt.subplot(2,1,2) #（行、列、子图编号）
plt.plot(x,np.cos(x))
plt.show()

# 四. 创建子图（面向对象方式）
'''
使用subplots函数创建子图（面向对象方式）¶
fig, ax = subplots(nrows=1, ncols=1, sharex=False, sharey=False) 返回结果： 
fig：Figure对象（plt.Figure类的实例），可以被看成是一个容纳各种坐标轴、图形、文字和标签的容器。 
ax：Axes(轴)对象或Axes(轴)对象数组。
Axes（plt.Axes类的实例）是一个带有刻度和标签的矩形。
'''

# 实验4：分别使用2个子图绘制函数y=sin(x)和y=cos(x)在[−π,2π]上的图形（面向对象方式）
import matplotlib.pyplot as plt
import numpy as np
#axs是包含两个Axes对象的数组（2行1列布局）
fig, axs = plt.subplots(2,1)
fig.set_size_inches(10,8)   #设置画布大小为10*8英寸
#准备x轴数据
x = np.arange(-1 * np.pi, 2 * np.pi, 0.01)
#在每个对象上调用plot方法
axs[0].plot(x,np.sin(x))
axs[1].plot(x,np.cos(x))
plt.show()

# 实验5：分别使用2个子图绘制4个函数：
# 第一子图包含y=sin(x)和y=cos(x)在[−π,2π]上的图形，
# 第二子图包含y=x^2和y=x^4在[0,1]间的图形（面向对象方式）
fig,axs = plt.subplots(2,2)
fig.set_size_inches(10,8)
x=np.arange(-1*np.pi,2*np.pi,0.01)
y1=np.sin(x)
y2=np.cos(x)
axs[0,0].set(xlabel='x',ylabel='y',title="sin(x)")
axs[0,0].plot(x,y1)
axs[0,0].legend(["y=sin(x)"])
axs[0,0].grid()
axs[0,1].set(xlabel='x',ylabel='y',title="cos(x)")
axs[0,1].plot(x,y2)
axs[0,1].legend(["y=cos(x)"])
axs[0,1].grid()
x=np.arange(0,1.1,0.1)
y1=x**2
y2=x**4
axs[1,0].set(xlabel='x',ylabel='y',title="lines")
axs[1,0].plot(x,y1)
axs[1,0].legend(["y=x^2"])
axs[1,0].grid()
axs[1,1].set(xlabel='x',ylabel='y',title="lines")
axs[1,1].plot(x,y2)
axs[1,1].legend(["y=x^4"])
axs[1,1].grid()
plt.show()

 