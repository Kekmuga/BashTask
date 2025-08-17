def total_revenue(purchases):
    sumus = 0
    for i in purchases:
        sumus += i["price"]*i["quantity"]
    return sumus

def items_by_category(purchases):
    categ = dict()
    for i in purchases:
        cata = i["category"]
        item = i["item"]
        if cata not in categ.keys(): #Смотрим на наличие ключа в словаре,
            categ[cata] = []        #если нет, то добавляем ключ и свежий список к нему
        if item not in categ[cata]:
            categ[cata].append(item)
    return categ

def expensive_purchases(purchases, min_price):
    list = []
    for i in purchases:
        if i['price'] >= min_price:
            list.append(i)
    return list

def average_price_by_category(purchases):
    categ = dict()
    for i in purchases:
        cata = i["category"]
        if cata not in categ.keys(): #Делаем всё тоже самое что и в items_by_category,
            categ[cata] = []         # но теперь назначаем ключам списки с ценами
        categ[cata].append(i['price'])

    for i in categ:
        avg = sum(categ[i])/len(categ[i]) #Находим среднее
        categ[i] = avg
    return categ

def most_frequent_category(purchases):
    categ = dict()
    for i in purchases:
        cata = i["category"]
        if cata not in categ.keys():
            categ[cata] = 0
        categ[cata] += i["quantity"]
    max = 0
    key = ''
    for i in categ:
        if categ[i] > max:
            max = categ[i]
            key = i
    return key, max

purchases = [
    {"item": "apple", "category": "fruit", "price": 1.2, "quantity": 10},
    {"item": "banana", "category": "fruit", "price": 0.5, "quantity": 5},
    {"item": "milk", "category": "dairy", "price": 1.5, "quantity": 2},
    {"item": "milk", "category": "dairy", "price": 1.5, "quantity": 100},
    {"item": "bread", "category": "bakery", "price": 2.0, "quantity": 3},
]
try:
    print("Введите минимальную цену товаров, чтобы скрипт нашёл список закупок с ценой позиций >= указанной")
    min = float(input())
    last_sent = most_frequent_category(purchases)
    print(f"Общая выручка: {total_revenue(purchases)}\n"
          f"Товары по категориям: {items_by_category(purchases)}\n"
          f"Покупки дороже {min}: {expensive_purchases(purchases, min)}\n"
          f"Средняя цена по категориям: {average_price_by_category(purchases)}\n"
          f"Категория с наибольшим количеством проданных товаров: {last_sent[0]}. По ней было купленно: {last_sent[1]} ед товара\n")
except Exception as e:
    print(f"Не удалось выполнить запрос.\n"
          f"Произошла ошибка: {e}")
