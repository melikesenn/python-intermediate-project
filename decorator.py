'''

def mydecorator(func):
    def wrapper():
        print("fonksiyon öncesi")
        func()
        print("fonksiyon sonrası")
    return  wrapper()

def sayhello():
    print("hello")

def saygreeting():
    print("greeting")


sayhello = mydecorator(sayhello)
 aşağıda dekoreator kullanılan hali bulunmaktadır
'''


def mydecorator(func):
    def wrapper():
        print("fonksiyon öncesi")
        func()
        print("fonksiyon sonrası")
    return  wrapper()

@mydecorator
def say():
    print("hello")

print(say)

