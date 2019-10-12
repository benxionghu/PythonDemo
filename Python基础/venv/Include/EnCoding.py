import  sys


a = 'Hello,中国'  # 字节串，长度为字节个数 = len('Hello,')+len('中国') = 6+2*2 = 10
b = u'Hello,中国'  # 字符串，长度为字符个数 = len('Hello,')+len('中国') = 6+2 = 8

print(type(a), len(a))
print(type(b), len(b))

encoding=sys.getdefaultencoding()
print(encoding)  #python 3 默认编码
