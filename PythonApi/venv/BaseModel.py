class BaseModel:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    name="张三"
    age="12"

    def sayHi(self):
        print(self.name+"你好呀")

    def sayAge(self):
        print(self.name +"说 你好呀，我今年"+ str(self.age))
