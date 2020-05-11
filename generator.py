#generator bellekte yer işgal etmeyen iterator üretir. elemana ulaşma isteğimiz yoksa yield kullanırız.

def cube():
    for i in range(5):
        yield i**2 #bellekte bir yerde saklanmıyor üretildiği an kullanılacak
'''
print(cube())

generator = cube()
iterator = iter(generator)
print(next(iterator))
print(next(iterator))
print(next(iterator))
'''
iterator = cube()

for i in iterator:
    print(i)