matematicas= float(input("escriba su promedio en matematicas "))
quimica= float(input("escriba su promedio en quimica "))
espanol= float(input("escriba su promedio en español "))
Historia=float(input("escriba su promedio en historia "))

promedio= (matematicas + quimica + espanol + Historia) / 4
print("su promedio en las distintas materias es:", promedio)

if promedio < 70:
    print("reprobaste")
    if promedio <=80:
        print("debes ir a asesorias")
elif promedio <=80:
    print("puedes mejorar")
elif promedio <= 90:
    print("buen promedio")
elif promedio >= 98:
    print("excelente")
