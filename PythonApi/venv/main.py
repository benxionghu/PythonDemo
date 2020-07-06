import sys;
#import BaseModel
import PythonApi.venv.PythonHelper as pythonHelper
from PythonApi.venv.BaseModel import BaseModel

def printHello():
    print("hello")

if "__name__=__main__":
    printHello()
    a=BaseModel("李四",12)
    a.sayHi();
    print(pythonHelper.add(1,2))

