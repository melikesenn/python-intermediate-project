def toplama(a,b):
    return a+b
def cikarma(a,b):
    return a-b

def islem(x,y,islem_adi):
    if islem_adi == "toplama":
        print(x(5,1))
    elif islem_adi == "cikarma":
        print(y(5,2))

    else:
        print("geçersiz")

islem(toplama,cikarma,"toplama")