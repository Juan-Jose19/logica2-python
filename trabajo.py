def mostrar_tablero(intentos):
    partes_cuerpo = [
        " O",
        "/|\\",
        "/ \\"
    ]
    dibujo = [
        "____",
        "|/        |     "
    ]
    for i in range(intentos):
        dibujo.append("|       {}     ".format(partes_cuerpo[i]))
    for i in range(len(dibujo), 8):
        dibujo.append("|             ")
    dibujo.append("|_          ")
    dibujo.append("\n")
    return "\n".join(dibujo)

def jugar_ahorcado():
    palabra = "python"
    letras_adivinadas = []
    intentos = 0
    max_intentos = len(palabra) + 2

    print("¡Bienvenido al juego del ahorcado!")
    print("Adivina la palabra:")
    print("_ " * len(palabra))

    while True:
        letra = input("Ingresa una letra: ").lower()

        if len(letra) != 1:
            print("Por favor, ingresa solo una letra.")
            continue

        if letra in letras_adivinadas:
            print("Ya has adivinado esa letra. Intenta con otra.")
            continue

        letras_adivinadas.append(letra)

        if letra in palabra:
            print("¡Correcto!")
        else:
            intentos += 1
            print("Incorrecto.")

        print(mostrar_tablero(intentos))

        palabra_mostrada = ""
        for letra_palabra in palabra:
            if letra_palabra in letras_adivinadas:
                palabra_mostrada += letra_palabra + " "
            else:
                palabra_mostrada += "_ "

        print(palabra_mostrada)

        if intentos >= max_intentos:
            print("¡Has perdido! La palabra era: {}".format(palabra))
            break

        if "_" not in palabra_mostrada:
            print("¡Felicidades! ¡Has ganado!")
            break

    reiniciar = input("¿Quieres jugar de nuevo? (s/n): ").lower()
    if reiniciar == "s":
        jugar_ahorcado()
    else:
        print("Gracias por jugar. ¡Hasta luego!")

jugar_ahorcado()
