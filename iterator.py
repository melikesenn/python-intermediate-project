"""
#iteratör sıra sıra dolaşmayı sağlar
liste = [1,2,3]
iterator = iter(liste)
next(iterator) #sırayla bastırmayı sağlar for döngüsü gibi

"""

class MyNumbers:
    def __init__(self,start,stop):
        self.stop = stop
        self.start = start

    def __iter__(self):
        return self #objeyi direk döndürür

    def __next__(self):
        if self.start <= self.stop:
            x = self.start
            self.start += 1
            return x
        else:
            raise StopIteration

liste = MyNumbers(10,20)

for i in liste:
    print(i)

