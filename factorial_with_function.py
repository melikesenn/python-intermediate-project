def factorial(number):
    if not isinstance(number,int):
        raise TypeError("numara sayi değil")

    if not number >= 0:
        raise ValueError("sayi 0 dan küçük olmamalı")

    def inner_factorial(number):
        if number <=  1:
            return 1
        return number * inner_factorial(number-1)

    return number * inner_factorial(number)
print(factorial(4))