string = input("Digite uma palavra: ")

verifica = 0
for char in string:
    if char.lower() == "a":
        verifica += 1

print("Têm",verifica,"letras 'a' nessa palavra")