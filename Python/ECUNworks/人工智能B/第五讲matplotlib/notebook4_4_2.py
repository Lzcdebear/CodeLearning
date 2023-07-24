# coding=utf-8
'''
4.4.2 常见图表类型
  Matplotlib提供了丰富的图形绘制函数，如scatter（散点图）、plot（折线图）、bar（条形图）、boxplot（箱型图）、pie（饼图）等等。

1. 2D散点图
  2D散点图，顾名思义就是由一些散乱的点组成的2D图表
    这些点在哪个位置，是由其X值和Y值确定的。2D散点图通常用于研究两组变量之间的数据相互关系。
    从散点图可以简单判断两个变量是否有相关关系、相关关系的强弱、是正相关还是负相关、相关的趋势如何等。
    Pyplot模块提供了scatter()函数绘制2D散点图，其常用格式如下所示：

    matplotlib.pyplot.scatter(x, y, s, c, marker,…)

x和y表示散点图的数据源
s表示数据点标记的大小
c表示数据点标记的颜色
marker表示标记的风格。
'''
# 绘制身高体重关系的2D散点图。本例使用data = np.random.multivariate_normal([172, 65], [[55, 35], [35, 45]], 200)语句
# 产生一个身高均值为172厘米，体重均值为65公斤的200行2列的随机实验数据，第1列是身高，第2列是体重。
import numpy as np
import matplotlib.pyplot as plt
plt.title('身高体重关系图')
plt.rcParams['font.sans-serif']=['SimHei'] #避免中文出现乱码
plt.rcParams['axes.unicode_minus']=False

#生成身高体重实验数据
data = np.random.multivariate_normal([172, 65], [[55, 35], [35, 45]], 200) 
heights = data[:, 0]
weights = data[:, 1]

#绘制散点图
p1 = plt.scatter(heights,weights,c='b', s=50, marker='*')
plt.xlabel('身高 (cm)')
plt.ylabel('体重 (kg)')
plt.grid()#显示网格
plt.show()

'''
3. 折线图
  折线图能够显示数据在一个连续的时间间隔上的变化，从而反映事物随时间或有序类别而变化的趋势。
    折线图可以清晰反映出数据的特征，比如是否递增，递增或递减的速率如何等。
    一般水平轴（X轴）用来表示时间的推移，并且间隔相同；而垂直轴（Y轴）代表不同时刻的数据的大小。
    Pyplot模块提供了plot() 函数绘制折线图，它会根据给定的x坐标值数组，以及对应的y坐标值数组绘制折线图，其格式如下所示：

    matplotlib.pyplot.plot(x, y, color, linewidth, linestyle,…)

  其中，x和y表示折线图的数据源；color表示折线颜色；linewidths表示线宽；linestyle表示线型。
'''
# 例4-4-4 绘制程序绘制产品销量的折线图。
import matplotlib.pyplot as plt

#准备数据
x_data = ['2011','2012','2013','2014','2015','2016','2017']
y_data = [58000,60200,63000,71000,84000,90500,107000]

plt.plot(x_data,y_data,color='blue',linewidth=2.0,linestyle='--' )#绘制折线图
plt.rcParams['font.sans-serif']=['SimHei']#显示中文
plt.title('产品销量图')#设置标题
plt.xlabel('年份')
plt.ylabel('销量')
plt.grid()
plt.show()

'''
4. 条形图
  条形图是一种以长方形的长度为变量的统计图表，用来进行各类别数据大小的比较。
    条形图能够使人们非常方便的看出各个数据的大小，并且容易于比较数据之间的差别。
    Pyplot模块提供了bar()函数绘制条形图，其常用格式如下所示：

    matplotlib.pyplot.bar(x, height, width, color, tick_label,...)

  其中，x表示x轴数据；height表示y轴对应条形的高度；width表示x轴对应条形的宽度；color表示条形图的颜色；tick_label表示条形图的标签。
'''
# 例4-4-5 绘制一周内图书馆到馆人数的条形图。
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif']=['SimHei'] #避免中文出现乱码
plt.rcParams['axes.unicode_minus']=False

N = 7
x = np.arange(N)
data = np.random.randint(low=20, high=500, size=N)#产生随机数
labels = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期天']
plt.title("图书馆一周内到馆情况")
plt.xlabel('星期')
plt.ylabel('到馆人数')
plt.bar(x,data,width=0.8,color='b', tick_label=labels)
plt.show()

'''
5. 箱型图
  箱型图是一种用作显示一组数据分散情况资料的统计图，因形状如箱子而得名，如图4-4-7所示。
    在将一组数据从大到小排列后，分别计算其上边缘、上四分位数、中位数、下四分位数、下边缘和异常值。

中位数，表示一组数据按顺序排列从小至大第50%位置的数值；
上四分位数，表示一组数据按顺序排列从小至大第25%位置的数值；
下四分位数，表示一组数据按顺序排列从小至大第75%位置的数值；
上边缘，等于上四分位数+IQR*1.5，表示非异常范围内的最大值，其中IQR=上四分位数-下四分位数；
下边缘，等于下四分位数-IQR*1.5，表示非异常范围内的最小值。
Pyplot模块提供了boxplot ()函数绘箱型图，其格式如下所示：
    matplotlib.pyplot.boxplot(x, labels, sym, whis, widths,...)

  其中，x表示指定要绘制箱型图的数据；
        labels表示数据标签；
        sym表示指定异常点的形状，默认为+号显示；
        whis为指定上下须与上下四分位的距离，默认为1.5倍的四分位差；
        widths为指定箱线图的宽度，默认为0.5。
'''
# 例4-4-6 绘制12位本科毕业生和12位研究生毕业生月薪的箱型图。
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #避免中文出现乱码
plt.rcParams['axes.unicode_minus']=False

data = [[3710, 3756, 3850, 3880, 3880, 3890, 3920, 3940, 3950, 4050, 4060, 4325],
        [4110, 4157, 4252, 4281, 4285, 4291, 4323, 4345, 4350, 4550, 4560, 4725]]
labels = ['本科生','研究生']
plt.boxplot(data, labels=labels, sym='*')
plt.title("本科生研究生月薪")
plt.ylabel('薪水')
plt.show()

'''
本科生的箱线图中
上边缘值为4129，
下边缘值为3719，
中位数约为3905，
上四分位数约为3975，
下四分位数约为3905，
且有两个异常值3710，4350；

研究生的箱线图中
上边缘值为4589，
下边缘值为4084，
中位数为4307，
上四分位数约为4274，
下四分位数约为4400，
且仅有一个异常值4725。

图中，中位线偏向下四分位数。
'''
'''
6. 饼图
  饼图是划分为几个扇形的圆形统计图表，用于描述量、频率或百分比之间的相对关系。
    在饼图中，每个扇区的弧长（以及圆心角和面积）大小为其所表示的数量的比例。

  Pyplot模块提供了pie()函数绘制饼图，其格式如下所示：

    matplotlib.pyplot.pie(x, labels, autopct,...)

  其中，x表示指定要绘制饼图的数据；labels表示数据标签；autopct表示数据格式。
'''
# 绘制水果店一周内日收入的饼图。
import matplotlib.pyplot as plt
import numpy as np
labels = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
data = np.random.randint(800,2000,7)
plt.pie(data, labels=labels, autopct='%1.1f%%')
plt.axis('equal')
plt.legend()
plt.show()

'''
7. 词云图
  “词云”又称标签云或者文字云，是一种对关键词的视觉化描述方法，
    通过形成“关键词云层”或“关键词渲染”，对文本中出现频率较高的“关键词”进行视觉上的突出。
    词云图过滤掉大量的文本信息，使浏览者只要一眼扫过文本就可以领略文本的主旨。
    在开始绘制词云图之前，需要安装jieba和wordcloud，以管理员身份运行Anaconda Prompt，输入如下命令进行安装：

pip install jieba
pip install wordcloud
'''

# 例4-4-8 从《三国演义》的文本文件中读取数据，生成并绘制词云图。
import matplotlib.pyplot as plt
import jieba
from wordcloud import WordCloud

# （1）读入文本数据
# 打开txt文本文件
fr = open(r'F:\\Python\\ECUNworks\\人工智能B\\第五讲matplotlib\\三国演义.txt', "r",encoding='UTF-8')
# 读取文本文件数据
text = fr.read()

# （2）中文分词
# 使用默认精确模式，进行结巴中文分词，生成字符串
cut_text = jieba.cut(text)
# 给出符号分隔开分词结果，生成字符串
result = " ".join(cut_text)

# （3）生成词云图
# 记录字体所在的路径位置
font = r'C:\Windows\Fonts\simfang.ttf'
wc = WordCloud(# 设置字体路径
               font_path=font,
               # 设置背景色
               background_color='Yellow',
               # 设置背景宽
               width=1400,
               # 设置背景高
               height=1400)
# 产生词云图
wc.generate(result)

# （4）显示词云图
# 设置图像的标题
plt.figure("词云图")
# 设置以图片形式来显示词云图
plt.imshow(wc)
# 关闭图像坐标系
plt.axis("off")
# 显示词云图
plt.show()
# 关闭txt文本文件
fr.close()