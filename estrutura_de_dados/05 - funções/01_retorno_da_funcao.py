def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1
    
    return antecessor, sucessor

print(calcular_total([10, 20, 34])) # soma dos numeros
print(retorna_antecessor_e_sucessor(10)) # retorna uma tupla

def func3():
    print("Olá mundo!")
    return None
print(func3())