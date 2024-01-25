class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print("Iniciando classe..")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado
        
    def __del__(self):    
        print("Removendo instancia da classe.")

    def falar(self):
        print("auau")
    
def criar_cachorro():
        c = Cachorro("Zeus", "Preto e Branco")
        print(c.nome)
    
c = Cachorro("Chappie" , "Amarelo")    
c.falar()

print("Olá Mundo")
del c
print("Olá Mundo")
print("Olá Mundo")
print("Olá Mundo")
print("Olá Mundo")

criar_cachorro()