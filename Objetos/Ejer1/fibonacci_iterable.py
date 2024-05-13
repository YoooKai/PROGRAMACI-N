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
"""mejor es:"""
    def __init__(self, n):
        self.n = n
        self.a= 0
        self.b = 1
        self.pointer = 0
        
def fibonacci_calc(self):
    result = self.a
    self.a, self.b = self.b, self.a + self.b
    return result 
    
def __next__(self):
    if self.pointer >= self.target:
        raise STopIteration
    f = self.fibonacci_calc()
    return f

def run(n):
    return list(Fibonacci(n))
""" se puede pasar a lista un iterable
es ineficiente hacer una lista con fibo"""
