
def ejecutar_bisiesto()->None:
    print("Vamos a decidir si un año es bisiesto o no")
    #TODO: completar
    anio = input("ingrese el año que quiere consultar: ")
    bisiestoS = bisiesto(anio)
    print(bisiestoS)

def ejecutar_clasificar()->None:
    print("Vamos a determinar de qué tipo es un triángulo dados sus ángulos")
    a1 = input("Ingrese el angulo 1: ")
    a2 = input("Ingrese el angulo 2: ")
    a3 = input("Ingrese el angulo 3: ")
    print(clasificar(a1, a2, a3))

def ejecutar_solucionar()->None:
    print("Vamos a tratar de hallar las soluciones de una ecuación cuadrática")
    #TODO: completar

def mostrar_menu()->None:
    print ("Menu principal")
    print ("(1) Año bisiesto")
    print ("(2) Tipo de triángulo")
    print ("(3) Solución ecuación cuadrática")

    x = input("Seleccione su opción: ")

    #TODO: ejecuatar una funcionalidad dada la opción seleccionada


def iniciar_aplicacion()->None:
    print("Bienvenido al laboratorio de condicionales")
    mostrar_menu()

#PROGRAMA PRINCIPAL
iniciar_aplicacion()

def bisiesto(anio:int)->bool:
    """
    Returns
    -------
    bool
        retorna true si año es un año bisiesto y false de lo contario

    """
    es_bisiesto= False
    if anio % 4 != 0:
        es_bisiesto= False
    elif anio % 100 != 0:
        es_bisiesto= True
    elif anio % 400 != 0:
        es_bisiesto= False
    else:
        es_bisiesto= True
    return es_bisiesto    

def clasificar(a1:float, a2:float, a3:float)->str:
    """ Retorna "equilatero" si el trangulo es equilatero,"isosceles" si es issosceles y "Escaleno" si es escaleno"""
    clasificacion_triangulo = "nada"
    if a1==a2 and a2==a3:
        clasificacion_triangulo= "equilatero"
    elif a1==a2 or a1==a3 or a2==a3:
        clasificacion_triangulo= "isosceles"
    else:
        clasificacion_triangulo= "escaleno"
    return clasificacion_triangulo