import pyttsx3

def TTS(texte):
    tts = pyttsx3.init()
    tts.setProperty("voice", "Microsoft Hortense Desktop - French")
    tts.say(texte)
    tts.runAndWait()
