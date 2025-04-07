def change():

    expense = 23.75
    money = 100
    vuelto = money - expense
    vuelto_pesos = int(vuelto)
    centavos = int((vuelto - vuelto_pesos) * 100)
    print("Ingresar gasto:")
    print(f"{expense}")
    print("Dinero recibido")
    print(f"{money}")
    print("")
    print("Vuelto")
    print("")
    print("Pesos:")
    print(f"{vuelto_pesos}")
    print("Centavos:")
    print(f"{centavos}")
