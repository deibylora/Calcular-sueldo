
def sueldo(horas_dia_scheduled, horas_dia_off, horas_nocturnas, pago_porhora):

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

    SFS = Sueldo * 0.304
    AFP = Sueldo * 0.287
    Sueldo_Neto = Sueldo - (SFS + AFP)


#Arreglar IRS,se calcula mensual, y solamente el prociento aplica si sobrepasa la cantidad
    if Sueldo_Neto < 34685:
        sueldo_IRS = Sueldo_Neto
        return sueldo_IRS
    if Sueldo_Neto >= 34685 and Sueldo_Neto <= 52027.416666667:
        sueldo_IRS = Sueldo_Neto - (Sueldo_Neto * 0.15)
        return sueldo_IRS
    if Sueldo_Neto >= 52027.416666667 and Sueldo_Neto <= 72260.25:
        sueldo_IRS = Sueldo_Neto - (Sueldo_Neto * 0.20)
        return sueldo_IRS
    if Sueldo_Neto > 72260.25:
        sueldo_IRS = Sueldo_Neto - (Sueldo_Neto * 0.25)
        return sueldo_IRS   

def deducciones_adicionales (deducciones_quncenales):
    deduccion = sueldo-deducciones_quncenales