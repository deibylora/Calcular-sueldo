
#pruebas de codigo

listanumeros = [3,2,6,4,1]

multi = list(map(lambda x: x**2, listanumeros))


filtro = list(filter(lambda x: x==4, listanumeros))

print(multi)
print(filtro)