
from threading import Semaphore

class FizzBuzz:
    def __init__(self, n: int):
        self.n = n

        self.number_sem = Semaphore(1)
        self.fizz_sem = Semaphore(0)
        self.buzz_sem = Semaphore(0)
        self.fizzbuzz_sem = Semaphore(0)

    def fizz(self, printFizz):
        for i in range(1, self.n + 1):
            if i % 3 == 0 and i % 5 != 0:
                self.fizz_sem.acquire()
                printFizz()
                self.number_sem.release()

    def buzz(self, printBuzz):
        for i in range(1, self.n + 1):
            if i % 5 == 0 and i % 3 != 0:
                self.buzz_sem.acquire()
                printBuzz()
                self.number_sem.release()

    def fizzbuzz(self, printFizzBuzz):
        for i in range(1, self.n + 1):
            if i % 15 == 0:
                self.fizzbuzz_sem.acquire()
                printFizzBuzz()
                self.number_sem.release()

    def number(self, printNumber):
        for i in range(1, self.n + 1):
            self.number_sem.acquire()

            if i % 15 == 0:
                self.fizzbuzz_sem.release()
            elif i % 3 == 0:
                self.fizz_sem.release()
            elif i % 5 == 0:
                self.buzz_sem.release()
            else:
                printNumber(i)
                self.number_sem.release()
