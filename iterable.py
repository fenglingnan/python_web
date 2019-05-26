class Foo(object):
    def __init__(self,n):
        self.n=n
    def __iter__(self):
        return self
    def __next__(self):
        if self.n==13:
            raise StopIteration('迭代终止了')
        self.n+=1
        return self.n

f1=Foo(7)
#next不保存变量
# print(next(f1))
# print(next(f1))
# print(next(f1))
# print(next(f1))
# print(next(f1))
# print(next(f1))
# print(next(f1))

for i in f1:
    print(i)

class Fib:
    m=3
    def __init__(self):
        self.n = 2
        self._a=1
        self._b=1

    def __iter__(self):
        return self

    def __next__(self):
        if self._a>100:
            raise StopIteration('迭代终止')
        self._a,self._b=self._b,self._a+self._b
        return self._a

f1=Fib()
print(f1.m)
print(f1.__dict__,Fib.__dict__)
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))

for i in f1:
    print(i)