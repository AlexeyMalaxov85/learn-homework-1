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

  sales = [
          {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
          {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
          {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
          ]
  def product_sales_sum(sum):
    sum_sales = 0
    for i in sum:
      sum_sales += i
    return sum_sales

  for all_sales in sales:
    print(f"Всего продано: {all_sales['product']} - {product_sales_sum(all_sales['items_sold'])}\n")
    
  for avg_sales in sales:
    print(f"В среднем продажи: {avg_sales['product']} - {round(product_sales_sum(avg_sales['items_sold']) / len(avg_sales['items_sold']))}\n")

  all_in_sum = 0
  for i in sales:
    all_in_sum += product_sales_sum(i['items_sold'])
  print(f"Всего продаж: {all_in_sum}")

  all_in_avg = 0
  for i in sales:
    all_in_avg += len(i['items_sold'])
  print(f"Среднние продажи всех товаров: {all_in_sum / all_in_avg}")


    
if __name__ == "__main__":
    main()
