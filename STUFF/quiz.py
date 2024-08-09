'''
You Can See What I Don't
You Can Change as you wish
I'm Not Nintendo After All (>-<)
Att: KARLX
'''
puntaje_t = 5.0
numero_preguntas = 10
valor_pregunta = puntaje_t / numero_preguntas
index = 1
p_correctas = 0
p_incorrectas = 0

nombre = input("\nIngresa Tu nombre antes del quiz: ")

while nombre != "":
    print("\nBienvenido al quiz. Van a ser", numero_preguntas, "preguntas, y cada una vale", valor_pregunta, "puntos.")
    print("NOTA: Escribe la opción que creas correcta EN MAYÚSCULA\n")
    break

pregunta = 1

while pregunta <= numero_preguntas:
    if pregunta == 1:
        print("1. ¿Cuál es la raíz cuadrada de 25?")
        respuesta = input("A. 12.5\nB. 25\nC. 5\nD. 1\nRTA = ").strip().upper()
        if respuesta == "C":
            p_correctas += 1
        else:
            p_incorrectas += 1

    elif pregunta == 2:
        print("\n2. ¿Cuál es la capital de España?")
        respuesta = input("A. Malaga\nB. Madrid\nC. Barcelona\nD. Cadiz\nRTA = ").strip().upper()
        if respuesta == "B":
            p_correctas += 1
        else:
            p_incorrectas += 1

    elif pregunta == 3:
        print("\n3. Año de Independencia de Colombia:")
        respuesta = input("A. 1789\nB. 1492\nC. 1796\nD. 1810\nRTA = ").strip().upper()
        if respuesta == "D":
            p_correctas += 1
        else:
            p_incorrectas += 1

    elif pregunta == 4:
        print("\n4. ¿Cuál de estas aplicaciones NO es para escuchar música?")
        respuesta = input("A. Amazon Prime Video\nB. Spotify\nC. YouTube Music\nD. Deezer\nRTA = ").strip().upper()
        if respuesta == "A":
            p_correctas += 1
        else:
            p_incorrectas += 1

    elif pregunta == 5:
        print("\n5. ¿Cuál de las siguientes obras es del escritor Gabriel García Márquez?")
        respuesta = input("A. María\nB. La Divina Comedia\nC. Doce Cuentos Peregrinos\nD. Todas las Anteriores\nRTA = ").strip().upper()
        if respuesta == "C":
            p_correctas += 1
        else:
            p_incorrectas += 1

    elif pregunta == 6:
        print("\n6. Año en el que Colombia ganó su primera Copa América")
        respuesta = input("A. 1994\nB. 2001\nC. 1989\nD. 2002\nRTA = ").strip().upper()
        if respuesta == "B":
            p_correctas += 1
        else:
            p_incorrectas += 1

    elif pregunta == 7:
        print("\n7. País más grande del mundo")
        respuesta = input("A. China\nB. Rusia\nC. Marruecos\nD. Ninguna de las anteriores\nRTA = ").strip().upper()
        if respuesta == "B":
            p_correctas += 1
        else:
            p_incorrectas += 1

    elif pregunta == 8:
        print("\n8. Resuelve: x = 136 - 5 x 2")
        respuesta = input("A. 262\nB. 126\nC. 96\nD. 72\nRTA = ").strip().upper()
        if respuesta == "B":
            p_correctas += 1
        else:
            p_incorrectas += 1

    elif pregunta == 9:
        print("\n9. Ingredientes del arroz con pollo")
        respuesta = input("A. Arroz y pollo\nB. Jugo de Maracuyá\nC. Arroz, pollo, etc.\nD. Ninguna de las anteriores\nRTA = ").strip().upper()
        if respuesta == "C":
            p_correctas += 1
        else:
            p_incorrectas += 1

    elif pregunta == 10:
        print("\n10. ¿Disfrutaste este Quiz?")
        respuesta = input("A. Seh\nB. Nonono\nC. Todas las anteriores\nD. Ninguna de las anteriores\nRTA = ").strip().upper()
        if respuesta != "":
            p_correctas += 1
        else:
            p_incorrectas += 1

    pregunta += 1

definitiva = valor_pregunta * p_correctas
print("\n* RESULTADOS: \n")
print("> Tus Respuestas Correctas fueron", p_correctas)
print("> Tus respuestas Incorrectas fueron", p_incorrectas)
print("> Tu puntaje final fue", definitiva)
if definitiva > 2.9:
    print("Pasaste el año, ",nombre)
else:
    print("Desafortunadamente, perdiste el año.")
