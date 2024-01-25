salario = 2000

def salario_bonus(bonus, lista):
    global salario
    
    lista_aux = lista.copy()
    lista_aux.append(2)
    print(f"lista auxiliar= {lista_aux}")
    
    salario += bonus
    return salario

lista = [1]

novo = salario_bonus(500, lista)  # 2500
print(novo)
print(lista)
