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
#first_string = input("")
#second_string = input("")


#def main(first_string, second_string):
#  if isinstance(first_string, str) and isinstance(second_string, str):
#    return True
#  else:
#    return False


#decision = main(first_string, second_string)

#if decision == True and len(first_string) == len(second_string):
#  print("1")
#elif decision == True and len(first_string) > len(second_string):
#  print("2")    
#elif second_string == "learn":
#  print("3")
#else:
#  print("0")

def main(first_str, second_str):
  if isinstance(first_str, str) and isinstance(second_str, str):
    if len(first_str) == len(second_str):
      return 1
    elif second_str == "learn":
      return 3
    else:
      return 2
  else:
    return 0




if __name__ == "__main__":
  print(main(1, "съешь ещё этих мягких французских булок"))
  print(main("съешь ещё этих мягких французских булок", "съешь ещё этих мягких французских булок"))
  print(main("съешь ещё этих мягких французских булок", "да выпей чаю"))
  print(main("Python", "learn"))    

