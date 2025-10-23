import tabulate

data = [
    ['id', 'name', 'number'],
    [0, 'jeff', 1234]
]
result = tabulate.tabulate(data)
print(result)