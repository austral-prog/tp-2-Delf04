#necesitamos saber qué país esta primero en el diccionario
#La respuesta debería tener el siguiente formato (Donde X es Bangladesh e Y es Barbados):

#The result of X comes first in the dictionary than Y is True/False.
#The result of Y comes first in the dictionary than X is True/False.

def earth():
    x = "Bangladesh"
    y = "Barbados"

    print(f"The result of {x} comes first in the dictionary than {y} is {x>y}")
    print(f"The result of {y} comes first in the dictionary than {x} is {y>x}")

earth()