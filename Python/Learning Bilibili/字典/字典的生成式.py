items = ['Fruits', 'Books', 'Others']
prices = [96, 78, 85]
d = {item: price for item, price in zip(items, prices)}
print(d)
d = {item.upper(): price for item, price in zip(items, prices)}
# .upper 就是指把里面的所有字母全都大写
print(d)
