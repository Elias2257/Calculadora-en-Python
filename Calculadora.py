def Menu():
    """Funcion que Muestra el Menu"""
    print """************
Calculadora
************
Menu
1) Suma
2) Resta
3) Multiplicacion
4) Division
5) Salir"""
def Calculadora():
    """Funcion Para Calcular Operaciones Aritmeticas"""
    Menu()
    opc = int(input("Selecione Opcion:\n"))
    while (opc >0 and opc <5):
        x = int(input("Ingrese un Numero:\n"))
        y = int(input("Ingrese otro Numero:\n"))
        if (opc==1):
            print "La Suma de ambos numeros es:", x+y
            opc = int(input("Selecione una Opcion:\n"))
        elif(opc==2):
            print "La Resta de ambos numeros es:",x-y
            opc = int(input("Selecione una Opcion:\n"))
        elif(opc==3):
            print "La Multiplicacion de ambos numero es:",x*y
            opc = int(input("Selecione una Opcion:\n"))
        elif(opc==4):
            try:
              print "La Division de ambos numeros es:", x/y
              opc = int(input("Selecione una Opcion:\n"))
            except ZeroDivisionError:
              print "No se Permite la Division Entre 0"
              opc = int(input("Selecione una Opcion:\n"))
Calculadora()
