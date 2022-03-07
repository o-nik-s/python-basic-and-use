import exceptions as exc
import fib

from exceptions import *

print(exc.greet("Student"))

# Однако мы всегда можем убедиться, что импортировали функцию fib
print(fib.fib(5))

print(BadName)
print(greet("Student"))
# print(GREETING) # Убрали в __all__, поэтому не можем импортировать
print(_GREETING_new)