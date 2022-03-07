'''Использовал слайсинг и удаление - code complexity заметно ниже ( У меня 5)'''

class ExtendedStack(list):
    def sum(self):
        self.append(sum(self[-2:]))
        del self[-3:-1]

    def sub(self):
        # операция вычитания
        self.append(self[-1]-self[-2])
        del self[-3:-1]

    def mul(self):
        # операция умножения
        self.append(self[-2]*self[-1])
        del self[-3:-1]

    def div(self):
        self.append(self[-1]//self[-2])
        del self[-3:-1]
