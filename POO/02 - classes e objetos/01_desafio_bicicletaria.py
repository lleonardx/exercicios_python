class Bicicleta:
    def __init__(self, cor, modelo, ano, valor, marcha):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.marcha = 1
        
    def buzinar(self):
        print("Plim plim")
        
    def parar(self):
        print("Parando bicicleta...")
        print("bicicleta parada.")
        
    def correr(self):
        print("vrumm")
    
    def trocar_marcha(self, nro_marcha):
        print("Trocando marcha")  
        
        def _trocar_marcha(nro_marcha):  
            if nro_marcha > self.marcha:
                print("Marcha trocada...")  
            else:
                print("Não foi possivel trocar de marcha")
    
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"    
            
        
b1 = Bicicleta("Preta", "Vulcan", 2022, 1250, 2)

b1.buzinar()
b1.correr()
b1.parar()

print(b1.cor, b1.modelo, b1.ano, b1.valor, b1.marcha)
