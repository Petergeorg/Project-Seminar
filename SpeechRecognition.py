import speech_recognition as sr 

def recognize_speech():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Bitte sprechen sie etwas...")
        audio = recognizer.listen(source)

    try:
        # Erkennung für Deutsch
        transkription = recognizer.recognize_google(audio, language="de-DE")
        print("Deutsch Transkription: " + transkription)
        check_transkription(transkription)
    except sr.UnknownValueError:
        print("Konnte deutsche Sprache nicht verstehen")
    except sr.RequestError as e:
        print(f"Fehler bei der Anfrage an die Google Speech Recognition API für Deutsch: {e}")

def check_transkription(transkription):
    if "vorwärts" in transkription:
        print("Befehl erkannt: vorwärts")
    elif "rückwärts" in transkription:
        print("Befehl erkannt: rückwärts")
    elif "los" in transkription:
        print("Befehl erkannt: los")
    elif "stopp" in transkription:
        print("Befehl erkannt: stopp")
    elif "rechts" in transkription:
        print("Befehl erkannt: rechts")
    elif "links" in transkription:
        print("Befehl erkannt: links")
    else:
        print("Kein bestimmtes Schlüsselwort erkannt")


if __name__ == "__main__":
    recognize_speech()