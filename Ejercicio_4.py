botella1 = input("Cuantas botellas de menos de 1 litro hay?")
botella2 = input("Cuantas botellas de mas de 1 litro hay?")

deposit1 = (0.10 * int(botella1))
deposit2 = (0.25 * int(botella2))

print("Tienes que devolver la cantidad de " + str(float(deposit1) + float(deposit2)) " euros")
