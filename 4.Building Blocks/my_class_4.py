class MyClass:
    def setAge(self, num):
        self.age = num

    def getAge(self):
        return self.age


one = MyClass()
one.setAge(36)
print(one.getAge())

two = MyClass()
two.setAge("Thirty-Six")
print(two.getAge())
two.setAge(36)
print(two.getAge())
