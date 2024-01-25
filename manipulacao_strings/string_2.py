nome = "Leonardo"
idade = 27
profissao = "Programador"
linguagem = "Python"
saldo = 45.435

#dictionary
dados = {"nome": "Leonardo", "idade": 27}

print("Nome: %s, Idade: %d" % (nome,idade)) 
print("Nome: {}, Idade: {}".format(nome,idade)) 
print("Nome: {0}, Idade: {1}".format(nome,idade)) 
print("Nome: {1}, Idade: {0}, Nome: {1} {1}".format(idade,nome)) 
print("Nome: {nome}, Idade: {idade}".format(nome=nome,idade=idade))
print("Nome: {name}, Idade: {age}".format(age=idade,name=nome))  
print("Nome: {name}, Idade: {age} {name} {name}".format(age=idade,name=nome))  
print("-----------------------")
print("Dictionary")
print("Nome: {nome}, Idade: {idade}".format(**dados))
print("-----------------------")
print("f-string")
print(f"Nome: {nome}, Idade: {idade}, Saldo: {saldo:.2f}")

