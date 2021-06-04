"""
PROBLEM #10 [MEDIUM]

This problem was asked by Apple.

Implement a job scheduler which takes in a function `f` and an integer `n`, and calls `f` after `n` milliseconds.
"""
import time, threading
from threading import Thread


class JobScheduler:
    """
    A very dummy JobScheduler.
    Can be improved to queue tasks, delay them, etc.
    By now it justs allows schedule one task at a time.
    """

    def __init__(self):
        self.result = None 
        self.timing = None
    # /def

    def run(self, f, n):
        self.result = None
        self.timing = None

        def sleep_and_call(n):
            time.sleep(n/1000)
            self.result = f
        # /def
        
        t: Thread = Thread(target=sleep_and_call, args=(n,))
        t0: int = time.time_ns() // 1E6  # ns to ms
        t.start()
        t.join()
        self.timing = time.time_ns() // 1E6 - t0
    # /def
    

if __name__ == "__main__":
    ms: float = 2000.0
    
    def add(x: int, y: int) -> int:
        return x + y

    def powpow(x: int, y: int) -> int:
        return x ** y
    
    def voiding(x: int) -> None:
        x += 0
    
    j: JobScheduler = JobScheduler()
    
    # since we can't isolate exact thread time, accept 1% std err
    j.run(add(2, 3), ms)
    assert j.result == add(2, 3)
    assert ms / j.timing > 0.99

    j.run(powpow(2, 3), ms)
    assert j.result == powpow(2, 3)
    assert ms / j.timing > 0.99
    
    j.run(voiding(3), ms)
    assert j.result == voiding(3)
    assert ms / j.timing > 0.99
    # doesn't make sense to compare it returns None, but just to showcase it doesn' brake
    
    print("Successfully tested.")
