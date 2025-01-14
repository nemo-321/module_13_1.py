#  импортируем библиотеку `asyncio`, которая предоставляет инструменты для работы с асинхронным программированием.
import asyncio

#  асинхронная функция `start_strongman` которая принимает имя силача и его силу (мощность).
#  Ключевое слово `async` указывает, что функция будет работать асинхронно.
async def start_strongman(name, power):

    # Когда функция вызывается, она выводит сообщение о начале соревнования для конкретного силача.
    print(f'Силач {name} начал соревнования.')

    # Здесь происходит цикл, который выполняется 5 раз (от 1 до 5).
    # `await asyncio.sleep(1 / power)` — это асинхронная операция, которая "приостанавливает" выполнение функции
    # на определенное время. Время ожидания зависит от параметра `power`. Чем больше `power`, тем меньше время ожидания,
    # что позволяет другим задачам выполняться в это время.
    for i in range(1, 6):
        await asyncio.sleep(1 / power)

        # Затем выводится сообщение о том, что силач поднял определенное количество шаров.
        print(f'Силач {name} поднял {i} шар')

        # Когда цикл завершен, выводится сообщение о том, что силач закончил соревнования.
    print(f'Силач {name} закончил соревнования.')

# Определение функции `start_tournament`,асинхронная функция, которая запускает соревнования для всех силачей.
async def start_tournament():

   # Создание задач: создаем список `tasks`, в который добавляем вызовы функции `start_strongman`
   # для каждого силача с их соответствующими значениями мощности.
   task1=asyncio.create_task( start_strongman("Pasha",3))
   task2=asyncio.create_task(start_strongman("Denis",4))
   task3 = asyncio.create_task(start_strongman("Apoiion", 5))

   #  запуск всех задач параллельно.
   #  Это означает, что каждый силач будет поднимать шары одновременно, но с учетом своих мощностей.
   await task1
   await task2
   await task3

# Запуск асинхронной функции start_tournament
asyncio.run(start_tournament())
