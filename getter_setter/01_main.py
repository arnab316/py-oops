class MyClass:
    def __init__(self, value):
        self.value = value
    def show(self):
      print(f"value is {self._value}")
    @property
    def ten_value(self):
        return self._value * 10
    @ten_value.setter
    def ten_value(self, value):
        self._value = value / 10


obj = MyClass(100)
obj.ten_value = 67
print(obj.ten_value)
obj.show()
