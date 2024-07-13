
def sueldo(horas_dia_scheduled, horas_dia_off, horas_nocturnas, pago_porhora, deducciones):

    Extras = (horas_dia_scheduled - 44) * 1.35
    horas_dia_off = horas_dia_off * pago_porhora * 2
    horas_nocturnas = horas_nocturnas* pago_porhora * 1.15
    if horas_dia_scheduled <= 44:
        Sueldo = (horas_dia_scheduled * pago_porhora) + (horas_dia_off) + (horas_nocturnas)
    elif horas_dia_scheduled > 44:    
        Sueldo = (Extras * pago_porhora) + ((horas_dia_scheduled - Extras) * pago_porhora) + (horas_dia_off) + (horas_nocturnas)
    elif horas_dia_scheduled < 0:
        print ("Error, debes ingresar una cantidad de horas validas, mayor que cero!!")
    else:
        print ("Ingrese un valor valido y mayor que cero")
    SFS = Sueldo * 0.0304
    AFP = Sueldo * 0.0287
    Sueldo_bruto = Sueldo 

    if Sueldo_bruto < 34685:
        IRSfinal = 0
        sueldo_neto = Sueldo_bruto - IRSfinal - (SFS + AFP) - deducciones
        return f"""----------Paystub------------
        
        Total de ingresos:                {Sueldo_bruto}
        Seguro basico:                    {SFS}, AFP: {AFP}
        Impuestos sobre la renta:         {IRSfinal}
        deduciones extras:                {deducciones}
        Ingreso neto:                     {sueldo_neto}\n""" 
    
    if Sueldo_bruto >= 34685 and Sueldo_bruto <= 52027.416666667:
        IRSfinal = (Sueldo_bruto - 34685)*0.15
        sueldo_neto = Sueldo_bruto - IRSfinal - (SFS + AFP) - deducciones
        return f"""----------Paystub------------
        
        Total de ingresos:                {Sueldo_bruto}
        Seguro basico:                    {SFS}, AFP: {AFP}
        Impuestos sobre la renta:         {IRSfinal}
        deduciones extras:                {deducciones}
        Ingreso neto:                     {sueldo_neto}\n""" 
    
    if Sueldo_bruto >= 52027.416666667 and Sueldo_bruto <= 72260.25:
        IRS0 = 34685
        IRS15 = 17342.416666667*0.15
        IRSfinal = (Sueldo_bruto - IRS0 - 17342.416666667) * 0.20
        sueldo_neto = Sueldo_bruto - IRSfinal - IRS15 - (SFS + AFP) - deducciones
        return f"""----------Paystub------------
        
        Total de ingresos:                {Sueldo_bruto}
        Seguro basico:                    {SFS}, AFP: {AFP}
        Impuestos sobre la renta:         {IRSfinal}
        deduciones extras:                {deducciones}
        Ingreso neto:                     {sueldo_neto}\n""" 
    if Sueldo_bruto > 72260.25:
        IRS0 = 34685
        IRS15 = 17342.416666667*0.15
        IRS20 = 20232.833333333* 0.20
        IRSfinal = (Sueldo_bruto - IRS0 - 17342.416666667 - 20232.833333333) * 0.25
        sueldo_neto = Sueldo_bruto - IRSfinal - IRS20 - IRS15 - (SFS + AFP) - deducciones

        return f"""----------Paystub------------
        
        Total de ingresos:                {Sueldo_bruto}
        Seguro basico:                    {SFS}, AFP: {AFP}
        Impuestos sobre la renta:         {IRSfinal}
        deduciones extras:                {deducciones}
        Ingreso neto:                     {sueldo_neto}\n""" 

def informacion():
    pago_hora = int(input("Ingrese su pago por hora: "))
    horas_normal = int(input("Ingrese la cantidad de horas normales: "))
    horas_noche = int(input("Ingrese la cantidad de horas nocturas: "))
    horas_off = int(input("Ingrese la cantidad de horas en su dia off: "))
    deduccion = float(input("Ingrese el total de otras deducciones: "))

    print(sueldo(horas_normal, horas_off, horas_noche, pago_hora, deduccion))
    