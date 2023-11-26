import get_data as gd

while True:
    judge = input("是否进行歌词文件转为csv操作,1 继续，0 停止")
    if judge == str(1):
        genre = input("请输入曲风")
        gd.get_lyric_csv(genre=genre)
    elif judge == str(0):
        break
    else:
        print("输入的judge不对，再输入一次")
        continue
while True:
    judge = input("是否进行歌词整理和整合到data中的操作，1 继续，0 停止")
    if judge == str(1):
        gd.word_purify()
        gd.word_freq()
    elif judge == str(0):
        break
    else:
        print("输入的judge不对。请再输入一次")
        continue
