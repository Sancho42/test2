# Тренировка использования пакета threading

import random
import time
import threading


class SolveFactorial:
    def __init__(self):
        self.answer = 0

    def handler_solve_fact_async(self, fact: int):
        answer = str(fact) + '! = ' + str(self.solve_fact(fact))
        print(answer, end='\n')

    def solve_fact(self, fact: int):
        factorial: int = fact
        if factorial > 0:
            if factorial > 1:
                factorial * self.solve_fact(factorial - 1)  # Это нужно для замедления работы потока
                return factorial * self.solve_fact(factorial - 1)
            else:
                return 1
        else:
            return 0

    def solve_fact_async(self, fact: int):
        factorial = fact
        x = threading.Thread(target=self.handler_solve_fact_async, args=(factorial,))
        x.start()
        return 0


def main():
    solver = SolveFactorial()
    for i in range(10):
        number = input('\nКакой факториал нужен?')
        try:
            solver.solve_fact_async(int(number))
        except Exception:
            print('error!')
            return 1
    return 0


if __name__ == '__main__':
    main()