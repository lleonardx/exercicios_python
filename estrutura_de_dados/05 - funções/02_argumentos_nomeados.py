def salvar_carro(marca, modelo, ano, placa):
    #Salvando no banco de dados..
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")
    
salvar_carro("Ford", "Ka", 2016, "DDD-5678")   
salvar_carro(marca="Ford", modelo="KA", ano=2016, placa= "DDD-5678") 
salvar_carro(**{"marca": "Ford", "modelo": "KA", "ano": 2016, "placa": "DDD-5678"})