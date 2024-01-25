class Animal:
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas
        
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join
    ([f'{chave} = {valor}' for chave, valor in self.
    __dict__.items()])}"    
         

class Manifero(Animal):
    def __init__(self, cor_pelo, **kw):
        self.cor_pelo = cor_pelo
        super().__init__(**kw)
        
class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        self.cor_bico = cor_bico
        super().__init__(**kw)


class Gato(Manifero):
    pass

class Ornitorrinco(Manifero, Ave):
    def __init__(self, cor_bico, cor_pelo, nro_patas):
        super().__init__(cor_bico = cor_bico, cor_pelo = cor_pelo,
                         nro_patas = nro_patas)


gato = Gato(nro_patas = 4, cor_pelo = "Preta")
print(gato)

ornitorrinco = Ornitorrinco(nro_patas = 2, cor_pelo = "Marrom", cor_bico = "Laranja")
print(ornitorrinco)

class Leao(Manifero):
    pass

class Cachorro(Manifero):
    pass