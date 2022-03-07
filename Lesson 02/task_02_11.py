# Лямбда функции предоставляют нам удобный способ создать функцию «прямо на месте».
# Но иногда, когда нужно создавать много однотипных лямбда функций, еще удобнее будет
# создать функцию, которая будет их генерировать.

# Реализуйте функцию mod_checker(x, mod=0), которая будет генерировать лямбда функцию от одного аргумента y,
# которая будет возвращать True, если остаток от деления y на x равен mod, и False иначе.

# Пример использования:
# mod_3 = mod_checker(3)
# print(mod_3(3)) # True
# print(mod_3(4)) # False
# mod_3_1 = mod_checker(3, 1)
# print(mod_3_1(4)) # True

def mod_checker(x, mod=0):
     mod_x = lambda y: y % x == mod
     return mod_x


mod_3 = mod_checker(3)
print(mod_3(3)) # True
print(mod_3(4)) # False
mod_3_1 = mod_checker(3, 1)
print(mod_3_1(4)) # True


'''Функция mod_checker возвращает саму  lambda функцию и определяет в ней значения X и MOD.Теперь про mod_3
mod_3 = mod_checker(3)
в данном случаем мы mod_3 присваиваем lambda,т.к. mod_cheker вернул нам ее, где X=3 и по умолчанию  base = 0.
Таким образом mod_3 становится функцией. 
mod_3(3)
Мы вызываем саму lamda и передаем только значение Y, т.к. lamda у нас запрашивает только одно значение.'''

'''
def main_f(x):
    def inc_f(y):
        return y + x

    return inc_f

foo = main_f(10)
print(foo(11))

foo = main_f(5)
print(foo(7))
'''