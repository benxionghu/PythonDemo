print("int ==> 整数. 主要⽤来进⾏数学运算")
print("str ==> 字符串, 可以保存少量数据并进⾏相应的操作")
print("bool==>判断真假, True, False")
print("list==> 存储⼤量数据.⽤[ ]表⽰")
print("tuple=> 元组, 不可以发⽣改变 ⽤( )表⽰")
print("dict==> 字典, 保存键值对, ⼀样可以保存⼤量数据")
print("set==> 集合, 保存⼤量数据. 不可以重复. 其实就是不保存value的dict")

s = "甜橙橙呀"

# 索引
print(s[0])
print(s[1])

# 切片
print(s[0:3])
print(s[:])
print(s[3:])


# 字符串大小写
s = 'where aRe you from'
# 首字母大写，其它都转换成小写
s1 = s.capitalize()
print(s1)

# 全部小写
s2 = s.lower()
print(s2)
# 全部大写
s3 = s.upper()
print(s3)
# 大变小，小变大
s4 = s.swapcase()
print(s4)
# 被特殊字符隔开的首字母大写（中文也算特殊字符）
str = "we have,a你好dream"
print(str.title())

# 字符居中
s = "甜橙橙"
print(s.center(20, '*'))  # *********女神*********

#去除空格
s = "  I have a dream     "
# 去掉两边的空格
s1 = s.strip()
print(s1)
# 去掉左边的空格
s2 = s.lstrip()
print(s2)
# 去掉右边的空格
s3 = s.rstrip()
print(s3)
# 指定内容将其去掉
s = "abcdefgabc"
print(s.strip('abc'))

#3.替换replace
s = "welcome to our singer"
ret = s.replace("to", "three")
print(ret)
ret1 = s.replace("o", "SB",1)  # 1表示替换几个字符
print(ret1)

#4.切割split
s = "we,are,too,many,dream"
s1 = s.split(",")
print(s1)  # ['we', 'are', 'too', 'many', 'dream']

# 如果切割的对象在字符串的两边，会多出空字符串
ss = "女神is女神my女神dream女神"
ss1 = ss.split("女神")
print(ss1)  # ['', 'is', 'my', 'dream', '']

#5.格式化输入
s = "我是%s,芳龄%d岁,我喜欢穿%s" % ("女神", 18, "滴滴滴")
print(s)
s1 = "我是{},芳龄{}岁,我喜欢穿{}".format("女神", 18, "滴滴滴")
print(s1)
s2 = "我是{0},芳龄{2}岁,我喜欢穿{1}".format("女神", "滴滴滴", 18)
print(s2)
s3 = "我是{name},芳龄{age}岁,我喜欢穿{dress}".format(name="女神", age=19, dress="滴滴滴")
print(s3)

#6.查找
s = "I have a dream"

# 以...开头
print(s.startswith("I"))  # True
# 以...结尾
print(s.endswith("am"))  # True
# 计数
print(s.count("a"))  # 3
# 查找索引位置,找不到返回-1
print(s.find("e"))  # 5
# 查找索引位置，找不到报错
print(s.index("m"))  # 13

if(s.find("b")>-1): #判断字符串是否存在
    print(s.index("b"))

# 7.isdigit()：是否由数字组成
s = "888"
if s.isdigit():
    print("整数")  # 整数

#  8.join（）：将序列转换成字符串
li = ["美女", "女神", "校花"]
s = "_".join(li)
print(s)  # 美女_女神_校花

s = "屌丝逆袭"
s1 = "_".join(s)
print(s1)  # 屌_丝_逆_袭




