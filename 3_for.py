"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по количеству проданных телефонов
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
def count_average(items_sold):
    scores_sum = 0
    for score in items_sold:
        scores_sum += score
    scores_avg = scores_sum / len(items_sold)
    return scores_avg

def total_score(items_sold):
    scores_sum = 0
    for score in items_sold:
        scores_sum += score
    return scores_sum

def main(data_phones_sold):
    total_scores_sum = 0
    quantity_phones = len(data_phones_sold)
    for product in data_phones_sold:
        product_total_score = total_score(product['items_sold'])
        print(f'Суммарное количество продаж для каждого телефона {product["product"]}: {product_total_score}')
        total_scores_sum += product_total_score
        product_score_avg = count_average(product['items_sold'])
        print(f"Среднее количество продаж для каждого телефона {product['product']}: {product_score_avg}")
    total_scores_avg = total_scores_sum / quantity_phones
    print(f'Суммарное количество продаж для всех {quantity_phones} телефонов: {total_scores_sum}')
    print(f'Среднее количество продаж для всех {quantity_phones} телефонов: {total_scores_avg}')



if __name__ == "__main__":
    main([
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ])
