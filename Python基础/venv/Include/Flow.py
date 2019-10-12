

age=input("你的年龄为：")  #输入框
age=int(age)  # 类型转换
if(age<=18):
   print("你还是个小孩子")
elif(age<=40):
   print("你已经成年了")
elif(age<=60):
   print("你已经成为爷爷辈分的人啦")
else:
   print("你的年龄有点强大")


num=0
while num<=7:
  print(num)
  if(num==3):
   break  # 满足当前条件则终止当前的循环
  num+=1
else:  # 当循环执行完成之后会执行else中的语句  当循环被终止的时候不会执行else中的语句
   print("end")

lngrid=["甜橙橙呀", "嘻嘻嘻", "哈哈哈", "哒哒哒", "滴滴滴"]
for item in lngrid:
    if ("甜" in item):
      print("喜欢的呀")
      continue
    print(item)

for i in range(1,10):
    for l in range(1,i+1):
       print(i, "*", l,"=", i*l , end="\t"  )
    print()






