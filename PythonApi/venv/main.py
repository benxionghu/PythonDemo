import sys;
import  BaseModel

def printHello():
    print("hello")

if "__name__=__main__":
    printHello()
    a = BaseModel("张三",23);
    a.sayHi();
