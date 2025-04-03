def change():

    gastos = float(input("Ingresar gasto correspondiente:\n")) 
    dinero_recibido = float(input("Dinero recibido\n"))
    vuelto = dinero_recibido - gastos
    pesos = int(vuelto)
    centavos = ((vuelto - pesos) * 100) 
   
    print("\nVuelto\n")
    print(f"Pesos:\n{pesos}")
    print(f"Centavos:\n{centavos}")

change()
