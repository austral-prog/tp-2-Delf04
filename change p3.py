#Escribir un programa que dado dos números reales que representan el gasto 
#efectuado por una persona y la cantidad pagada, imprima en pantalla el informe de la cantidad de pesos y centavos a devolver.
#Hay que respetar el formato del informe (incluido la prolijidad con los espacios y saltos de linea). 

# Un ejemplo de un informe es:

#Ingresar gasto:
#23.75
#Dinero recibido
#100

#Vuelto

#Pesos:
#76
#Centavos:
#25


 
    
#5change()



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