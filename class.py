# why we need the __build_class__
# we make class that is setting tool for repeated variables and method(function)

import operator

class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

cal1 = Calculator()
cal2 = Calculator()

print(call.add(3))
print(call.add(4))
print(call.add(5))
print(call.add(6))
