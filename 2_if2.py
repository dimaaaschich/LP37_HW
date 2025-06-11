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

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    def compare_str(first, second):
        if not (isinstance(first, str) and isinstance(second, str)):
            return 0
        elif first == second:
            return 1
        elif second == 'learn':
            return 3
        elif len(first) > len(second):
            return 2
    
    print(compare_str(1, 'string'))
    print(compare_str('one', 'one'))
    print(compare_str('longer', 'short'))
    print(compare_str('Python', 'learn'))
    
if __name__ == "__main__":
    main()
