import tkinter as tk
import keyboard
import pyautogui
import time
import datetime
from wikirandom import GetRandomInfo
from tts import TTS

# chatKey = None

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.input_label = tk.Label(self, text="Entrer un caractère :")
        self.input_label.pack(side="left")
        self.input_entry = tk.Entry(self)
        self.input_entry.pack(side="left")

        self.size_label = tk.Label(self, text="Taille maximale du message :")
        self.size_label.pack(side="left")
        self.size_entry = tk.Entry(self)
        self.size_entry.pack(side="left")

        self.submit_button = tk.Button(self, text="Soumettre", command=self.submit)
        self.submit_button.pack(side="left")
        self.key = None
        self.max_size = None

    def submit(self):
        char = self.input_entry.get()
        max_size = self.size_entry.get()
        try:
            max_size = int(max_size)
            if max_size > 0:
                if len(char) == 1:
                    self.key = char
                    self.max_size = max_size
                    self.master.destroy()
                else:
                    TTS("Vous devez entrer une seule touche")
            else:
                TTS("La taille maximale du message doit être supérieure à 0")
        except ValueError:
            TTS("La taille maximale du message doit être un nombre entier")

def script():
    heure_actuelle = datetime.datetime.now().strftime("%H:%M")
    message3 = GetRandomInfo()
    while True:
        if keyboard.is_pressed('ctrl+1'):
            print("1")
            pyautogui.press(chatKey)
            keyboard.write("GG a vous les copains")
            pyautogui.press('enter')
        if keyboard.is_pressed('ctrl+2'):
            heure_actuelle = datetime.datetime.now().strftime("%H:%M")
            heure = datetime.datetime.now().strftime("%H")
            pyautogui.press(chatKey)
            if int(heure) > 21 and int(heure) < 6:
                message2 = "Il est actuellement " + heure_actuelle
            else:
                message2 = "Il est actuellement " + heure_actuelle
            for c in message2:
                keyboard.write(c)
                time.sleep(0.01) # attendez 0,1 seconde entre chaque frappe de clavier
            pyautogui.press('enter')
        if keyboard.is_pressed('ctrl+3'):

            messages = []
            while message3:
                if len(message3) > longeurMax:
                    last_space_index = longeurMax
                    messages.append(message3[:last_space_index])
                    message3 = message3[last_space_index:]
                elif len(message3) > int(0.9*longeurMax):
                    last_space_index = message3[:int(0.9*longeurMax)].rfind(' ')
                    messages.append(message3[:last_space_index])
                    message3 = message3[last_space_index+1:]
                else:
                    messages.append(message3)
                    message3 = ""
                    
            for x in messages:
                pyautogui.press(chatKey)
                for c in x:
                    keyboard.write(c)
                    #time.sleep(0.001) # attendez 0,1 seconde entre chaque frappe de clavier
                pyautogui.press('enter')
            message3 = GetRandomInfo()
        time.sleep(0.01)


root = tk.Tk()
app = Application(master=root)
app.mainloop()

chatKey= app.key
longeurMax = app.max_size
print("La touche pour ouvrir le chat est :", chatKey)
print("La longeur max d'un message est :", longeurMax)

if chatKey != None:
    TTS("Vous avez sélectionné" + chatKey)
    print("Le script est lancé . . .")
    script()
else:
    print("On abandonne")

