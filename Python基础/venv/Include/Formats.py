
x = int(input("please enter first integer:"))
y = int(input("please enter second integer:"))

if (x == y):
    print("两数相同！")
elif(x > y):
    print("较大的数为：" ,x)
else:
    print("较大的数为：" ,y)

print("较大的数为：",x if( x >y) else y)

name = "甜橙橙"
age = 18
print("%s今年已经%d岁了，她是如此的美丽动人！" % (name, age))  # %s：字符串占位符 %d：数字占位符
print()
print("%s在班里一直名列前茅，成绩超过了他们班%%90的学生。" % name)  #这句话如果使用要使用占位符，那么就需要加两个%。因为一段话中一旦出现了%，那就是占位的意思，而想要输出占位符%，则使用%%。


# ==:比较的是值
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)


# is：比较的是id
a = b = [1, 2, 3]
c = [1, 2, 3]
print(id(a))
print(id(b))
print(id(c))
print(a is b )
print(a is c)

# 数字
a = 12
b = 12
print("数字",a is b)  # True
print(id(a))
print(id(b))

# 字符串
x = "abc"
y = "abc"
print(x is y)  # True
print(id(x))
print(id(y))

# 列表
x = [1, 2, 3]
y = [1, 2, 3]
print("列表",x is y)  # False
print(id(x))
print(id(y))

# 元组
x = (1, 2, 3,4,5)
y = (1, 2, 3,4,5)
print("元组",x is y)  # False
print(id(x))
print(id(y))

# 字典
a = {"name":"女神"}
b = {"name":"女神"}
print("字典",a is b)  # False
print(id(a))
print(id(b))

# 集合
a = {"女神", "屌丝"}
b = {"女神", "屌丝"}
print( "集合:" ,a is b)
print(id(a))
print(id(b))