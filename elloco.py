
# Sueldo_bruto = 100000

# SFS = Sueldo_bruto * 0.0304
# AFP = Sueldo_bruto * 0.0287

# IRS0 = 34685
# IRS15 = 17342.416666667*0.15
# IRS20 = 20232.833333333* 0.20
# IRS25 = (Sueldo_bruto - IRS0 - 17342.416666667 - 20232.833333333) * 0.25
# sueldo_neto = Sueldo_bruto - IRS25 - IRS20 - IRS15 - (SFS + AFP)

# print(sueldo_neto)

def name (*nombres):
    for nombre in nombres:
        nombre+=nombre
        capitalizado = nombre.capitalize()
    print (capitalizado)
print(name("deiby", "mirian", "engel", "noel"))