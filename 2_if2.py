"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""


def main(first_str, second_str):
  if isinstance(first_str, str) and isinstance(second_str, str):
    if first_str == second_str:
      return 1
    elif len(first_str) > len(second_str) and second_str != "learn":
      return 2
    elif first_str != second_str and len(first_str) == len(second_str):
      return f"Error. Strings {first_str} and {second_str} not identical"
    else:
      return 3
  else:
    return 0
  

if __name__ == "__main__":
  print(main(1, "съешь ещё этих мягких французских булок"))
  print(main("съешь ещё этих мягких французских булок", "съешь ещё этих мягких французских булок"))
  print(main("съешь ещё этих мягких французских булок", "да выпей чаю"))
  print(main("Python", "learn"))
  print(main("мама", "мыла")) # Expectation result = "Error. Strings not identical" ?? не пойму каким способом можно сделать это красиво и не усложняя код
  