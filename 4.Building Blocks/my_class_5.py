class MyClass(object):
    age = 21
    def __init__(self, num1, num2):
        print(self)
        self.num1 = num1
        self.num2 = num2


x = MyClass(9, 81)
print(x.num1, x.num2, x.age)
