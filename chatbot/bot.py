print("=== Chatbot con decisiones ===")
nombre = input("¿Cómo te llamás? ")
print(f"¡Hola {nombre}! Escribime algo (por ejemplo: hola, contame un chiste, chau)")
cantidad_mensajes=0
# Diccionario: clave = palabra que buscamos, valor = respuesta del bot
respuestas = {
    "hola": "¡Hola! ¿Cómo estás?",
    "chiste": "¿Qué le dice un jardinero a otro? Nos vemos cuando podamos.",
    "no hablar": "Intentalo de nuevo...",
    "nose": "No te aflijas, ¿Puedo contarte algo mío? Por ejemplo hoy tengo mucho sueño",
}
palabras_salida = ["salir", "adios", "adiós", "bye", "chau"]
while True:  # loop infinito: se corta solo con el break
    cantidad_mensajes=cantidad_mensajes+1 #cantidad_mensajes += 1
    mensaje = input("Vos: ").lower() # pasamos todo a minusculas para comparar mas facil
    if mensaje in palabras_salida:
        print("Bot: ¡Listo! Fue un gusto charlar, nos vemos.")
        print(f"Cantidad de mensajes recibidos: {cantidad_mensajes}")
        break

    # Buscamos si alguna clave del diccionario está contenida en el mensaje
    encontrada = False
    for clave in respuestas:
        if clave in mensaje:
            print(f"Bot: {respuestas[clave]}")
            encontrada = True
            break  # ya encontramos una respuesta, no seguimos buscando
    
    if not encontrada:
        print("Bot: No te entendí muy bien, ¡pero estoy aprendiendo!")