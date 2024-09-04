from mypackage import module1,module2
print(module1.func1())
print(module2.func2())

print("Using Second Method: ")
import mypackage
print(module1.func1())
print(module2.func2())

print("Using Third Method: ")
from mypackage.module1 import func1
from mypackage.module2 import func2
print(func1())
print(func2())