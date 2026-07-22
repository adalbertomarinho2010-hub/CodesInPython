import pyttsx3 as x3
voz = x3.init()
vozes = voz.getProperty("voices")
voz.setProperty("voice", vozes[0].id)
texto = input("Digite a mensagem: ")
voz.say(texto)
voz.runAndWait()
voz.save_to_file(texto, "audio.mp3")