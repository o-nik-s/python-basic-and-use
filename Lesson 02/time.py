# Как узнать в python время выполнения скрипта

'''Очень часто возникает необходимость оценки эффективности того или иного куска кода в python. 
Поиски по интернету натолкнули на весьма интересный и простой способ.
Создаём класс и переопределяем два метода:'''

import time

class Profiler(object):
    def __enter__(self):
        self._startTime = time.time()

    def __exit__(self, type, value, traceback):
        print("Elapsed time: {:.3f} sec".format(time.time() - self._startTime))

'''Используется код следующим образом:'''
with Profiler() as p:
    # здесь пишем код, который необходимо проверить
'''При входе в инструкцию with вызывается метод __enter__(), а при завершении (даже если возникло исключение) - __exit__().'''

# Отсюда: https://cucumbler.ru/blog/articles/kak-uznat-v-python-vremja-vypolnenija-skripta.html


'''Вы можете сами оценить время работы скрипта, используя простую конструкцию:
start_time = time.time()  # вычисляем время на начало вычислений
# код, время выполнения которого Вы оцениваете
elapsed_time = time.time() - start_time  # считаем сколько времени прошло с начала вычислений'''