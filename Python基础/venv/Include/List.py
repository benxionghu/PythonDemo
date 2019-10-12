
#列表的索引
list=["张三","李四","王五","赵琦"]
print(list[0])
print(list[3])
list[2] = "逆袭"
print(list)

#列表的切片
list = ["小明", "校花", "屌丝", "女神", "帅哥"]
print(list[0:3])  # ['小明', '校花', '屌丝']
print(list[-6:-2])  # ['小明', '校花', '屌丝']
print(list[:])  # ['小明', '校花', '屌丝', '女神', '帅哥']

# 4、列表的增删改查
list = ["小明", "校花", "屌丝", "女神", "帅哥"]
print(list)  # ['小明', '校花', '屌丝', '女神', '帅哥']
list.append("男神")
print(list)  # ['小明', '校花', '屌丝', '女神', '帅哥', '男神']

li = []
while True:
    names = input("请输入姓名，退出Q:")
    if names == 'Q':
        break
    li.append(names)
print(li)

list = ["小明", "校花", "女神", "帅哥"]
list.insert(2, "屌丝")
print(list)  # ['小明', '校花', '屌丝', '女神', '帅哥']

list = ["小明", "校花", "女神", "帅哥"]
li = ["小三", "小四"]
list.extend(li)
print(list)  # ['小明', '校花', '女神', '帅哥', '小三', '小四']