
def sueldo(horas_dia_scheduled, horas_dia_off, horas_nocturnas, pago_porhora, deducciones):

    Extras = (horas_dia_scheduled - 44) * 1.35
    horas_dia_off = horas_dia_scheduled * 2
    horas_nocturnas = horas_dia_scheduled * 1.15
    if horas_dia_scheduled <= 44:
        Sueldo = (horas_dia_scheduled * pago_porhora) + (horas_dia_off * pago_porhora) + (horas_nocturnas * pago_porhora)
    elif horas_dia_scheduled > 44:    
        Sueldo = (Extras * pago_porhora) + ((horas_dia_scheduled - Extras) * pago_porhora) + (horas_dia_off * pago_porhora) + (horas_nocturnas * pago_porhora)
    elif horas_dia_scheduled < 0:
        print ("Error, debes ingresar una cantidad de horas validas, mayor que cero!!")
    else:
        print ("Ingrese un valor valido y mayor que cero")
    SFS = Sueldo * 0.0304
    AFP = Sueldo * 0.0287
    Sueldo_bruto = Sueldo 
#Arreglar IRS,se calcula mensual
    if Sueldo_bruto < 34685:
        sueldo_neto = Sueldo_bruto - (SFS + AFP) - deducciones
        return sueldo_neto
    if Sueldo_bruto >= 34685 and Sueldo_bruto <= 52027.416666667:
        sueldo_neto = Sueldo_bruto - ((Sueldo_bruto - 34685)*0.15) - (SFS + AFP) - deducciones
        return sueldo_neto
    if Sueldo_bruto >= 52027.416666667 and Sueldo_bruto <= 72260.25:
        IRS0 = 34685
        IRS15 = 17342.416666667*0.15
        IRS20 = (Sueldo_bruto - IRS0 - 17342.416666667) * 0.20
        sueldo_neto = Sueldo_bruto - IRS20 - IRS15 - (SFS + AFP) - deducciones
        return sueldo_neto
    if Sueldo_bruto > 72260.25:
        IRS0 = 34685
        IRS15 = 17342.416666667*0.15
        IRS20 = 20232.833333333* 0.20
        IRS25 = (Sueldo_bruto - IRS0 - 17342.416666667 - 20232.833333333) * 0.25
        sueldo_neto = Sueldo_bruto - IRS25 - IRS20 - IRS15 - (SFS + AFP) - deducciones
        return sueldo_neto  

def informacion():
    nombre = input ("Ingrese su nombre y apellido: ")
    pago_por_hora = int(input("Ingrese su pago por hora: "))
    horas_scheduled = int(input("Ingrese la cantidad de horas normales: "))
    horas_nocturnas = int(input("Ingrese la cantidad de horas nocturas: "))
    horas_off = int(input("Ingrese la cantidad de horas en su dia off: "))
    deduccion = int(input("Ingrese el total de otras deducciones: "))

    sueldo(horas_scheduled, horas_off, horas_nocturnas, pago_por_hora, deduccion)
    
    