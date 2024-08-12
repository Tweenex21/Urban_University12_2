import threading
import random
import time

class Bank:
    def __init__(self):
        self.balance = 0  # Начальный баланс
        self.lock = threading.Lock()  # Создаем объект Lock

    def deposit(self):
        for i in range(100):
            rand_dep = random.randint(50, 500)
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            elif self.balance < 500 and self.lock.locked():
                self.balance += rand_dep
                print(f'Пополнение: {rand_dep}. Баланс: {self.balance} ')
                self.lock.release()
            time.sleep(0.003)


    def take(self):
        for i in range(100):
            rand_take = random.randint(50, 500)
            print(f'Запрос на {rand_take} ')
            if rand_take <= self.balance:
                self.balance -= rand_take
                print(f'Снятие: {rand_take}. Баланс: {self.balance}')
            else:
                print(f'Запрос отклонен, недостаточно средств')
                self.lock.acquire()
            time.sleep(0.002)




# Создаем объект класса Bank
bank = Bank()

# Создаем потоки для методов deposit и take
deposit_thread = threading.Thread(target=bank.deposit)
take_thread = threading.Thread(target=bank.take)

# Запускаем потоки
deposit_thread.start()
take_thread.start()

# Ожидаем завершения потоков
deposit_thread.join()
take_thread.join()

# Выводим итоговый баланс
print(f"Итоговый баланс: {bank.balance}")