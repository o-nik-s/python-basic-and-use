GREETING = "Hello, "  # Используем специальную константу
GREETING_new = "Hello, "

class BadName(Exception):
    pass


def greet(name):
    if name[0].isupper():
        return GREETING + name
    else:
        raise BadName(name + " is inappropriate name")


print("Import is execution")

__all__ = ["BadName", "greet", GREETING_new]  # Указали те имена, которые будут импортироваться с помощью * /не хотим импортировать GREETING/