n = int(input("Введите количество товаров, по которым будем собирать аналитику: "))
goods = []
for i in range(n):
    goods_name = input("Введите наименование товара: ")
    goods_price = int(input("Введите цену товара: "))
    goods_quantity = int(input("Введите количество товара: "))
    goods_measure = input("Введите единицу измерения товара: ")
    goods.append((i + 1, {'название': goods_name, 'цена': goods_price, 'количество': goods_quantity, 'eд': goods_measure}))
print(goods)
goods_dict = {
    'название': [],
    'цена': [],
    'количество': [],
    'eд': []
}
for _, dict_ in goods:
    for key in goods_dict:
        goods_dict.get(key).append(dict_.get(key))
for key in goods_dict:
    if len(set(goods_dict.get(key))) == 1:
        goods_dict[key] = list(set(goods_dict.get(key)))
print(goods_dict)
