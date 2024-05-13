# ******************
# FIBONACCI ITERABLE
# ******************

class Fibonacci:
    def __init__(self, n):
        self.n = n
        self.fibo = [0, 1]
        self.index = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index < self.n:
            if self.index >= len(self.fibo):
                self.fibo.append(self.fibo[-1] + self.fibo[-2])
            result = self.fib_sequence[self.index]
            self.index += 1
            return result
        else:
             raise StopIteration

def run(n):
    return list(Fibonacci(n))
""" se puede pasar a lista un iterable"""
