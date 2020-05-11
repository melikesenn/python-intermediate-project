def us(number):

    def inner(power):

        return number ** power

    return inner

iki = us(2)
print(iki(3))