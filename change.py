def change():

    expense = 23.75
    money = 100
    vuelto = money - expense
    centavos = (vuelto % 1) * 100
    print("Ingresar gasto:")
    print(f"{expense}")
    print("Dinero recibido")
    print(f"{money}")
    print("")
    print("Vuelto")
    print("")
    print("Pesos")
    print(f"{vuelto.__int__()}")
    print("Centavos")
    print(f"{centavos}")
