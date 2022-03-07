

lst = [1, 2, 3, 4, 5, 6]
book = {
    'title': 'The Langoliers',
    'author': 'Stephen King',
    'year_published': 1990
}
string = "Hello, World!"

for i in book:
    print(i)

iterator = iter(book)
print(next(iterator))
print(next(iterator))
print(next(iterator))
# print(next(iterator))

# КОгда мы выполняет цикл for in book /см. выше/, происходит что-то похожее:
it = iter(book)
while True:
    try:
        i = next(it)
        print(i)
    except StopIteration:
        break




