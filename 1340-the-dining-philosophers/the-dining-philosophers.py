from threading import Lock
class DiningPhilosophers:
    def __init__(self):
        self.forks=[Lock() for _ in range(5)]
        self.lock=Lock()
    def wantsToEat(self,
                   philosopher: int,
                   pickLeftFork: 'Callable[[], None]',
                   pickRightFork: 'Callable[[], None]',
                   eat: 'Callable[[], None]',
                   putLeftFork: 'Callable[[], None]',
                   putRightFork: 'Callable[[], None]') -> None:
        left=philosopher
        right=(philosopher+1)%5
        with self.lock:
            self.forks[left].acquire()
            self.forks[right].acquire()
            pickLeftFork()
            pickRightFork()
            eat()
            putLeftFork()
            putRightFork()
            self.forks[left].release()
            self.forks[right].release()