import random


puntaje =0

while True:
    guess = int(input("Cual crees que es el número entre 1 y 10:"))
    numero = random.randint(1,10)

    if guess == numero:
        print("Has adivinado el número")
        puntaje += 1
    elif guess > numero:
        print("El numero que debes adivinar es menor")
    elif guess < numero:
        print("El numero que debes adivinar es mayor")
    else:
        print("No lo adivinaste, ten más suerte la próxima")
        print("el número era:", numero)

    pregunta = input("Quieres dejar de jugar:")
    if pregunta == "si":
        print("Gracias por jugar, tu puntaje es:", puntaje, "puntos")
        break
