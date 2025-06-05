"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
sales = [ {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
{'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
{'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]} ]

def count_average(phone_sales):
    phone_sum = 0
    for score in phone_sales:
        phone_sum += score
    phone_avg = phone_sum / len(phone_sales)
    return phone_avg

all_model_avg = 0
all_model_sales = 0
for one_model in sales:
    model_avg = count_average(one_model['items_sold'])
    model = sum(one_model['items_sold'])
    all_model_avg += model_avg
    all_model_sales += model
    print(f"Количество проданных {one_model['product']}: {int(model)}")
    print(f"Средняя продажа {one_model['product']}: {int(model_avg)}")
all_sales_avr = all_model_avg / len(sales)
print(f'Количество всех проданных моделей {int(all_model_sales)}')
print(f'Средняя количество всех проданных моделей {int(all_sales_avr)}')

if __name__ == "__main__":
    main()
