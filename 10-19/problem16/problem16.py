"""
PROBLEM 16 [EASY]

This problem was asked by Twitter.

You run an e-commerce website and want to record the last N order ids in a log. Implement a data structure to accomplish this, with the following API:

record(order_id): adds the order_id to the log
get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.
You should be as efficient with time and space as possible.
"""

class Log:
    def __init__(self, n: int) -> None:
        self.n = n
        self.log_list = list()
        self.curr_pos = 0
    
    def record(self, order_id: int) -> None:
        if len(self.log_list) >= self.n:
            self.log_list[self.curr_pos] = order_id
        else:
            self.log_list.append(order_id)
        self.curr_pos = (self.curr_pos + 1) % self.n

    
    def get_last(self, i: int) -> int:
        return self.log_list[self.curr_pos - i]


if __name__ == "__main__":
    records: list[int] = [1, 5, 10, 15, 20]
    log: Log = Log(3)
    for r in records:
        log.record(r)
    
    assert log.get_last(3) == 10
    assert log.get_last(2) == 15
    assert log.get_last(1) == 20

    print("Successfully tested.")
