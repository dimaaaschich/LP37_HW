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

questions_and_answers = {}

def ask_user(answers_dict):
    """
    Замените pass на ваш код
    """
my_dict = {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"}
    
    #def ask_user(input):
user = input('Задайте вопрос ')
#    print(user in my_dict)
def ask_user(my_dict):
    while user in my_dict:
        print(my_dict.get(user))
        break
ask_user(my_dict)

if __name__ == "__main__":
    ask_user(questions_and_answers)
