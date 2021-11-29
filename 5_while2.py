"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например:
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user() которая с помощью функции input()
  просит пользователя ввести вопрос, а затем, если вопрос есть
  в словаре, программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую
    
"""

from random import choice  


questions_and_answers = {
                      "как дела?": ["Хорошо!", "Нормально!", "Отлично!", "Пойдет!"],
                        "что делаешь?": ["Программирую", "Отдыхаю", "Гуляю", "Пью кофе"]
                        }

def ask_user(answers_dict):
  
  question = input("Задай вопрос: ").lower().strip()
  while True:
    if question in answers_dict:
      print(choice(answers_dict.get(question)))
      break
    else:
      question = input("Спроси еще чего: ")
    
if __name__ == "__main__":
    ask_user(questions_and_answers)
