class LoggableList(list, Loggable):
    def append(self, val):
        list.append(self, val)
        self.log(val)

# Сложность ниже в 1.5 раз
