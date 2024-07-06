from modulos_sueldo import sueldo, informacion

while True:
    menu_principal = input("""Calculadora de sueldo, seleccione una opcion:

            1-Calcular sueldo por quincena
            2-Calcular sueldo mensual
            3-Calcular doble sueldo\n""")
    
    #corregir esto
    if menu_principal in ("1", "2", "3", "4"):
        if menu_principal == "1":
            print (informacion())
        elif menu_principal == "2":
            print (informacion())
        elif menu_principal == "3":
            print (informacion())
        else:
            print ("Elija una opcion correcta:\n")
#prueba


