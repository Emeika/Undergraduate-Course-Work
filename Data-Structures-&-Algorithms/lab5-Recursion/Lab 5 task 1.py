# task 1

def duplicate(lista,num):
    if lista == []:
        return False

    elif lista[0] == num:
        return True
    else:
        return duplicate(lista[1:],num)

lista = [5,3,5,3,2,6,7,8]
num = 10
print(duplicate(lista,num))

#
#o(n)

