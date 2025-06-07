"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def hello_user(ask = input('Введите что-то \n')):
    try:
        while True:
            print(ask)

    except KeyboardInterrupt:
        print('Пока')
       
if __name__ == "__main__":
    hello_user()
  