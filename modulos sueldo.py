
def sueldo_neto(horas_dia_scheduled, horas_dia_off, horas_nocturnas, pago_porhora):

    Extras = (horas_dia_scheduled - 44) * 1.35
    horas_dia_off = horas_dia_scheduled * 2
    horas_nocturnas = horas_dia_scheduled * 1.15
    if horas_dia_scheduled <= 44:
        return (horas_dia_scheduled * pago_porhora) + (horas_dia_off * pago_porhora) + (horas_nocturnas * pago_porhora)
        
    elif horas_dia_scheduled > 44:    
        return (Extras * pago_porhora) + ((horas_dia_scheduled - Extras) * pago_porhora) + (horas_dia_off * pago_porhora) + (horas_nocturnas * pago_porhora)

    elif horas_dia_scheduled < 0:
        print ("Error, debes ingresar una cantidad de horas validas, mayor que cero!!")
    else:
        print ("Ingrese un valor valido y mayor que cero")

def ars_planbasico ():
    ARS_basico = sueldo_neto * 0.304
    AFP = sueldo_neto * 0.287
    return sueldo_neto + ARS_basico + AFP




