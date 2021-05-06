def calcula_preu_total(menjar):

    IVA = round((float(menjar) * 0.1),2)
    Propina = round((float(menjar) * 0,1),2)
    Preu_total = round((float(menjar) + float(IVA) + float(Propina)),2)

    print("Preu del menjar: " + str(float(menjar)))
    print("IVA: " + str(float(IVA)))
    print("Propina: " + str(float(Propina)))
    print("Preu total: " + str(float(Preu_total)))

    print("Tria el plat")
    print("1- Pizza 6€")
    print("2- Ensalada 4€")
    print("3- Kebab 3€")
    print("4- Salmó 8€")

    num_ordre = int(input("Escriu el número del play: "))

    if num_ordre == 1:
        calcula_preu_total(6)
        elif num_ordre == 2:
            calcula_preu_total(4)
            elif num_ordre == 3:
                calcula_preu_total(3)
                elif num_ordre == 4:
                    calcula_preu_total(8)
                    else:
                        print("El plat que has elegit no esta disponible.")